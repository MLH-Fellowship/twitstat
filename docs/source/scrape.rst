.. _scrape:

Scraping Module
===============

Twitstat uses Twitter's python API `tweepy <https://github.com/tweepy/tweepy>`_ to get all the tweets for the analysis.
Tweepy is first used to fetch the trending topics around a specified geographical location, these fetched topics are then
fed into the api's search method. The search method gets Twitstat all the tweets (and other important information such as
the likes, retweets, et cetera for each tweet) corresponding to the search query.
