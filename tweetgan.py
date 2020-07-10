import tweepy
from aitextgen import aitextgen

# Without any parameters, aitextgen() will download, cache, and load the 124M GPT-2 "small" model
ai = aitextgen()

ai.generate()
ai.generate(n=3, max_length=100)
ai.generate(n=3, prompt="This can be anything ", max_length=100)
ai.generate(n=3, prompt="Literally, anything", max_length=100, temperature=1.2)

#### Create keys to send tweets from gan text #####
CONSUMER_KEY="xxxx"
CONSUMER_SECRET="xxxxx"
ACCESS_TOKEN="xxxxxx"
ACCESS_TOKEN_SECRET="xxxx"

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)
user = api.me()

# Create a tweet
print("Enter what you want to tweet : ")
x = input()


api.update_status(x)
print("You Tweeted " + x)
print(user.name)
