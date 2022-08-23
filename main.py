import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


def years_suffix(year):
    if year % 10 == 1:
        return 'год'
    elif year % 10 >= 2 & year % 10 <= 4:
        return 'года'
    elif year % 100 >= 11 & year % 100 <= 14:
        return 'лет'
    else:
        return 'лет'


foundation_year = 1922
current_year = datetime.datetime.now().year
year_delta = current_year-foundation_year
year_word = years_suffix(year_delta)

rendered_page = template.render(
    year=year_delta,
    year_word=year_word,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()



