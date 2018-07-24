""" Exploratory data analysis EDA on insta-cart data-set.
"""
import pandas as pd
from pathlib import Path


def load_data():
    """ Loads the data.

    :return: dictionary of DataFrames with file names as keys.
    """
    data_in_dict = dict()
    data_path = Path.cwd().parent.joinpath('data')
    for file in list(sorted(data_path.rglob('*.csv'))):
        data_in_dict[file.stem] = pd.read_csv(file)
    return data_in_dict


def n_products(data_frame, n=10, view_type='head'):
    """ Finds the top or bottom n products in orders/sales.

    :param data_frame: DataFrame containing order_products data.
    :param n: number of products
    :param view_type: Defines the type either head or tail.
    :return: DataFrame of top or bottom n products
    """
    grouped = data_frame.groupby('product_id')
    count = grouped.size().reset_index(name='order_id_count')
    sort_count = count.sort_values(by='order_id_count', ascending=False)
    if view_type is 'head':
        return sort_count.head(n)
    elif view_type is 'tail':
        return sort_count.tail(n)
    else:
        print('view_type can either be head or tail.')


if __name__ == '__main__':
    # load data into data frames
    data_frames = load_data()
    if len(data_frames) == 0:
        print('Download instacart market analysis data-set using the link: '
              'https://www.instacart.com/datasets/grocery-shopping-2017')
        exit(0)

    # data frames
    order_products = data_frames['order_products_train']
    orders = data_frames['orders']

    # find top n best selling products
    top_n_products = n_products(order_products.iloc[:, :], view_type='head')
