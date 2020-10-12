import sys

import pandas as pd
from flask import Flask, jsonify

from apps.process_data import ProcessData, Results
from apps.tweets import Twitter
from loguru import logger

logger.add(
    "logs/twitstat.log",
    colorize=True,
    format="<green>{time}</green> <level>{message}</level>",
    rotation="50 MB",
    backtrace=True,
    diagnose=True,
)
app = Flask(__name__)


@app.route("/", methods=["GET"])
def analyze_tweets():
    logger.info("Analyze tweets initiated")
    twitter = Twitter()
    top_trends = twitter.get_top_trends()
    logger.info(f"Top trends now are {top_trends}")
    trending_tweets = twitter.get_trending_tweets(top_trends[0]["name"])
    df = pd.DataFrame(trending_tweets)
    esp = 1.29
    df, clusters_count = ProcessData().cluster(esp, df)
    res, clusters_count = Results(df).get_result()
    logger.info(f"Clusters: {clusters_count}")
    result = {}
    for ind, row in res.iterrows():
        result[ind] = dict(row)
    response = dict()
    response["cluserts_count"] = clusters_count.to_json()
    response["result"] = result
    return jsonify(response)
