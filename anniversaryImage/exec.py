#!/usr/bin/env python
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options, parse_command_line

from handler import mainhandler, uploadhandler, demohandler

define("port", default=8888, help="run on the given port", type=int)


def main():
    parse_command_line()
    application = tornado.web.Application(
        [
            (r"/", mainhandler.MainHandler),
            (r"/image", uploadhandler.UploadImageHandler),
            (r"/demo", demohandler.DemoHandler)
        ],
        template_path=os.path.join(os.path.dirname(__file__), "template"),
        static_path=os.path.join(os.path.dirname(__file__), "static")
    )
    application.listen(options.port)
    print("接続OK")
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
