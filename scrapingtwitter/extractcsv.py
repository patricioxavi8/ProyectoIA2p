import tweepy
import csv
import unicodedata
consumer_key = 'YpYcmiKHtGxOXheTDW4HIc3zc'
consumer_secret = 'Pb7whiggvDJnISGwTEugSJP4Pn6CCUbei0fObTtlfhHyxfQ2zU'
access_token = '738112788942495745-QQnjiJfb54za9XVICrLRLyMjRYZbiD2'
access_token_secret = 'TwNe0LYo0c5P1S7jDI6lhULX2UMBPAVtV97uwPDYkIZXH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('muestra.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#COENacional",count=100,
                           lang="es",
                           since="2020-07-20").items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])