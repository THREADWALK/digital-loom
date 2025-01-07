import tweepy 
from textblob import TextBlob 
 
def advanced_sentiment_analysis(api_key, api_secret, access_token, access_secret): 
    auth = tweepy.OAuthHandler(api_key, api_secret) 
    auth.set_access_token(access_token, access_secret) 
    api = tweepy.API(auth) 
    mentions = api.mentions_timeline(count=50) 
    sentiments = [{"text": m.text, "polarity": TextBlob(m.text).sentiment.polarity} for m in mentions] 
    return sentiments 
