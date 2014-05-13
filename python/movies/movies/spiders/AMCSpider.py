from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy import log

from movies.items import AMCItem


class AMCSpider(Spider):
    """
    Spider for Craigslist
    """

    name = "amc-spider"
    allowed_domains = "amctheatres.com"

    start_urls = ['https://www.amctheatres.com/movie-theatres/amc-loews-village-7']

    def parse(self, response):
        """
        Parse the data from the spider
        """
        sel = Selector(response)
        sites = sel.css('p.nav-link+script')
        items = []

        #start logging
        log.msg("Begin Log", level=log.INFO)

        for site in sites:
            item = AMCItem()

            item['data'] = site.extract()
            items.append(item)

        return items
