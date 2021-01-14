import scrapy

from movie.items import MovieItem


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.dytt8.net/index.htm']

    def parse(self, response):
        # list = response.xpath('//a').extract()
        sel_list = response.xpath('//a')
        for sel in sel_list:
            item = MovieItem()
            item['link'] = sel.xpath('@href').extract()
            item['name'] = sel.xpath('text()').extract()
            yield item
