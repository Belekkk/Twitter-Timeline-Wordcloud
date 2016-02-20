import tweepy
import keys
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from scipy.misc import imread
from stop_words import get_stop_words


def get_my_tweets(keys, nb=100):
    ''' Get your own tweets '''
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)
    public_tweets = api.user_timeline(count=nb)
    return [tweet.text for tweet in public_tweets]


def get_user_tweets(keys, user, nb=100):
    ''' Get a user's tweets '''
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)
    api = tweepy.API(auth)
    public_tweets = api.user_timeline(id=user, count=nb)
    print([tweet.text for tweet in public_tweets])
    return [tweet.text for tweet in public_tweets]


def clean_tweets(tweets):
    ''' Cleaning tweets '''
    no_urls_no_tags = " ".join([word for word in tweets.split()
                                if 'http' not in word
                                and '@' not in word
                                and not word.startswith('@')
                                and word != 'RT'])
    return no_urls_no_tags

# Wordcloud by Andreas Mueller takes a stopwords dict
stop_words = {word for word in get_stop_words('french')}


def wordcloud(data, user, mask='extras/twitter_mask.png', stopwords=stop_words, save=True):
    ''' Compute wordcloud '''
    twitter_mask = imread(mask, flatten=True)

    more_stopwords = STOPWORDS  # English stopwords
    stopwords = stopwords.union(more_stopwords)

    wordcloud = WordCloud(
        font_path='extras/quartzo.ttf',
        stopwords=stopwords,
        background_color='white',
        width=1800,
        height=1400,
        mask=twitter_mask
    ).generate(data)

    plt.imshow(wordcloud)
    plt.axis('off')

    if save:
        plt.savefig('example/wordcloud_{0}.png'.format(user), dpi=300)
    plt.show()


tweets = ' '.join(get_user_tweets(keys, user='OpenBikes_', nb=1000))
cleaned_tweets = clean_tweets(tweets)
wordcloud(data=cleaned_tweets, user='OpenBikes_', stopwords=stop_words)
