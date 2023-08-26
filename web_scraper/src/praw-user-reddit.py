import praw
import time

# Autenticação na API do Reddit
reddit = praw.Reddit(client_id='DzLrEIjbuDKTEirqtk3uHw',
                     client_secret='5PK8_DzWN4RtuUlTVTxpONZWCtFXSw',
                     username='taw-balbino',
                     password='!!3uSKPvumU9Kst',
                     user_agent='webcrowler')


for submission in reddit.redditor("derimat").submissions.controversial(time_filter='all'):
    print(submission.selftext)