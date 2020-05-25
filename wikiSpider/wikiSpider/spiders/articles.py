from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wiki.mbalib.com']
    start_urls = ['https://wiki.mbalib.com/wiki/%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        text = response.xpath('//*[@id="bodyContent"]/p[2]').extract() #use chrome to check element's xpath
        print( "URL: {}".format( url ) )
        print( "Title: {}".format( title ) )
        print( "Text: {}".format( text ) )