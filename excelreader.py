import pandas


def read_from_excel(filename):
    excel_data = pandas.read_excel(filename, sheet_name='Лист1', usecols=['Название', 'Сорт', 'Цена', 'Картинка'])

    return excel_data.to_dict(orient='records')

