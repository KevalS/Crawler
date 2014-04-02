from scrapy.spider import Spider
from scrapy.selector import Selector

from craigslist.items import CraigslistItem

class CraigsListSpider(Spider):

	name = "cl-spider"
	allowed_domains = "craigslist.org"

	start_urls = ['http://newyork.craigslist.org/tia/']

	def parse(self,response):
		sel = Selector(response)
		sites = sel.css('section.body div#toc_rows div.content p.row span.pl')
		items = []

		for site in sites :
			item = CraigslistItem()

			item['name'] = site.css('a::text').extract()
			item['link'] = site.css('a::attr(href)').extract()
			item['date'] = site.css('span.date::text').extract()
			items.append(item)

		return items