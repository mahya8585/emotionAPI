#!/usr/bin/env python

import tornado.web
from anniversaryImage.service import cognitive, response, fileservice

DEMO_IMAGE = "https://pbs.twimg.com/media/CSEq_TuU8AEVT3f.jpg"


class DemoHandler(tornado.web.RequestHandler):
    def get(self):
        # ファイルの削除
        fileservice.remove_file()

        # ファイルの読み込み
        file_path = fileservice.get_demo_file(DEMO_IMAGE)
        fileservice.resize_img()

        # 感情チェック
        score = cognitive.run_emotion_check(DEMO_IMAGE)
        no1_emotion = cognitive.get_no1_emotion_name(score)

        # ページ遷移
        self.render("result.html",
                    score=response.convert_from_intarray(score.values()),
                    label=response.convert_from_strarray(score.keys()),
                    emotion_name=no1_emotion
                    )


if __name__ == "__main__":
    DemoHandler()
