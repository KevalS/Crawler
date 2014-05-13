from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log

from craigslist.items import CraigslistItem

class CraigsListSpider(Spider):
	"""
	Spider for Craigslist
	"""

	name = "cl-spider"
	allowed_domains = "craigslist.org"

	start_urls = ['http://newyork.craigslist.org/tia/']

	def parse(self,response):
		"""
		Parse the data from the spider
		"""
		sel = Selector(response)
		sites = sel.css('section.body div#toc_rows div.content p.row span.pl')
		items = []

		#start logging
		log.msg("Begin Log", level=log.INFO)

		for site in sites :
			item = CraigslistItem()

			item['name'] = site.css('a::text').extract()
			item['link'] = site.css('a::attr(href)').extract()
			item['date'] = site.css('span.date::text').extract()
			items.append(item)

		return items