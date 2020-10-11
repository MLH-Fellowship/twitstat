import os
from dotenv import load_dotenv
import tweepy as tw
import re
import string
import nltk
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer

# NLTK variables to aid in cleaning/preprocessing
ps = nltk.PorterStemmer()

# Pandas dataframe for tweets
df = pd.DataFrame(columns=["id", "tweet", "popularity"])


class Results:
    def __init__(self):
        """Initialize final results of the analysis"""
        self.clusters_count = df.clusters.value_counts()
        self.df_results = df.groupby(["clusters"]).max().reset_index()
        print("Number of tweets per cluster: \n{}".format(self.clusters_count))
        print("Top cluster tweets: \n{}".format(self.df_results.to_string()))


def authorise_api():
    """Authorise access to twitter API and return the api handler"""
    load_dotenv()
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_key_secret = os.getenv("CONSUMER_KEY_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tw.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tw.API(auth, wait_on_rate_limit=True)

    return api


def get_top_trends(api):
    """Returns a list of top trends at the specified location"""
    # Current location: New Delhi, India. WOEID = 1 for global trending
    latitude = 28.644800
    longitude = 77.216721

    locations = api.trends_closest(latitude, longitude)
    woeid = locations[0]["woeid"]

    trends = api.trends_place(woeid)
    trends_dict = trends[0]["trends"]

    return [trends_dict[0]]


def de_emojify(text):
    """Remove emoticons from given text"""
    regrex_pattern = re.compile(pattern="["
                                        u"\U0001F600-\U0001F64F"  # emoticons
                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                        u"\U00002500-\U00002BEF"  # chinese char
                                        u"\U00002702-\U000027B0"
                                        u"\U00002702-\U000027B0"
                                        u"\U000024C2-\U0001F251"
                                        u"\U0001f926-\U0001f937"
                                        u"\U00010000-\U0010ffff"
                                        u"\u2640-\u2642"
                                        u"\u2600-\u2B55"
                                        u"\u200d"
                                        u"\u23cf"
                                        u"\u23e9"
                                        u"\u231a"
                                        u"\ufe0f"  # dingbats
                                        u"\u3030"
                                        "]+", flags=re.UNICODE)
    return regrex_pattern.sub(r'', text)


def remove_punctuation(text):
    """Remove links and other punctuation from text"""
    text = text.replace('\n', '')
    text = text.replace('\t', '')
    re.sub(r'http\S+', '', text)    # removes links

    translator = str.maketrans('', '', string.punctuation)
    return text.lower().translate(translator)


def tokenize(text):
    """Stem and tokenizes input text, used as custom tokenizer in tfi-df vectorization"""
    tokens = nltk.word_tokenize(text)
    stems = []
    for item in tokens:
        stems.append(ps.stem(item))
    return stems


def cluster(esp):
    """Clusters data using DBSCAN with a specified esp value"""
    df["tweet_clean"] = df["tweet"].apply(lambda y: remove_punctuation(y))
    df["tweet_clean"] = df["tweet_clean"].apply(lambda y: de_emojify(y))

    vectorizer = TfidfVectorizer(tokenizer=tokenize, stop_words='english', min_df=1)
    x = vectorizer.fit_transform(df.loc[:, "tweet_clean"])

    db = DBSCAN(esp, min_samples=20).fit(x)

    df["clusters"] = db.labels_
    print("Number of unique clusters generated: {}".format(df.clusters.nunique()))


def stream(api, find_word):
    """Steam tweets containing the specified word"""
    query = (
        find_word + " -filter:retweet" + " -filter:media" + " -filter:links"
    )
    i = 0
    limit = 1000
    tweet_count = 100

    for tweet in tw.Cursor(
        api.search, q=query, count=tweet_count, lang="en", result_type="mixed"
    ).items():
        df.loc[i, "id"] = tweet.id
        df.loc[i, "tweet"] = tweet.text
        df.loc[i, "popularity"] = tweet.favorite_count + tweet.retweet_count
        i += 1

        if i > limit:
            break
        else:
            pass


def main():
    api = authorise_api()
    top_trend = get_top_trends(api)
    stream(api, top_trend[0]["name"])

    esp = 1.29
    cluster(esp)

    Results()


if __name__ == "__main__":
    main()
