import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from typing import Tuple, List

class seaborn_plotter:
    """
    This object's purpose is to create plots with preset formats
    """

    def __init__(self):
        """
        Initializes plotter
        """
        self.show_plot = True

    def histogram(self, data:pd, x_col:str, bins:int, title:str=None, xlabel:str=None, ylabel:str=None, hue:str=None, figsize:Tuple = (10, 6), savefig_filepath:str=None):
        """
            This function generates a Histogram via Seaborn

        :param data: pandas dataframe of data
        :param x_col: x axis column name
        :param bins: Generic bin parameter that can be the name of a reference rule, the number of bins, or the breaks of the bins.
        :param title: title name
        :param xlabel: x-label name
        :param ylabel: y-label name
        :param hue: hue for plotting
        :param figsize: figure size
        :param savefig_filepath: string of filepath to save plot
        :return: plot object
        """
        # set figure size
        plt.figure(figsize=figsize)

        # Generate Histogram
        sns.histplot(data=data, x=x_col, bins=bins, hue=hue)

        # set title and labels
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)

        # save figure
        if savefig_filepath:
            plt.savefig(savefig_filepath, bbox_inches = 'tight')

        # show plot
        if self.show_plot:
            plt.show()
        else:
            plt.close()

        return plt

    def barplot(self, data:pd, x_col:str, y_col:str, hue:str=None, title:str=None, xlabel:str=None, ylabel:str=None, figsize:Tuple = (10,6), savefig_filepath:str=None, order_col:List[str]=None):
        """
            This function generates a bar plot via Seaborn

        :param data: pandas data frame
        :param x_col: x column to plot
        :param y_col: y column to plot
        :param hue: hue group
        :param title: plot title
        :param xlabel: x-axis label
        :param ylabel: y-axis label
        :param figsize: figure size
        :param savefig_filepath: string of filepath to save plot
        :param order_col: optional list of columns to order the x axis bars
        :return: return a plt object
        """

        # set figure size
        plt.figure(figsize=figsize)

        # generate bar plot
        if order_col:
            sns.barplot(data=data, x=x_col, y=y_col, hue=hue, order=order_col)
        else:
            sns.barplot(data=data, x=x_col, y=y_col, hue=hue)

        # set title and labels
        if title:
            plt.title(title)
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)

        # rotation x ticks
        plt.xticks(rotation=90)

        # Turn on grid
        plt.grid()

        # save figure
        if savefig_filepath:
            plt.savefig(savefig_filepath, bbox_inches = 'tight')

        # show plot
        if self.show_plot:
            plt.show()
        else:
            plt.close()

        return plt

    def show_plot_off(self)->None:
        """
            Function to turn off showing plot
        :return:
        """
        self.show_plot = False

    def show_plot_on(self)->None:
        """
            Function to turn on showing plot
        :return:
        """
        self.show_plot = True