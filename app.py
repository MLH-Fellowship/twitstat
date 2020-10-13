import json
import sys
from datetime import datetime, time
import random

import pandas as pd
from flask import Flask, jsonify, Response

from apps.process_data import ProcessData, Results
from apps.tweets import Twitter
from loguru import logger
from flask import render_template

logger.add(
    "logs/twitstat.log",
    colorize=True,
    format="<green>{time}</green> <level>{message}</level>",
    rotation="50 MB",
    backtrace=True,
    diagnose=True,
)
app = Flask(
    __name__,
    static_url_path="",
    static_folder="./static",
    template_folder="./templates",
)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/analyzetweets", methods=["GET"])
def analyze_tweets():
    twitter = Twitter()
    top_trends = twitter.get_top_trends()
    logger.info(f"Top trends now are {top_trends}")
    trending_tweets = twitter.get_trending_tweets(top_trends[0]["name"])
    df = pd.DataFrame(trending_tweets)
    esp = 1.29
    df, clusters_count = ProcessData().cluster(esp, df)
    res, clusters_count = Results(df).get_result()
    result = {}
    for ind, row in res.iterrows():
        result[ind] = dict(row)
    clusters_count = json.loads(clusters_count.to_json())
    response = dict()
    response["cluserts_count"] = clusters_count
    response["result"] = result
    return jsonify(response)
