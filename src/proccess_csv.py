import numpy as np
import matplotlib
import pandas as pd
import logging
import seaborn as sns
from utils.logger_setup import setup_logger
import os


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
        app_logger.info("Data analysed successfully")
