from pytube import YouTube
from pytube.cli import on_progress
from pathlib import Path
import concurrent.futures

music_dir = Path.home() / "Desktop" / "music"
Path(music_dir).mkdir(parents=True, exist_ok=True)

link_list = []


def download(link):
    yt = YouTube(
        link,
        on_progress_callback=on_progress,
    )
    yt.streams.filter(only_audio=True).first().download(music_dir)
    print("start downloading")


def download_proccess():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download, link_list)


while True:
    enter_link = input("[f] - finish\nenter youtube link ")
    if enter_link == "f":
        download_proccess()
        break
    link_list.append(enter_link)
