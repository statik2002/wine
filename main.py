import datetime
import argparse

from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

from excelreader import read_products


# Выводим правильное значение лет\год\года в зависимости от значения года
def get_word_year(year):
    if 11 <= year % 100 <= 19:
        return "лет"
    elif year % 10 == 1:
        return "год"
    elif 1 < year % 10 < 5:
        return "года"
    else:
        return "лет"


def main():

    parser = argparse.ArgumentParser(description='Сайт магазина авторского вина "Новое русское вино"')
    parser.add_argument('-f', '--filepath', help='Путь к файлу xlsx с винами', default='wine.xlsx')
    parser.add_argument('-t', '--templatepath', help='Путь к файлу шаблона', default='template.html')
    args = vars(parser.parse_args())

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template(args['templatepath'])

    products = read_products(args['filepath'])

    foundation_year = 1922
    current_year = datetime.datetime.now().year
    year_delta = current_year - foundation_year
    year_word = get_word_year(year_delta)

    rendered_page = template.render(
        year=year_delta,
        year_word=year_word,
        products=products,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
