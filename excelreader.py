import pandas
import pprint
import collections


def read_from_excel(filename):
    excel_data = pandas.read_excel(filename, sheet_name='Лист1', usecols=['Название', 'Сорт', 'Цена', 'Картинка'])

    return excel_data.to_dict(orient='records')


def read_from_excel2(filename):
    excel_data2 = pandas.read_excel(filename, sheet_name='Лист1', na_values=None, keep_default_na=False)
    category = excel_data2.columns.ravel()[0]
    grouped = excel_data2.groupby(by=category, sort=False).apply(lambda x: x.to_dict(orient='records'))
    return grouped.to_dict()


def read_from_excel3(filename):
    excel_data2 = pandas.read_excel(filename, sheet_name='Лист1', na_values=None, keep_default_na=False)
    perm = excel_data2.to_dict(orient='records')
    ex = collections.defaultdict(list)
    for item in perm:
        ex[item['Категория']].append(item)
    return ex
