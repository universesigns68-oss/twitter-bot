import os
import random
import tweepy

client = tweepy.Client(
    consumer_key=os.environ["X_API_KEY"],
    consumer_secret=os.environ["X_API_SECRET"],
    access_token=os.environ["X_ACCESS_TOKEN"],
    access_token_secret=os.environ["X_ACCESS_SECRET"],
)

messages = [
    "trust the timing",
    "something is coming",
    "they still think about you",
    "good news is near",
    "stop overthinking"
]

zodiac = [
    "aries","taurus","gemini","cancer",
    "leo","virgo","libra","scorpio",
    "sagittarius","capricorn","aquarius","pisces"
]

post = f"{random.choice(zodiac)}, {random.choice(messages)}"

client.create_tweet(text=post)

print("posted:", post)
