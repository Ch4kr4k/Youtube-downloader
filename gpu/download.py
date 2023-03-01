#!/usr/bin/env python

import os
import sys
import string
import random
from pathlib import Path
import argparse
from pytube import YouTube


def on_complete(stream, file_path):
    print(stream)
    print(file_path)


def on_progress(stream, chunk, bytes_remaining):
    print(100 - (bytes_remaining / stream.filesize * 100))


def re(a, b):
    os.remove(a)
    os.remove(b)


def driver(link, resolution):
    tmp0 = "/tmp"
    path = Path.home()
    path = str(path)
    final_path = (path + "/Downloads/Video")
    video_object = YouTube(
        link,
        on_complete_callback=on_complete,
        on_progress_callback=on_progress
    )
    v = random.choice(string.ascii_lowercase)
    v = (v + ".mp4")
    a = random.choice(string.ascii_lowercase)
    a = (a + ".mp4")
    tmp = ("/tmp/" + v)
    tmp1 = ("/tmp/" + a)

    try:
        print("Downloading Video and audio")
        print(tmp)
        #s1 = video_object.streams.filter(resolution="2160p").first()
        #s2 = video_object.streams.filter(resolution="1440p").first()
        #s3 = video_object.streams.filter(resolution="1080p").first()
        video_only = video_object.streams.filter(
            resolution=f"{resolution}").first().download(tmp0, v)
        print(tmp1)
        audio_only = video_object.streams.filter(
            only_audio=True).last().download(tmp0, a)
        print("completed")
        t = video_object.title
        title = (t + ".mp4")
        res = (f'{final_path}/"{title}"')
        os.system(
            f"ffmpeg -i {tmp} -i {tmp1} -c copy -c:v h264_nvenc -map 0:v:0 -map 1:a:0 {res}")
        re(tmp, tmp1)
    except KeyboardInterrupt:
        re(tmp, tmp1)
        print("Removed")
        exit()
    except:
        re(tmp, tmp1)
        print("some error")
        exit()
