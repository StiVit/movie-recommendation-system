import numpy as np
import matplotlib
import pandas as pd
import logging
from utils.logger_setup import setup_logger


movies = pd.read_csv('../dataset/tmdb_5000_movies.csv')
app_logger = setup_logger("app_logger", logging.INFO)

print(movies.info())
