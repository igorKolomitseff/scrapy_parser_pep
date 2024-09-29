import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_DOMAIN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_DOMAIN]
    start_urls = [f'https://{domain}/' for domain in allowed_domains]

    def parse(self, response):
        for pep_link in response.css(
            '#index-by-category table.pep-zero-table > tbody tr >'
            'td:nth-of-type(2) > a::attr(href)'
        ).getall():
            yield response.follow(
                pep_link,
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        yield PepParseItem(
            number=response.css(
                'header > ul.breadcrumbs > li:contains("PEP Index") + li::text'
            ).get().replace('PEP ', ''),
            name=''.join(response.css('h1.page-title *::text').getall()),
            status=response.css(
                'dt:contains("Status") + dd > abbr::text'
            ).get()
        )
