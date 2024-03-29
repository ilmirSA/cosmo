import os
import urllib.parse


def define_extension(url):
    # разбивает ссылку на разнные части такие как path netloc
    parsed_link = urllib.parse.urlparse(url)

    # берет из parsed_link второй индекс и отделяет от него расширение.
    extension = os.path.splitext(parsed_link[2])

    if extension[1].endswith(("jpg", "jpeg", "png", "gif")):
        return extension[1]
    else:
        False


# u = "https://www.youtube.com/embed/tvB0mdkrG3Q?rel=0"
# i = 'https://apod.nasa.gov/apod/image/9909/moon3_cassini.jpg'
# print(define_extension(u))
