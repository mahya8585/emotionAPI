#!/usr/bin/env python

import os
import requests
from PIL import Image


FORM_NAME = "photo"
FILE_NAME = "static/img/target.jpg"
TEMPORARY_FILE_NAME = "static/img/tmp.jpg"
MAX_PX = 4096


def get_file(files):
    """
    multipart/formで送付されたfileを取得する
    :param files: byteファイル
    :return: ファイルパス
    """

    file = files[FORM_NAME][0]["body"]
    mime = files[FORM_NAME][0]["content_type"]

    # とりあえずjpgにだけ対応・・・
    if mime == "image/jpeg":
        f = open(FILE_NAME, "bw")
        f.write(file)
        f.close()
    else:
        print("対応していないcontent_typeです")

    return FILE_NAME


def remove_file():
    """
    指定ファイルを削除する。
    ここではfile_name
    """
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)


def resize_img():
    """
    max_sizeより大きいファイルは画像のリサイズを行う。
    """
    target = Image.open(FILE_NAME)
    target_size = target.size
    print(target_size)

    if (target_size[0]) > MAX_PX or (target_size[1] > MAX_PX):
        target.thumbnail((MAX_PX, MAX_PX), Image.ANTIALIAS)
        target.save(TEMPORARY_FILE_NAME, quality=100)
        remove_file()
        os.rename(TEMPORARY_FILE_NAME, FILE_NAME)

        print("resize, done!")
        print(target.size)


def get_demo_file(file_path):
    """
    fileを取得する
    :param filepath イメージURL
    :return: ファイルパス
    """
    img = requests.get(file_path)
    with open(FILE_NAME, 'wb') as file:
        file.write(img.content)

    return FILE_NAME
