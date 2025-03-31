import time

from flask import Flask, render_template, request, send_file
import requests
import json
from datetime import datetime
import os

import obs
import Statistik

app = Flask(__name__)

def print_error(e):
    return f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | >>> {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uri_raw_1 = request.form['playlist_url_1']
        uri_raw_2 = request.form['playlist_url_2']

        result_1 = handle_message(uri_raw_1)
        result_2 = handle_message(uri_raw_2)

        # Запуск функций после успешного сохранения файлов
        obs.OBSIE()
        col_poh_trekov_result = Statistik.col_poh_trekov()
        proc_shoshesti_result = Statistik.proc_shoshesti()


        # Чтение данных из файла common_elements.txt
        try:
            with open('common_elements.txt', 'r', encoding='utf-8') as file:
                common_elements = file.read()
        except FileNotFoundError:
            common_elements = "Файл common_elements.txt не найден."

        return render_template("result.html",
                               col_poh_trekov_result=col_poh_trekov_result,
                               proc_shoshesti_result=proc_shoshesti_result,
                               common_elements=common_elements)

    return render_template("index.html")

def handle_message(uri_raw):
    try:
        uri_raw = uri_raw.strip()
        uri_parts = uri_raw.split('?')[0].split('/')

        owner = uri_parts[4]
        kinds = uri_parts[6]

        uri = f"https://music.yandex.ru/handlers/playlist.jsx?owner={owner}&kinds={kinds}"
        response = requests.get(uri)
        response.raise_for_status()

        data = response.json()
        playlist_title = data['playlist']['title']
        tracks = data['playlist']['tracks']

        # Получение URL обложки плейлиста
        cover_url = data['playlist']['cover'] if 'cover' in data['playlist'] else None

        all_file = ""

        for track in tracks:
            artists_names = ", ".join(artist['name'] for artist in track['artists'])
            full_track = f"{artists_names} - {track['title']}\n"
            all_file += full_track

        filename = f"{playlist_title}_{owner}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(all_file)

        # Сохранение URL обложки в текстовый файл
        if cover_url:
            cover_filename = f"{playlist_title}_cover.jpg"
            cover_response = requests.get(cover_url)
            with open(cover_filename, 'wb') as cover_file:
                cover_file.write(cover_response.content)

        return f"Плейлист сохранен в файл: {filename}<br>Обложка сохранена в файл: {cover_filename if cover_url else 'Нет обложки'}<br>Поддержите работу сервиса: https://u-pov.ru/donate. Спасибо за использование! 💜"

    except (json.JSONDecodeError, requests.exceptions.RequestException) as e:
        return f"Ошибка! {print_error(e)}"
    except IndexError as e:
        return f"Ошибка! {print_error(e)}"
    except Exception as e:
        return f"Ошибка! {print_error(e)}"

@app.route("/download")
def download_file():
    path = os.getcwd() + "/common_elements.txt"
    return send_file(path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)