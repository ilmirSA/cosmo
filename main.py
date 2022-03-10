import os
import urllib.parse

import requests
from dotenv import load_dotenv


# проверяет сущесвует ли папка если нет, то создает ее.
def path_check(path):
    os.makedirs(f"{path}", exist_ok=True)


def define_extension(url):
    # разбивает ссылку на разнные части такие как path netloc
    parsed_link = urllib.parse.urlparse(url)

    # берет из parsed_link второй индекс и отделяет от него расширение.
    extension = os.path.splitext(parsed_link[2])

    if extension[1].endswith(("jpg", "jpeg", "png", "gif")):
        return extension[1]
        # берет  первый индекс из переменной extension там
        # должно храниться расширение файла и проверяет его
        # через endswith если условие верно возвращает расширение файла


# скачивает фотографии Nasa
def nasa_image_download(token, path):
    url = "https://api.nasa.gov/planetary/apod"

    payload = {"api_key": token, "count": 50}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    image_information = response.json()

    for numeration, image_info, in enumerate(image_information, start=1):
        picture_request = requests.get(image_info["url"])
        picture_request.raise_for_status()

        if define_extension(image_info["url"]) == None:
            # идет проверка ссылки если ссылка возвращает None то он ее пропускает это сделано что бы не скачивать видео файлы
            continue

        with open(f'{path}Nasa_{numeration}{define_extension(image_info["url"])}', "wb") as file:
            file.write(picture_request.content)


# скачивает фотографии spaceX
def fetch_spacex_last_launch(path):
    url = "https://api.spacexdata.com/v3/launches/"
    response = requests.get(url)
    response.raise_for_status()

    for page in range(1, 51):
        links = response.json()[page]["links"]["flickr_images"]
        if len(links) > 5:
            for numeration, link in enumerate(links, start=1):
                image_download = requests.get(link)
                with open(f'{path}spaceX_{numeration}{define_extension(link)}', "wb") as file:
                    file.write(image_download.content)
            break


# скачивает фотографии нашей земли от Nasa
def earth_photo(token, path):
    url = "https://api.nasa.gov/EPIC/api/natural"

    payload = {"api_key": token}
    response = requests.get(url, params=payload)
    response.raise_for_status()

    for numeration, image_info in enumerate(response.json(), start=1):
        image_name = image_info["image"]
        image_date = image_info["date"]
        image_date = image_date.split(" ")[0].replace("-", "/")

        download_image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png"

        download_image = requests.get(download_image_url, params=payload)

        with open(f'{path}earth_{numeration}{define_extension(download_image_url)}', "wb") as file:
            file.write(download_image.content)


def main():
    load_dotenv()
    token = os.getenv("NASA_TOKEN")

    path = "image/"
    nasa_image_download(token, path)
    fetch_spacex_last_launch(path)
    earth_photo(token, path)


if __name__ == "__main__":
    main()
