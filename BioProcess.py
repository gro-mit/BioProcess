#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
import random
import json

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from Handlers import *
from methods import knn,kmeans,hc

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/",HomeHandler),
            (r"/knn",KnnHandler),
            (r"/pca",PcaHandler),
            (r"/hc",HcHandler),
            (r"/kmeans",KmeansHandler),
            (r"/about",AboutHandler),
            (r"/upload",UploadHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
        )
        tornado.web.Application.__init__(self,handlers,**settings)


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        para = json.loads(self.get_argument("para"))
        if para['type'] == 'knn':
            print type(para['kvalue'])
            print para['weight']
            f = open(os.path.join(os.path.dirname(__file__),"tempfile","knn_train.csv"),"wb")
            f.write(self.request.files["trainset"][0].body)
            f.close()
            f = open(os.path.join(os.path.dirname(__file__),"tempfile","knn_test.csv"),"wb")
            f.write(self.request.files["testset"][0].body)
            f.close()
            result = knn(kvalue=para['kvalue'],weight=para['weight'])
            status = 'sucess'
            respon = {'status':status,'result':result}
            respon_json = tornado.escape.json_encode(respon)
        if para['type'] == 'kmeans':
            print para['kvalue']
            print para['seed']
            f = open(os.path.join(os.path.dirname(__file__),"tempfile","kmeans_data.csv"),"wb")
            f.write(self.request.files["dataset"][0].body)
            f.close()
            result = kmeans(kvalue=para['kvalue'],seed=para['seed'])
            status = 'success'
            respon = {'status':status,'result':result}
            respon_json = tornado.escape.json_encode(respon)
        if para['type'] == 'hc':
            # print para['kvalue']
            f = open(os.path.join(os.path.dirname(__file__),"tempfile","hc_data.csv"),"wb")
            f.write(self.request.files["dataset"][0].body)
            f.close()
            result = hc()
            status = 'success'
            respon = {'status':status}
            respon_json = tornado.escape.json_encode(respon)
        self.write(respon_json)


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(),max_buffer_size=10485760000)
    http_server.listen(options.port)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()

if __name__ == "__main__":
    main()
