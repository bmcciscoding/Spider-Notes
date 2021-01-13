import scrapy

print('hello')

class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.dytt8.net/index.htm/']

    def parse(self, response):
        body_filename = 'body.html'
        open(body_filename, 'wb').write(response.body)
