import numpy as np
import pandas as pd
import logging
import re
import seaborn as sns
from matplotlib import pyplot as plt

from utils.logger_setup import setup_logger
import os

patternname = r"(?:.name.: .)(\w{1,}\s{0,}\w{0,})"
patternlang = r"(?:.iso_639_1.: .)(\w{1,}\s{0,}\w{0,})"

def dict2list(x):
    """
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
            elif re.search(patternname, element):
                namelist.append(re.search(patternname, element).group(0)[9:])
        if len(namelist) > 0:
            return {k: 1 for k in namelist}
        else:
            return x
    else:
        return x


def process_data():
    df_movies = pd.read_csv('dataset/tmdb_5000_movies.csv')
    app_logger = setup_logger("app_logger", logging.INFO)

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

    df_movies = df_movies.applymap(dict2list)