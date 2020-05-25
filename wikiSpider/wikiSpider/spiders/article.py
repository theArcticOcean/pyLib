import scrapy

class ArticleSpider( scrapy.Spider ):
    name='simple_article'

    def start_requests(self):
        urls = [
            'https://wiki.mbalib.com/wiki/%E9%9D%9E%E8%90%A5%E5%88%A9%E7%BB%84%E7%BB%87',
            'https://wiki.mbalib.com/wiki/%E7%BB%B4%E5%9F%BA%E5%AA%92%E4%BD%93%E5%9F%BA%E9%87%91%E4%BC%9A',
            'https://wiki.mbalib.com/wiki/GNU%E8%87%AA%E7%94%B1%E6%96%87%E6%A1%A3%E8%AE%B8%E5%8F%AF%E8%AF%81'
        ]
        return [ scrapy.Request(url=_url, callback=self.parse) for _url in urls ]

    def parse(self, response):
        url = response.url
        title = response.css('h1')
        print( 'URL: {}'.format(url) )
        print( 'Title: {}'.format(title) )