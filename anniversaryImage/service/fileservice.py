#!/usr/bin/env python

import os

form_name = "photo"
file_name = "static/img/target.jpg"


def get_file(files):
    file = files[form_name][0]["body"]
    mime = files[form_name][0]["content_type"]

    # とりあえずjpgにだけ対応・・・
    if mime == "image/jpeg":
        f = open(file_name, "bw")
        f.write(file)
        f.close()
    else:
        print("対応していないcontent_typeです")


def remove_file():
    if os.path.exists(file_name):
        os.remove(file_name)


if __name__ == "__main__":
    get_file()
