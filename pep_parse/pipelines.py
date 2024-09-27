import csv
import datetime as dt
from collections import defaultdict

from pep_parse.constants import (
    BASE_DIR,
    FILE_DATETIME_FORMAT,
    STATUS_SUMMARY_OUTPUT_FILE,
    RESULTS_DIR
)

PEP_TABLE_COLUMN_HEADERS = ('Статус', 'Количество')
SUCCESS_FILE_CREATED = 'Файл с результатами был сохранён: {file_path}'


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        file_path = results_dir / STATUS_SUMMARY_OUTPUT_FILE.format(
            now_formatted=dt.datetime.now().strftime(FILE_DATETIME_FORMAT)
        )
        with open(file_path, 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, dialect=csv.unix_dialect)
            writer.writerows((
                PEP_TABLE_COLUMN_HEADERS,
                *self.results.items(),
                ('Всего', sum(self.results.values()))
            ))
        spider.logger.info(SUCCESS_FILE_CREATED.format(file_path=file_path))
