from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'
STATUS_SUMMARY_OUTPUT_FILE = 'status_summary_{now_formatted}.csv'

FILE_DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'