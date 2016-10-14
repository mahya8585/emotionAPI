#!/usr/bin/env python

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


if __name__ == "__main__":
    MainHandler()
