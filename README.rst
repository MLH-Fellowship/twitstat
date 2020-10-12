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
.. image:: https://readthedocs.org/projects/twitstat/badge/?version=latest
    :target: https://twitstat.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://img.shields.io/github/license/MLH-Fellowship/twitstat.svg?logo=github
     :target: https://github.com/MLH-Fellowship/twitstat/blob/main/LICENSE
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

Twitstat is a simple web application that analyses twitter data to provide interesting insights into trending hashtags
and topics. It cleverly clusters and charts data to ease the process of better understanding trends around the world!

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

* Running locally

.. code-block:: bash

    flask run


Issues
--------

.. image:: https://img.shields.io/github/issues/MLH-Fellowship/twitstat?logo=github
     :target: https://github.com/MLH-Fellowship/twitstat/issues
     :alt: GitHub issues
.. image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat&logo=git&logoColor=white
     :target: https://github.com/MLH-Fellowship/twitstat/pulls
     :alt: PRs Welcome
.. image:: https://img.shields.io/github/last-commit/MLH-Fellowship/twitstat?logo=github
     :target: https://github.com/MLH-Fellowship/twitstat/
     :alt: GitHub last commit

.. class:: bold

    `Track Issues <https://github.com/MLH-Fellowship/twitstat/issues>`__ on GitHub

.. class:: bold

    Feel free to `open new issue(s) <https://github.com/MLH-Fellowship/twitstat/issues/new/choose>`__ . Make sure you follow the Issue Template provided.


Contribution Guidelines
------------------------

.. image:: https://img.shields.io/github/issues-pr-raw/MLH-Fellowship/twitstat?logo=git&logoColor=white
     :target: https://github.com/MLH-Fellowship/twitstat/compare
     :alt: GitHub pull requests
.. image:: https://img.shields.io/github/contributors/MLH-Fellowship/twitstat?logo=github
     :target: https://github.com/MLH-Fellowship/twitstat/graphs/contributors
     :alt: GitHub contributors

.. class:: bold

    Refer `CONTRIBUTING.rst <https://github.com/MLH-Fellowship/twitstat/blob/main/CONTRIBUTING.rst>`__ for detailed information on Contributing to TwitStat.


* Write clear meaningful git commit messages (Do read `How to Write a Git Commit Message <https://chris.beams.io/posts/git-commit/>`__).
* Make sure your PR's description contains GitHub's special keyword references that automatically close the related issue when the PR is merged. (Check out `Closing Issues via Pull Requests <https://github.com/blog/1506-closing-issues-via-pull-requests>`__ for more info)
* When you make very very minor changes to a PR of yours (like for example fixing a text in button, minor changes requested by reviewers) make sure you squash your commits afterward so that you don't have an absurd number of commits for a very small fix. (Learn how to squash at `Squash Commits with Git <https://davidwalsh.name/squash-commits-git>`__)
* When you're submitting a PR for a UI-related issue, it would be really awesome if you add a screenshot of your change or a link to a deployment where it can be tested out along with your PR. It makes it very easy for the reviewers and you'll also get reviews quicker.
* Please follow the `PR Template <https://github.com/MLH-Fellowship/twitstat/blob/main/.github/PULL_REQUEST_TEMPLATE.md>`__ to create the PR.
* Always open PR to ``develop`` branch.

* Please read our `Code of Conduct <./CODE_OF_CONDUCT.md>`__.

Contributors
-------------

Made with :heart: by `Aditya Raman <https://github.com/ramanaditya>`_ and `Garima Singh <https://github.com/grimmmyshini>`_!


License
--------

TwitStat is `MIT licensed <https://github.com/MLH-Fellowship/twitstat/blob/main/LICENSE>`__.
