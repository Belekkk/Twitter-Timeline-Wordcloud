import tweetwordcloud as twc
import keys

# Get tweets posted by @OpenBikes_
tweets = ' '.join(twc.get_user_tweets(keys, user='OpenBikes_', nb=1000))

# Clean tweets
cleaned_tweets = twc.clean_tweets(tweets)

# Compute TagCloud
twc.wordcloud(data=cleaned_tweets, stopwords=twc.get_stopwords('french'),
              mask='extras/twitter_mask.png', fontpath='extras/quartzo.ttf')
