import random

class HeliusApiMock:
    def get_token_activity(self):
        """Simulate token trading activity."""
        return {
            "trades": random.randint(0, 100),
            "volume": random.uniform(1000, 10000)
        }
