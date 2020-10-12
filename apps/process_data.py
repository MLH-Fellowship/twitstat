import logging

import nltk
from sklearn.cluster import DBSCAN
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob

from apps.clean_data import CleanData

try:
    from nltk import word_tokenize, sent_tokenize
except ImportError:
    nltk.download("punkt")
    from nltk import word_tokenize, sent_tokenize


class ProcessData:
    def __init__(self):
        self.porter_stemmer = nltk.PorterStemmer()
        self.clean_data = CleanData()

    def tokenize(self, tweet):
        """Stem and tokenizes input text, used as custom tokenizer in tfi-df vectorization"""
        tokens = nltk.word_tokenize(tweet)
        stems = []
        for item in tokens:
            stems.append(self.porter_stemmer.stem(item))
        return stems

    def analyse_sentiment(self, tweet):
        """Analyses the sentiment of the given tweet"""
        analysis = TextBlob(tweet)
        sentiment = analysis.sentiment.polarity
        if sentiment > 0:
            return "positive"
        elif sentiment == 0:
            return "neutral"
        else:
            return "negative"

    def cluster(self, esp, df):
        """Clusters data using DBSCAN with a specified esp value"""
        df["tweet_clean"] = df["tweets"].apply(
            lambda y: self.clean_data.remove_punctuation(y)
        )
        df["tweet_clean"] = df["tweet_clean"].apply(
            lambda y: self.clean_data.de_emojify(y)
        )

        vectorizer = TfidfVectorizer(
            tokenizer=self.tokenize, stop_words="english", min_df=1
        )
        x = vectorizer.fit_transform(df.loc[:, "tweet_clean"])

        db = DBSCAN(esp, min_samples=20).fit(x)

        df["clusters"] = db.labels_
        logging.info(f"Number of unique clusters generated: {df.clusters.nunique()}")

        return df, df.clusters.nunique()


class Results:
    def __init__(self, df):
        """Initialize final results of the analysis"""
        self.df = df
        self.clusters_count = df.clusters.value_counts()

    def get_result(self):
        df_results = self.df.groupby(["clusters"]).max().reset_index()
        df_results["sentiment"] = df_results["tweet_clean"].apply(
            lambda y: ProcessData().analyse_sentiment(y)
        )
        return df_results, self.clusters_count
