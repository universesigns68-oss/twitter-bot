import os
import random
import tweepy
from openai import OpenAI

# ====== DEBUG ======
print("KEY:", bool(os.getenv("X_API_KEY")))
print("TOKEN:", bool(os.getenv("X_ACCESS_TOKEN")))
print("AI:", bool(os.getenv("OPENAI_API_KEY")))

# ====== X API ======
client = tweepy.Client(
    consumer_key=os.getenv("X_API_KEY"),
    consumer_secret=os.getenv("X_API_SECRET"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_SECRET"),
)

# ====== OPENAI ======
ai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ZODIAC = [
    "aries","taurus","gemini","cancer",
    "leo","virgo","libra","scorpio",
    "sagittarius","capricorn","aquarius","pisces"
]

# ====== PROMPT MODES ======
def generate_ai_text():
    try:
        mode = random.choice(["soft", "deep", "controversial"])

        if mode == "soft":
            prompt = """
Write ONE short horoscope sentence.

Rules:
- 4 to 6 words
- lowercase only
- emotional and comforting
- vague and relatable
- no punctuation
"""
        elif mode == "deep":
            prompt = """
Write ONE deep emotional horoscope sentence.

Rules:
- 4 to 7 words
- lowercase
- introspective and slightly sad
- feel like inner realization
- no punctuation
"""
        else:
            prompt = """
Write ONE viral horoscope-style sentence.

Rules:
- 4 to 8 words
- lowercase only
- emotionally intense
- slightly controversial but NOT offensive
- feel like a hidden truth
- make reader question themselves
- no punctuation

Themes:
- they ignored you
- you stayed too long
- someone regrets losing you
- you knew already
"""

        res = ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=30
        )

        text = res.choices[0].message.content.strip().lower()

        # clean text
        text = text.replace(".", "").replace(",", "")

        return text

    except Exception as e:
        print("AI error:", e)
        return "you already know the truth"

# ====== POST ======
def post_tweet():
    try:
        sign = random.choice(ZODIAC)
        msg = generate_ai_text()

        tweet = f"{sign}, {msg}"

        client.create_tweet(text=tweet)

        print("✅ Posted:", tweet)

    except Exception as e:
        print("❌ Error:", e)
        raise

# ====== RUN ======
if __name__ == "__main__":
    post_tweet()
