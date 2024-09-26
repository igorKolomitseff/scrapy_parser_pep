# Проект асинхронного парсера документации PEP

## Функции проекта

* Собирает информацию о документах PEP: номер документа, его название и статус
* Анализирует статусы документов PEP: подсчитывает количественно документы PEP 
по их статусам.

## Стек технологий
* [Python](https://www.python.org/)
* [Scrapy](https://scrapy.org/)

## Как развернуть проект
1. Клонируйте репозиторий и перейдите в директорию scrapy_parser_pep
```bash
git git@github.com:igorKolomitseff/scrapy_parser_pep.git
cd scrapy_parser_pep
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python3 -m venv venv
source venv/bin/activate  # Для Linux и macOS
source venv/Scripts/activate  # Для Windows
```
3. Обновите pip и установите зависимости проекта:
```bash
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Выполните команду:
```bash
scrapy crawl pep
```

Результаты работы будут доступны в директории 
[results](https://github.com/igorKolomitseff/scrapy_parser_pep/tree/main/results) 
в файлах формата CSV.


### Автор

[Игорь Коломыцев](https://github.com/igorKolomitseff)