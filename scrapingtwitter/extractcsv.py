import tweepy
import csv
import re
import os
import os.path

consumer_key = 'YpYcmiKHtGxOXheTDW4HIc3zc'
consumer_secret = 'Pb7whiggvDJnISGwTEugSJP4Pn6CCUbei0fObTtlfhHyxfQ2zU'
access_token = '738112788942495745-QQnjiJfb54za9XVICrLRLyMjRYZbiD2'
access_token_secret = 'TwNe0LYo0c5P1S7jDI6lhULX2UMBPAVtV97uwPDYkIZXH'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



def tweets_search():
    palabra = input("Palabra a buscar: ")
    numero_de_Tweets = int(input(u"Número de tweets a capturar: "))

    return tweepy.Cursor(api.search, palabra + " -filter:retweets", lang="es",tweet_mode="extended").items(numero_de_Tweets)


## formatting csv text

a, b = 'áéíóúü', 'aeiouu'
trans = str.maketrans(a, b)


def remove_url(str):
    return re.sub(r"http\S+", "", str)


def removeSign(str):
    return re.sub(r"\?|(\¿)|(…)|(RT)|(\"\")|(\")|(\.)|(«)|(»)|(“)|(”) +", "", str)


def removeEnye(str):
    return re.sub(r"(n)/i", "n", str)


def strip_undesired_chars(tweet):
    stripped_tweet = tweet.replace('\n', ' ').replace('\r', '')
    char_list = [stripped_tweet[j] for j in range(
        len(stripped_tweet)) if ord(stripped_tweet[j]) in range(65536)]
    stripped_tweet = ''
    for j in char_list:
        stripped_tweet = stripped_tweet + j

    removed_url = stripped_tweet.translate(trans)
    return removeEnye(removeSign((remove_url(removed_url))))


## write csv

def write_csv_type_of_param(nombre_archivo_salida, outtweets, type):
    with open(nombre_archivo_salida, type, newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        if type == "w":
            writer.writerow(['created_at', 'text'])
        writer.writerows(outtweets)
    pass


def write_csv(tweets):
    nombre_archivo_salida = input(
        "Introduce el nombre del archivo csv de salida (si el archivo ya existe se añaden los nuevos datos al mismo): ");
    outtweets = [(tweet.created_at, strip_undesired_chars(
        tweet.full_text)) for tweet in tweets]

    if os.path.isfile(nombre_archivo_salida):
        write_csv_type_of_param(nombre_archivo_salida, outtweets, "a");
    else:
        write_csv_type_of_param(nombre_archivo_salida, outtweets, "w");


write_csv(tweets_search());
