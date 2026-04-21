import os
import random
import tweepy
from openai import OpenAI

# ====== DEBUG (xoá sau khi chạy OK) ======
print("KEY:", os.getenv("X_API_KEY"))
print("TOKEN:", os.getenv("X_ACCESS_TOKEN"))
print("AI:", os.getenv("OPENAI_API_KEY"))

# ====== X API ======
client = tweepy.Client(
    consumer_key=os.getenv("X_API_KEY"),
    consumer_secret=os.getenv("X_API_SECRET"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_SECRET"),
)

# ====== OPENAI ======
ai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

zodiac = [
    "aries","taurus","gemini","cancer",
    "leo","virgo","libra","scorpio",
    "sagittarius","capricorn","aquarius","pisces"
]

# ====== AI GENERATE ======
def generate_ai_text():
    try:
        prompt = """
Write ONE short viral horoscope sentence.

Rules:
- 3 to 6 words
- lowercase only
- no punctuation
- emotional, mysterious, relatable
- sounds like a sign from universe
"""

        res = ai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=20
        )

        text = res.choices[0].message.content.strip().lower()

        # clean
        text = text.replace(".", "").replace(",", "")

        return text

    except Exception as e:
        print("AI error:", e)
        return "trust the timing"

# ====== POST ======
def post_tweet():
    try:
        sign = random.choice(zodiac)
        msg = generate_ai_text()

        tweet = f"{sign}, {msg}"

        client.create_tweet(text=tweet)

        print("✅ Posted:", tweet)

    except Exception as e:
        print("❌ Error:", e)

# ====== RUN ======
if __name__ == "__main__":
    post_tweet()
