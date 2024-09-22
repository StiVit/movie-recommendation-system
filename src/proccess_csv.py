import numpy as np
import pandas as pd
import logging
import re
from src.word_analysis import sentimental_analysis
from utils.logger_setup import setup_logger
from src.feature_extraction import extract_features

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
    data_processing_logger = setup_logger("data_processing_logger", logging.INFO)
    pd.set_option('display.max_columns', None)

    df_movies["polarity"], df_movies["subjectivity"] = zip(*df_movies['overview'].apply(sentimental_analysis))
    data_processing_logger.info("Text sentiment measured successfully")

    df_movies['overview'] = df_movies['overview'].fillna("")
    df_movies[['time', 'location', 'plot_keywords']] = df_movies['overview'].apply(lambda x: pd.Series(extract_features(x)))
    data_processing_logger.info("Features successfully extracted")
    print(df_movies.head())

    df_movies = df_movies.map(dict2list)
    dummy_features = ['genres']
    df_movies, columndictionary = dict2dummy(df_movies, dummy_features)
    return df_movies, columndictionary