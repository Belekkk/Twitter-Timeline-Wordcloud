# Twitter Timeline Wordcloud - `Python`

Simple way to get tweets and visualizing them into a wordcloud.

![openbikes_wordcloud](http://i.imgur.com/ORSROdA.png)

## Setup

### Installation

```sh
pip install git+git//github.com/axelbellec/twitter-timeline-wordcloud.git
```

### Run locally

Install requirements :
```sh
python setup.py install
```

## Add credentials

You have to create a `keys.py` file containing Twitter API credentials :
```python
CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')
```

## Usage

Just follow these 3 steps :
	- Getting tweets
	- Cleaning them
	- Enjoying!
```python
import tweetwordcloud as twc
import keys

# Get tweets posted by @OpenBikes_
tweets = ' '.join(twc.get_user_tweets(keys, user='OpenBikes_', nb=1000))

# Clean tweets
cleaned_tweets = twc.clean_tweets(tweets)

# Compute TagCloud
twc.wordcloud(data=cleaned_tweets, stopwords=twc.get_stopwords('french'),
              mask='extras/twitter_mask.png', fontpath='extras/quartzo.ttf')

```
