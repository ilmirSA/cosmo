import os
import urllib.parse
import requests


def define_extension(url):
    # разбивает ссылку на разнные части такие как path netloc
    parsed_link = urllib.parse.urlparse(url)

    # берет из parsed_link второй индекс и отделяет от него расширение.
    extension = os.path.splitext(parsed_link[2])

    if extension[1].endswith(("jpg", "jpeg", "png", "gif")):
        return extension[1]


def path_check(path):
    os.makedirs(f"{path}", exist_ok=True)


def main():
    path = "image/spacex/"
    path_check(path)
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


if __name__ == "__main__":
    main()
