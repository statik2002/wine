import pandas
import collections


# Первая функция чтения из файла из задания (уже не используем, можно удалить)
def read_from_excel(filename):
    excel_data = pandas.read_excel(filename, sheet_name='Лист1', usecols=['Название', 'Сорт', 'Цена', 'Картинка'])

    return excel_data.to_dict(orient='records')


# Вторая функция чтения из файла из задания (уже не используем, можно удалить)
def read_from_excel2(filename):
    excel_data2 = pandas.read_excel(filename, sheet_name='Лист1', na_values=None, keep_default_na=False)
    category = excel_data2.columns.ravel()[0]
    grouped = excel_data2.groupby(by=category, sort=False).apply(lambda x: x.to_dict(orient='records'))
    return grouped.to_dict()


# Третья функция чтения из файла из задания (рабочая)
def read_from_excel3(filename):
    excel_data = pandas.read_excel(filename, sheet_name='Лист1', na_values=None, keep_default_na=False)
    data_dict = excel_data.to_dict(orient='records')

    # Берем название первой колонки из файла
    category = excel_data.columns.ravel()[0]

    final_default_dict = collections.defaultdict(list)
    for item in data_dict:
        final_default_dict[item[category]].append(item)

    return final_default_dict
