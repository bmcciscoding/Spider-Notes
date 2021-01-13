import scrapy


class ImdbSpider(scrapy.Spider):
    name = "imdb"
    start_urls = ("https://www.dytt8.net/index.htm",)

    def parse(self, response):
        filename = "imdb.html"

        xpath_str = '//*[@id="header"]/div/div[3]/div[2]/div[2]/div[1]/div/div[3]/div[2]/ul/table/tbody/tr[1]/td[1]/a[2]'
        res = response.xpath("//a").getall()
        for item in res:
            print(item)
