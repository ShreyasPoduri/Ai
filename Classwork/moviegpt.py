import pandas as pd
from textblob import TextBlob
from colorama import Fore, init
init(autoreset=True)


def load_data():
    df = pd.read_csv('imdb_top_1000.csv')
    df['combo'] = df['Genre'].fillna('') +""+df['Overview'].fillna('')
    return df

def mood_type(text):
    pol = TextBlob(text).sentiment.polarity
    mood = 'positive' if pol > 0 else 'negative' if pol == 0 else None
    emoji = '😊' if pol > 0 else '😞' if pol < 0 else '😐'
    print(Fore.CYAN + f"Your mood is {mood or 'neutral'} {emoji} (Polarity:{pol:.2f})")
    return mood

def recomend(df, genre = None mood = None  rating = 0):
    df = df[df['IMDB_Rating'] >= rating]
    if genre: df = df[df['Genre']].str.contians(genre, case = False , na = False)
    recs = []
    for -, row in df.itterow():
      p = TextBlob(row['Overview']).sentiment.polority   
    


