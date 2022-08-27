import pandas
import collections


def read_products(filepath):
    data_frame = pandas.read_excel(filepath, sheet_name='Лист1', na_values=None, keep_default_na=False)
    products = data_frame.to_dict(orient='records')

    # Берем название первой колонки из файла
    category = data_frame.columns.ravel()[0]

    product_collection = collections.defaultdict(list)
    for product in products:
        product_collection[product[category]].append(product)

    return product_collection
