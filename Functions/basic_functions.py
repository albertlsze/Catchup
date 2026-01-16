import os
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#from sklearn.preprocessing import MultiLabelBinarizer
from pandas.plotting import scatter_matrix
from typing import List, Dict

def feature_scatter_matrix(data: pd, attributes: List[str], savefig_filepath: str = None) -> None:
    """
        Create scatter matrix to quickly look at relationship between different parameters

    :param data: pandas datagrame
    :param attributes: attributes you want to plot against
    :param savefig_filepath: file path to save figure
    :return: None
    """
    # generate scatter matrix
    axes = scatter_matrix(data.filter(attributes), figsize=(20, 20))

    # rotate x and y labels
    for ax in axes.flatten():
        ax.xaxis.label.set_rotation(90)
        ax.yaxis.label.set_rotation(0)
        ax.yaxis.label.set_ha('right')

    # save figure
    if savefig_filepath:
        plt.savefig(savefig_filepath, bbox_inches='tight')

    # show plot
    plt.show()

    return None

def load_pickle(filename:str):
    """
        This function takes a pickle filepath and opens the object
    :param filename: string of filepath
    :return: data object
    """
    with open(filename, 'rb') as f:
        object = pickle.load(f)

    return object

def min_max_norm(data_pd: pd, col_names: List[str]) -> pd:
    """
        This function performs a min and max normalization process

    :param data_pd: dataframe of data
    :param col_names: columns that need to be normalized
    :return: update data frame with normalized data
    """
    # copy the data
    data_min_max_scaled = data_pd.copy()

    # apply normalization techniques
    for col_name in col_names:
        data_min_max_scaled[col_name] = (data_min_max_scaled[col_name] - data_min_max_scaled[col_name].min()) / (data_min_max_scaled[col_name].max() - data_min_max_scaled[col_name].min())

    return data_min_max_scaled
'''
def one_hot_encoder_col(data_pd:pd, transform_col:str)->pd:
    """
        This function on-hot encodes a given column, provided the column is a string based seperated by ,
        ex. 'Spa, pool, cabana'

    :param data_pd: dataframe of data
    :param transform_col: column to one-hot-encode
    :return: updated dataframe
    """
    # takes column with string and converts them to a list
    data_pd[transform_col] = data_pd[transform_col].apply(lambda x: ",".join(s.strip() for s in x.split(",")))

    # use MultiLabelBinarizer to create a one-hot encoded dataframe of the amenities
    mlb = MultiLabelBinarizer()
    product_pd = pd.DataFrame(mlb.fit_transform(data_pd[transform_col].str.split(',')),
                              columns=mlb.classes_,
                              index=data_pd.index)

    # create a new dataframe with the id_col and amenities
    new_df = pd.concat([data_pd, product_pd], axis=1)
    return new_df'''

def save_pickle(object, filename: str)->None:
    """
        This function takes an object and saves it as a pickle file in the filename format

    :param object: some type of data object
    :param filename: string of filepath
    :return: No return
    """
    with open(filename, 'wb') as f:
        pickle.dump(object, f)

    return None