TwitStat
==========

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style
.. image:: https://img.shields.io/badge/python-3.8.5-blue.svg
     :target: https://www.python.org/downloads/release/python-385/
     :alt: Python 3.8.5
.. image:: https://img.shields.io/github/v/release/MLH-Fellowship/twitstat.svg
     :target: https://github.com/MLH-Fellowship/twitstat/releases/
     :alt: Release
.. image:: https://img.shields.io/github/license/MLH-Fellowship/twitstat.svg?logo=github
     :target: https://github.com/MLH-Fellowship/twitstat/blob/master/LICENSE
     :alt: MIT License
.. image:: https://img.shields.io/github/stars/MLH-Fellowship/twitstat.svg?logo=github
     :target: https://github.com/MLH-Fellowship/twitstat/stargazers
     :alt: GitHub Stars
.. image:: https://img.shields.io/github/forks/MLH-Fellowship/twitstat.svg?logo=github&color=teal
     :target: https://github.com/MLH-Fellowship/twitstat/network/members
     :alt: GitHub Forks


----


:Language: python 3.8.5
:License: MIT
:Pycharm: Yes


Basic Project Structure
-----------------------

Branch
^^^^^^

- ``main`` branch is used for Production
- ``develop`` branch is used for the development or staging
- ``feature_branch`` branch should create PR to ``develop`` branch
- Delete the ``feature_branch`` once merged

Project Board
^^^^^^^^^^^^^^

- ``Frontend`` for the Frontend part of the Application
- ``Backend`` for the backend part of the application
- ``Bugs`` for reporting all the bugs, found on the application

Setup
-------
.. image:: https://img.shields.io/github/languages/code-size/MLH-Fellowship/twitstat?logo=github
     :target: https://github.com/MLH-Fellowship/twitstat/
     :alt: Code Size
.. image:: https://img.shields.io/github/commit-activity/m/MLH-Fellowship/twitstat?color=bluevoilet&logo=github
     :target: https://github.com/MLH-Fellowship/twitstat/commits/
     :alt: Commit Activity
.. image:: https://img.shields.io/github/repo-size/MLH-Fellowship/twitstat?logo=github
     :target: https://github.com/MLH-Fellowship/twitstat/
     :alt: Repo Size

* Setting up your project and environment

.. code-block:: bash

    # Clone the repository
    git clone git@github.com:MLH-Fellowship/twitstat.git
    cd twitstat

    # Create Virtual Environment
    python -m venv venv
    source venv/bin/activate

    # Install dependencies
    python -m pip install -r requirements/local.txt

* Working in Development Mode

.. code-block:: bash

    # We use develop branch for development
    git checkout -b develop remotes/origin/develop
    git checkout -b "your_feature_branch"

* If your terminal doesn't load ``.env`` file automatically

.. code-block:: bash

    export $(grep -v '^#' .env | xargs)

