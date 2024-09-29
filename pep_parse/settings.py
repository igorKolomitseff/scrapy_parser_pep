from pathlib import Path

BOT_NAME = 'pep_parse'
NEWSPIDER_MODULE = 'pep_parse.spiders'
SPIDER_MODULES = [NEWSPIDER_MODULE]
ROBOTSTXT_OBEY = True

PEP_DOMAIN = 'peps.python.org'

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'
PEP_OUTPUT_FILE = 'pep_%(time)s.csv'
STATUS_SUMMARY_OUTPUT_FILE = 'status_summary_{now_formatted}.csv'

FILE_DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

FEEDS = {
    f'{RESULTS_DIR}/{PEP_OUTPUT_FILE}': {
        'format': 'csv',
        'fields': ['number', 'name', 'status']
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
