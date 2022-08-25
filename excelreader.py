import pandas
import pprint


def read_from_excel(filename):
    excel_data = pandas.read_excel(filename, sheet_name='Лист1', usecols=['Название', 'Сорт', 'Цена', 'Картинка'])

    return excel_data.to_dict(orient='records')


def read_from_excel2(filename):
    excel_data2 = pandas.read_excel(filename, sheet_name='Лист1', na_values=None, keep_default_na=False)
    category = excel_data2.columns.ravel()[0]
    grouped = excel_data2.groupby(by=category, sort=False).apply(lambda x: x.to_dict(orient='records'))
    return grouped.to_dict()
