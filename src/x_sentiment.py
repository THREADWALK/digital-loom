import tweepy 
from textblob import TextBlob 
 
def analyze_sentiment(api_key, api_secret, access_token, access_secret): 
    auth = tweepy.OAuthHandler(api_key, api_secret) 
    auth.set_access_token(access_token, access_secret) 
    api = tweepy.API(auth) 
    mentions = api.mentions_timeline(count=20) 
    sentiments = [TextBlob(m.text).sentiment.polarity for m in mentions] 
    return sum(sentiments) / len(sentiments) if sentiments else 0 
