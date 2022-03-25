import os

import requests
from dotenv import load_dotenv

import check_file_extension


def fetch_nasa_photo(token, url, path):
    payload = {"api_key": token, "count": 50}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    image_information = response.json()

    for numeration, image_info, in enumerate(image_information, start=1):
        picture_request = requests.get(image_info["url"])

        picture_request.raise_for_status()

        if not check_file_extension.define_extension(image_info["url"]):
            continue

        photo_extension = check_file_extension.define_extension(image_info["url"])

        with open(f'{path}Nasa_{numeration}{photo_extension}', "wb") as file:
            file.write(picture_request.content)


def main():
    load_dotenv()
    token = os.getenv("NASA_TOKEN")
    path = "image/nasa/"
    path_check = os.makedirs(f"{path}", exist_ok=True)
    url = "https://api.nasa.gov/planetary/apod"
    fetch_nasa_photo(token, url, path)


if __name__ == "__main__":
    main()
