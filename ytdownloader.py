from PIL import Image, ImageFont, ImageDraw
from colorama import Fore
import pytube
from pytube import YouTube as yt
import sys
import warnings
import pytube.cli as pyc
import math
from pathlib import Path

if not sys.warnoptions:
    warnings.simplefilter("ignore")


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def mapBitToChar(im, col, row):
    if im.getpixel((col, row)):
        return " "
    else:
        return "#"


def output():
    ShowText = " YT Downloader"
    font = ImageFont.truetype("arialbd.ttf", 9)  # load the font
    size = font.getsize(ShowText)  # calc the size of text in pixels
    image = Image.new("1", size, 1)  # create a b/w image
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), ShowText, font=font)  # render the text to the bitmap
    print(
        Fore.LIGHTCYAN_EX +
        "\n-------------------------------------------------------------------------"
    )
    for r in range(size[1]):
        print(Fore.YELLOW +
              "".join([mapBitToChar(image, c, r) for c in range(size[0])]))
    print(
        Fore.YELLOW +
        "\n                                                        berkebiten (2022)"
    )


def main():
    print(
        Fore.LIGHTCYAN_EX +
        "\n-------------------------------------------------------------------------"
    )
    pytube.request.default_range_size = 1048576  # this is for chunck size, 1MB size
    url = input(Fore.LIGHTCYAN_EX + "Video URL: " + Fore.LIGHTMAGENTA_EX)
    path = str(Path.home() / "Downloads")
    ytube = yt(url, on_progress_callback=pyc.on_progress)
    streams = ytube.streams
    highest_res = streams.get_highest_resolution()
    print(
        Fore.RED + "Downloading..",
        Fore.YELLOW + ytube.title,
        Fore.BLUE + "~",
        convert_size(highest_res.filesize),
        Fore.RED,
    )
    highest_res.download(path)
    print(Fore.GREEN + "Download Completed..")


output()
cont = "1"
while cont == "1":
    main()
    cont = input(
        Fore.LIGHTCYAN_EX +
        "Enter \n-> '1' to download another video \n-> '2' to stop the program\n "
        + Fore.LIGHTMAGENTA_EX)
