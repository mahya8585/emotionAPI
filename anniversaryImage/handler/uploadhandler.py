#!/usr/bin/env python

import tornado.web
from anniversaryImage.service import fileservice
from anniversaryImage.service import cognitive
from anniversaryImage.service import response


class UploadImageHandler(tornado.web.RequestHandler):
    def post(self):
        # ファイルの削除
        fileservice.remove_file()

        # ファイルの読み込み
        file_path = fileservice.get_file(self.request.files)
        fileservice.resize_img()

        # 感情チェック
        score = cognitive.run_emotion_check(file_path)
        no1_emotion = cognitive.get_no1_emotion_name(score)

        # ページ遷移
        self.render("result.html",
                    score=response.convert_from_intarray(score.values()),
                    label=response.convert_from_strarray(score.keys()),
                    emotion_name=no1_emotion
                    )


if __name__ == "__main__":
    UploadImageHandler()
