"""Script to sort & move files older than 7 days."""
import os
import shutil
from datetime import datetime


# File extensions to sort
image_formats = ["jpg", "png", "bmp", "gif"]
audio_formats = ["mp3", "ogg", "wav"]
video_formats = ["mp4", "avi"]
doc_formats = ["pdf", "txt", "rtf"]

# Directories to sort into
directories = ["images", "audio", "videos", "documents", "other"]


def init_directories() -> None:
    """Create directories to sort into."""
    os.chdir("./Sorted")
    folder = os.getcwd()

    for directory in directories:
        if not os.path.isdir(os.path.join(folder, directory)):
            os.mkdir(os.path.join(folder, directory))


def last_modified(file):
    """Return when was the file last modified (in days)."""
    today = datetime.today()
    file_last_modified = os.stat(file).st_mtime

    return abs(datetime.fromtimestamp(file_last_modified) - today).days


init_directories()

os.chdir("../Stuff")  # Move to directory from where to sort files

for file in os.listdir():
    if not os.path.isfile(file):
        continue

    # Check if file was modified more than 7 days ago
    if last_modified(file) <= 7:
        continue

    extension = file.split(".")[-1].lower()

    if extension in image_formats:
        shutil.move(file, "../Sorted/images")
    elif extension in audio_formats:
        shutil.move(file, "../Sorted/audio")
    elif extension in video_formats:
        shutil.move(file, "../Sorted/videos")
    elif extension in doc_formats:
        shutil.move(file, "../Sorted/documents")
    else:
        shutil.move(file, "../Sorted/other")
