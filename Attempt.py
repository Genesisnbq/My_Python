from urllib import request


class Spider():
    url = '[图片]https://www.douyu.com/g_LOL'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        a = 1
        print(a);

    def go(self):
        self.__fetch_content()

spider = Spider()  # 实例化
spider.go()
