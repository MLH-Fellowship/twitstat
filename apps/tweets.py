import os

import tweepy


class Twitter:
    def __init__(self):

        # Authorization
        self.TWITTER_CONSUMER_API_KEY = os.getenv("TWITTER_CONSUMER_API_KEY")
        self.TWITTER_CONSUMER_SECRET_KEY = os.getenv("TWITTER_CONSUMER_SECRET_KEY")
        self.TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
        self.TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

        auth = tweepy.OAuthHandler(
            self.TWITTER_CONSUMER_API_KEY, self.TWITTER_CONSUMER_SECRET_KEY
        )
        auth.set_access_token(
            self.TWITTER_ACCESS_TOKEN, self.TWITTER_ACCESS_TOKEN_SECRET
        )

        self.TWITTER_API = tweepy.API(auth, wait_on_rate_limit=True)

    def get_top_trends(self) -> list:
        """Returns a list of top trends at the specified location"""
        # WOEID = 1 for global trending
        latitude = os.getenv("LATITUDE")
        longitude = os.getenv("LONGITUDE")

        locations = self.TWITTER_API.trends_closest(latitude, longitude)
        woeid = locations[0]["woeid"]

        trends = self.TWITTER_API.trends_place(woeid)
        trends_dict = trends[0]["trends"]

        return [trends_dict[0]]

    def get_trending_tweets(self, find_word):
        query = find_word + " -filter:retweet" + " -filter:media" + " -filter:links"
        tweet_count_limit = 1000
        tweet_counter = 0
        tweets_list = list()

        while tweet_counter < tweet_count_limit:
            for tweet in tweepy.Cursor(
                self.TWITTER_API.search,
                q=query,
                count=tweet_count_limit,
                lang="en",
                result_type="mixed",
            ).items():
                tweets = dict()
                tweets["id"] = tweet.id
                tweets["tweets"] = tweet.text
                tweets["interactions"] = tweet.favorite_count + tweet.retweet_count

                tweets_list.append(tweets)

                tweet_counter += 1
                if tweet_counter > 1000:
                    break

        return tweets_list


if __name__ == "__main__":
    api = Twitter()
    top_trends = api.get_top_trends()
    print(top_trends)
    trending_tweets = api.get_trending_tweets(top_trends[0]["name"])
    print(trending_tweets)
