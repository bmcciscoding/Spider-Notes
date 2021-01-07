import scrapy


class ImdbItem(scrapy.Item):
    title = scrapy.Field()


class ExampleSpider(scrapy.Spider):
    name = "imdb"
    start_urls = [
        # "https://www.imdb.com/what-to-watch/fan-favorites/?ref_=watch_tpks_tab",
        "https://www.dytt8.net/index.htm",
    ]

    items = []

    def parse(self, response):

        items = []

        item = ImdbItem()
        item["title"] = "test"

        items.append(item)
        print("add")
        print(items)
        # print(response.body)
        # xpahtstring = '//*[@id="header"]/div/div[3]/div[2]/div[2]/div[1]/div/div[2]/div[2]/ul/table/tbody/tr[3]/td[1]/a[2]'
        # for sel in response.xpath("//td"):
        #     item = ImdbItem()
        #     item["title"] = "test"
        #     items.append(item)
        # item["title"] = sel.xpath("//a").extract()

        return items
