import logging
import os
import matplotlib.pyplot as plt
from utils.logger_setup import setup_logger

def structure_output(df):
    output_logger = setup_logger("output_logger", logging.INFO)
    if os.path.isfile('dataset/data_frame_analysis'):
        output_logger.info("File with data analyse exists")
    else:
        with open('dataset/data_frame_analysis', 'w') as output:
            output.write(f"Movies DF:\n\n{df.head()}\n")
            output.write("\n\nMovies DF:\n")
            output.write(f"{df.info()}\n\n")
            output.write(f"{df.describe()}\n\n")
            output.write(f"{df['original_language'].value_counts()}")
            output.write(f"\n{df['status'].value_counts()}")
            output.write(f"\n\nDuplicates:\n\n{df.duplicated().sum()}")
            output.write(f"\n\nNulls:\n\n{df.isnull().sum()}\n\n**************************************\n\n")
            df.hist(figsize=(20, 12), bins=100)
            plt.show()
        output_logger.info("Data analysed successfully")