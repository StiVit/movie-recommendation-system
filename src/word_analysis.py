from wordcloud import WordCloud
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt

def sentimental_analysis(text):
    """
    Creates an object of the TextBlob class, the sentiment attribute is used:
    polarity: how positive or negative the sentiment is
    """
    sentiment = TextBlob(str(text)).sentiment
    return sentiment.polarity, sentiment.subjectivity
