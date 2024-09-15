import numpy as np
import pandas as pd
import logging
import re
from matplotlib import pyplot as plt
from src.word_analysis import generate_word_cloud, sentimental_analysis

from utils.logger_setup import setup_logger
import os

patternname = r"(?:.name.: .)(\w{1,}\s{0,}\w{0,})"
patternlang = r"(?:.iso_639_1.: .)(\w{1,}\s{0,}\w{0,})"


def dict2list(x):
    """
    Input: It expects x, a string that resembles a list of dictionaries.
    Extract important info out the string columns that contain of lists of dictionaries
    """
    if type(x) is str:
        templist = x.strip('[]').split(',')
        namelist = []
        lang = False
        for element in templist:
            if re.search(patternlang, element):
                namelist.append(re.search(patternlang, element).group(0)[14:])
                lang = True
            elif re.search(patternname, element) and not lang:
                namelist.append(re.search(patternname, element).group(0)[9:])
        if len(namelist) > 0:
            return {k: 1 for k in namelist}
        else:
            return x
    else:
        return x


def dict2dummy(df, columns):
    """
    Input:
        df: A pandas DataFrame.
        columns: A list of column names in the DataFrame that contain dictionaries or dictionary-like data
    Converts DataFrame columns containing dictionary-like data into one-hot encoded dummy variables for further analysis.
    """
    columnnames = {}
    for col in columns:
        columnnames[col] = list(df[col].apply(pd.Series).drop([0], axis=1))
        df = pd.concat([df.drop([col], axis=1), df[col].apply(pd.Series).fillna(0).drop([0], axis=1)], axis=1)
        return df, columnnames


def process_data():
    df_movies = pd.read_csv('dataset/tmdb_5000_movies.csv')
    app_logger = setup_logger("app_logger", logging.INFO)
    pd.set_option('display.max_columns', None)
    # Get some more info about the data I'm working with
    if os.path.isfile('dataset/data_frame_analysis'):
        app_logger.info("File with data analyse exists")
    else:
        with open('dataset/data_frame_analysis', 'w') as output:
            output.write(f"Movies DF:\n\n{df_movies.head()}\n")
            output.write("\n\nMovies DF:\n")
            output.write(f"{df_movies.info()}\n\n")
            output.write(f"{df_movies.describe()}\n\n")
            output.write(f"{df_movies['original_language'].value_counts()}")
            output.write(f"\n{df_movies['status'].value_counts()}")
            output.write(f"\n\nDuplicates:\n\n{df_movies.duplicated().sum()}")
            output.write(f"\n\nNulls:\n\n{df_movies.isnull().sum()}\n\n**************************************\n\n")
            df_movies.hist(figsize=(20, 12), bins=100)
            plt.show()
        app_logger.info("Data analysed successfully")

    # generate_word_cloud(df_movies, 'overview')
    df_movies["Polarity"] = zip(*df_movies['overview'].apply(sentimental_analysis))
    app_logger.info("Text sentiment successfully measured successfully")
    df_movies = df_movies.map(dict2list)
    dummy_features = ['genres']
    df_movies, columndictionary = dict2dummy(df_movies, dummy_features)
