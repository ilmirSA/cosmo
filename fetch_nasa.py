import os

import requests
from dotenv import load_dotenv

import check_file_extension


def main():
    load_dotenv()
    token = os.getenv("NASA_TOKEN")
    path = "image/nasa/"
    path_check = os.makedirs(f"{path}", exist_ok=True)
    url = "https://api.nasa.gov/planetary/apod"

    payload = {"api_key": token, "count": 50}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    image_information = response.json()

    for numeration, image_info, in enumerate(image_information, start=1):
        picture_request = requests.get(image_info["url"])
        picture_request.raise_for_status()

        if check_file_extension.define_extension(image_info["url"]) is None:
            # идет проверка ссылки если ссылка возвращает None то он ее пропускает это сделано что бы не скачивать видео файлы
            continue

        with open(f'{path}Nasa_{numeration}{check_file_extension.define_extension(image_info["url"])}', "wb") as file:
            file.write(picture_request.content)


if __name__ =="__main__":
    main()
