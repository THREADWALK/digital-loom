def generate_emotion(interactions): 
    sentiment_score = sum(1 for i in interactions if "positive" in i) - sum(1 for i in interactions if "negative" in i) 
    return "happy" if sentiment_score  else "neutral" 
