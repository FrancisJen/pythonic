from urllib import request

class Spider():
    url = 'https://www.douyu.com/g_LOL'
    def __fetch_data(self):
        r = request.urlopen(Spider.url)
        # bytes
        html = r.read()
        html = str(html, encoding="utf=8")
        a = 1

    def go(self):
        self.__fetch_data()

spider = Spider()
spider.go()