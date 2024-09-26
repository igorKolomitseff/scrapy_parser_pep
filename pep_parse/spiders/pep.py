import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse_pep(self, response):
        yield PepParseItem({
            'number': int(response.xpath(
                '//ul[@class="breadcrumbs"]/li[contains(., "PEP")]/'
                'following-sibling::li/text()'
            ).get().replace('PEP ', '')),
            'name': ''.join(response.xpath(
                '//h1[@class="page-title"]//text()'
            ).getall()),
            'status': response.xpath(
                '//dt[contains(., "Status")]/'
                'following-sibling::dd[1]/abbr/text()'
            ).get()
        })

    def parse(self, response):
        pep_links = response.xpath(
            '//*[@id="numerical-index"]//table[contains(@class, '
            '"pep-zero-table")]/tbody/tr/td[a][1]/a/@href'
        ).getall()
        for pep_link in pep_links:
            yield response.follow(pep_link, callback=self.parse_pep)
