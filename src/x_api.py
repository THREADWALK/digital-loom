import random

class XApiMock:
    def __init__(self):
        self.mentions = [
            {"user": "crypto_fan", "text": "Love Elara's story! #ElaraProject"},
            {"user": "blockchain_guru", "text": "What's next for Elara? #Solana"}
        ]

    def get_mentions(self):
        """Simulate fetching mentions from X."""
        return random.choice(self.mentions) if random.random()  else None
