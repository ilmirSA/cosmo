import os
import urllib.parse
import requests

import check_file_extension


def main():
    path = "image/spacex/"
    path_check = os.makedirs(f"{path}", exist_ok=True)
    url = "https://api.spacexdata.com/v3/launches/"
    response = requests.get(url)
    response.raise_for_status()

    for number, resp in enumerate(response):

        links = response.json()[number]["links"]["flickr_images"]

        if len(links) > 5:
            for numeration, link in enumerate(links, start=1):
                image_download = requests.get(link)
                with open(f'{path}spaceX_{numeration}{check_file_extension.define_extension(link)}', "wb") as file:
                    file.write(image_download.content)
            break


if __name__ == "__main__":
    main()
