.. _nlp:

Analysis Module
===============

Twitsat uses three major modules to facilitate its data analysis

- Preprocessing module
- Clustering module
- Sentiment analysis module


Preprocessing Module
--------------------

Before data can be loaded into any of the *actual* analyser functions, it has to be preprocessed or *cleaned*. The preprocessing module removes any unwanted text such as emoticons,
line breaks, punctuations et cetera, from the tweets. Certain words *(called stop-words)* are also removed as they do not add meaning to the text. At last, all the words are tokenized
*(split into multiple words)* and *stemmed*. These tasks are done with the help of `nltk's <https://github.com/nltk/nltk>`_ algorithms.


Clustering Module
-----------------

Twitstat's clustering module uses `scikit-learn's <https://github.com/scikit-learn/scikit-learn>`_ `DBSCAN <https://scikit-learn.org/stable/modules/clustering.html#dbscan>`_
clustering algorithm to cluster tweets falling under the trending categories. **Density-based spatial clustering of applications with noise** *(DBSCAN)* is a density-based
clustering algorithm, that is, given a set of points in some space, it groups together points that are closely packed together. Points which are sparsely packed are classified
as outliers.


Sentiment Analysis Module
-------------------------

At last, after splitting tweets into clusters, the most popular tweet of each cluster is identified. These *popular* tweets are then fed into `texblob's <https://github.com/sloria/TextBlob>`_
sentiment analysis module where the tone (positive, negative or neutral) of the tweets is decided.

