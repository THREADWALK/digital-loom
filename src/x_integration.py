import tweepy 
 
def monitor_mentions(api_key, api_secret, access_token, access_secret): 
    auth = tweepy.OAuthHandler(api_key, api_secret) 
    auth.set_access_token(access_token, access_secret) 
    api = tweepy.API(auth) 
    mentions = api.mentions_timeline(count=10) 
    return [mention.text for mention in mentions] 
