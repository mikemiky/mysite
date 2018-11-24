import scrapy
from first_scrapy.items import DemozItem


class DemozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        'http://www.chinadmoz.org/subindustry/8/'
        'http://www.chinadmoz.org/subindustry/23/'
         ]
    def parse(self, response):
        sel = scrapy.selector.Selector()
        sites = response.xpath('//ui[@class="directory-url"]/li')
        items = []
        for site in sites:
            item = DemozItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@herf').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)

        return items