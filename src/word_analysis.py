from wordcloud import WordCloud
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt


def generate_word_cloud(df, column):
    df[column] = df[column].fillna('')
    text = "".join(cat for cat in df[column][:100])
    word_cloud = WordCloud(collocations=False, background_color='white').generate(text)
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


def sentimental_analysis(text):
    """
    Creates an object of the TextBlob class, the sentiment attribute is used:
    polarity: how positive or negative the sentiment is
    """
    sentiment = TextBlob(str(text)).sentiment
    return sentiment.polarity, sentiment.subjectivity
