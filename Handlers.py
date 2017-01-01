import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

class KnnHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('knn.html')

class PcaHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('pca.html')

class HcHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('hc.html')

class KmeansHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('kmeans.html')

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('about.html')