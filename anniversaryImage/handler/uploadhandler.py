#!/usr/bin/env python

import tornado.web
from anniversaryImage.service import fileservice


class UploadImageHandler(tornado.web.RequestHandler):
    def post(self):
        # ファイルの削除
        fileservice.remove_file()

        # ファイルの読み込み
        file = self.request.files
        fileservice.get_file(file)

        # ページ遷移
        self.render("result.html", message="Finish!!!!!!!")


if __name__ == "__main__":
    UploadImageHandler()
