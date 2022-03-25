import os
import urllib.parse
import requests

import check_file_extension


def fetch_spacex_launch(url, path):
    response = requests.get(url)
    response.raise_for_status()

    for page in response.json():

        links = page["links"]["flickr_images"]

        if len(links) > 5:
            for numeration, link in enumerate(links, start=1):
                image_download = requests.get(link)
                image_download.raise_for_status()
                photo_extension = check_file_extension.define_extension(link)
                with open(f'{path}spaceX_{numeration}{photo_extension}', "wb") as file:
                    file.write(image_download.content)
            break


def main():
    path = "image/spacex/"
    path_check = os.makedirs(f"{path}", exist_ok=True)
    url = "https://api.spacexdata.com/v3/launches/"
    fetch_spacex_launch(url, path)


if __name__ == "__main__":
    main()
