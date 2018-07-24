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


if __name__ == '__main__':
    # load data into data frames
    data_frames = load_data()
    if len(data_frames) == 0:
        print('Download instacart market analysis data-set using the link: '
              'https://www.instacart.com/datasets/grocery-shopping-2017')
        exit(0)

