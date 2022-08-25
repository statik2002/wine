import datetime
import pprint
import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

from excelreader import read_from_excel, read_from_excel2, read_from_excel3

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

# Функцию read_from_excel3 импортировали из excelreader.py
wine_data = read_from_excel3('wine3.xlsx')


# Выводим правильное значение лет\год\года в зависимости от значения года
def years(year):
    if 11 <= year % 100 <= 19:
        return "лет"
    elif year % 10 == 1:
        return "год"
    elif 1 < year % 10 < 5:
        return "года"
    else:
        return "лет"


foundation_year = 1922
current_year = datetime.datetime.now().year
year_delta = current_year - foundation_year
year_word = years(year_delta)

rendered_page = template.render(
    year=year_delta,
    year_word=year_word,
    wine_data=wine_data,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
