import os

import requests
from dotenv import load_dotenv

from fetch_spacex import define_extension, path_check


def main():
    load_dotenv()
    token = os.getenv("NASA_TOKEN")
    path = "image/earth/"
    path_check(path)
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


if __name__ == "__main__":
    main()