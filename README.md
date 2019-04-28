# reddit-scrubber
Simple tool to scrub reddit account before deactivation

This code runs on python 3.

1a) Run to set environment: 

    $ virtualenv --no-site-packages .env && source .env/bin/activate && pip install -r requirements.txt

1b) Or simply install PRAW v4 if you don't use virtualenvs:

    $ pip install praw

2) Go to https://www.reddit.com/prefs/apps and click on create another app and the bottom of the page. You can write basically anything here, just make sure to select `script`. Once created you get your Client-ID and Client-Secret.

3) Rename `config.py.example` to `config.py` and enter the relevant information replacing `example` data.

4) Finally just run

    $ python reddit-scrubber.py
