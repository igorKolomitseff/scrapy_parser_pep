import csv
import datetime as dt
import logging
from collections import defaultdict

from pep_parse.settings import (
    BASE_DIR,
    FILE_DATETIME_FORMAT,
    STATUS_SUMMARY_OUTPUT_FILE,
    RESULTS_DIR
)

PEP_TABLE_COLUMN_HEADERS = ('Статус', 'Количество')
PEP_TABLE_FOOTER = 'Всего {total}'

RESULTS_DIR_CREATED = 'Создана папка для результатов: {results_dir}'
SUCCESS_FILE_CREATED = 'Файл с результатами был сохранён: {file_path}'


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        if not self.results_dir.exists():
            self.results_dir.mkdir()
            logging.info(
                RESULTS_DIR_CREATED.format(results_dir=self.results_dir)
            )

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        self.results[item['status']] += 1
        return item

    def close_spider(self, spider):
        file_path = self.results_dir / STATUS_SUMMARY_OUTPUT_FILE.format(
            now_formatted=dt.datetime.now().strftime(FILE_DATETIME_FORMAT)
        )
        with open(file_path, 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(
                csv_file,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            )
            writer.writerows((
                PEP_TABLE_COLUMN_HEADERS,
                *self.results.items(),
                PEP_TABLE_FOOTER.format(
                    total=sum(self.results.values())
                ).split()
            ))
        logging.info(SUCCESS_FILE_CREATED.format(file_path=file_path))
