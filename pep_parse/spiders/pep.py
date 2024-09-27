import scrapy

from pep_parse.items import PepParseItem


NUMERICAL_INDEX_LINK_ERROR = (
    'Ссылка на таблицу всех PEP '
    'по номерам не найдена'
)


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        numerical_index_link = response.xpath(
            '//*[@id="numerical-index"]/h2/following-sibling::p/a/@href'
        ).get()
        if numerical_index_link is not None:
            yield response.follow(
                numerical_index_link,
                callback=self.parse_numerical_index_pep_table
            )
        else:
            self.logger.error(NUMERICAL_INDEX_LINK_ERROR)

    def parse_numerical_index_pep_table(self, response):
        for pep_link in response.xpath(
            '//*[@id="numerical-index"]//table[contains(@class, '
            '"pep-zero-table")]/tbody/tr/td[a][1]/a/@href'
        ).getall():
            yield response.follow(
                pep_link,
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        yield PepParseItem({
            'number': int(response.xpath(
                '//header/ul[@class="breadcrumbs"]/li[a[contains(., '
                '"PEP Index")]]/following-sibling::li/text()'
            ).get().replace('PEP ', '')),
            'name': ''.join(response.xpath(
                '//h1[@class="page-title"]//text()'
            ).getall()),
            'status': response.xpath(
                '//dt[contains(., "Status")]/'
                'following-sibling::dd[1]/abbr/text()'
            ).get()
        })
