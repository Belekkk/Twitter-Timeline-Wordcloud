
"""
    Twitter worcloud unofficial library
    --------------------------------
"""

__project__ = 'tweetwordcloud'
__author__ = 'Axel Bellec'
__version__ = '0.1.0'


from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from scipy.misc import imread

from stop_words import get_stop_words

import tweepy


def get_my_tweets(keys, nb=100):
    ''' Get your own tweets '''
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    public_tweets = api.user_timeline(count=nb)

    return [tweet.text for tweet in public_tweets]


def get_user_tweets(keys, user, nb=100):
    ''' Get a user's tweets '''
    auth = tweepy.OAuthHandler(keys.CONSUMER_KEY, keys.CONSUMER_SECRET)
    auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    public_tweets = api.user_timeline(id=user, count=nb)

    return [tweet.text for tweet in public_tweets]


def clean_tweets(tweets):
    ''' Cleaning tweets '''
    no_urls_no_tags = " ".join([word for word in tweets.split()
                                if 'http' not in word
                                and '@' not in word
                                and not word.startswith('@')
                                and word != 'RT'])
    return no_urls_no_tags


def get_stopwords(language='english'):
    ''' Andreas Mueller takes a stopwords dict '''
    return {word for word in get_stop_words(language)}


def wordcloud(data, filepath=None, extension='png', mask=None, fontpath=None, stopwords=None, width=1800, height=1400, plot_axis='off', bg_color='white', dpi=300):
    ''' Compute wordcloud '''

    stopwords = stopwords.union(STOPWORDS) if stopwords else STOPWORDS

    twitter_mask = imread(mask, flatten=True) if mask else None

    wordcloud = WordCloud(
        font_path=fontpath,
        stopwords=stopwords,
        background_color=bg_color,
        width=width,
        height=height,
        mask=twitter_mask
    ).generate(data)

    plt.imshow(wordcloud)
    plt.axis(plot_axis)

    if filepath:
        plt.savefig('{filepath}.{filetype}'.format(filepath=filepath, filetype=extension), dpi=dpi)
    plt.show()
