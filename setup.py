#!/usr/bin/env python

''' TweetWordCloud package '''

from setuptools import setup, find_packages
from tweetwordcloud import __version__, __author__, __project__

README = 'readme.md'
REQUIREMENTS = [
    'tweepy',
    'scipy',
    'matplotlib',
    'stop-words',
    'wordcloud'
]


def long_description():
    ''' Insert READLE.md into the package '''
    try:
        with open(README) as file:
            return file.read()
    except IOError:
        return 'Failed to read README.md'


setup(
    name=__project__,
    version=__version__,
    description='Twitter Wordcloud library',
    author=__author__,
    author_email='axel.bellec@outlook.fr',
    packages=find_packages(),
    long_description=long_description(),
    install_requires=REQUIREMENTS,
)
