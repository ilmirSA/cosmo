import os

import requests
from dotenv import load_dotenv

import check_file_extension


def ftech_eath_photo(token, url, path):
    payload = {"api_key": token}
    response = requests.get(url, params=payload)
    response.raise_for_status()

    for numeration, image_info in enumerate(response.json(), start=1):
        image_name = image_info["image"]
        image_date = image_info["date"]
        image_date = image_date.split(" ")[0].replace("-", "/")

        download_image_url = f"https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_name}.png"

        download_image = requests.get(download_image_url, params=payload)
        download_image.raise_for_status()

        photo_extension = check_file_extension.define_extension(download_image_url)
        with open(f'{path}earth_{numeration}{photo_extension}', "wb") as file:
            file.write(download_image.content)


def main():
    load_dotenv()
    token = os.getenv("NASA_TOKEN")
    path = "image/earth/"
    path_check = os.makedirs(f"{path}", exist_ok=True)
    url = "https://api.nasa.gov/EPIC/api/natural"
    ftech_eath_photo(token, url, path)


if __name__ == "__main__":
    main()
