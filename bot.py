import os
import random
import tweepy

# ====== DEBUG (xóa sau khi ổn) ======
print("KEY:", bool(os.getenv("X_API_KEY")))
print("TOKEN:", bool(os.getenv("X_ACCESS_TOKEN")))
print("AI:", bool(os.getenv("OPENAI_API_KEY")))

# ====== KẾT NỐI X API ======
client = tweepy.Client(
    consumer_key=os.getenv("X_API_KEY"),
    consumer_secret=os.getenv("X_API_SECRET"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_SECRET"),
)

# ====== DATA (fallback) ======
ZODIAC = [
    "aries","taurus","gemini","cancer",
    "leo","virgo","libra","scorpio",
    "sagittarius","capricorn","aquarius","pisces"
]

MESSAGES = [
    "trust the timing",
    "something is coming",
    "they still think about you",
    "good news is near",
    "you feel it for a reason",
    "your intuition was right",
    "a shift is happening",
    "unexpected news arrives",
    "they miss you quietly",
    "wait a little longer"
]

def generate_text():
    """Không dùng AI để tiết kiệm chi phí. Có thể nâng cấp sau."""
    return random.choice(MESSAGES)

def post_tweet():
    try:
        text = f"{random.choice(ZODIAC)}, {generate_text()}"
        client.create_tweet(text=text)
        print("✅ Posted:", text)
    except Exception as e:
        print("❌ Error:", e)
        raise  # để Actions thấy lỗi (dễ debug)

if __name__ == "__main__":
    post_tweet()
