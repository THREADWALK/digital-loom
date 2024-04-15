import os

class EmotionEngine:
    def __init__(self):
        self.moods = ["happy", "sad", "excited", "curious"]

    def process_interaction(self, mention):
        """Generate emotional response based on mention."""
        mood = random.choice(self.moods)
        response = f"Elara feels {mood} because of {mention['user']}'s comment!"
        self._save_diary(mood, response)
        return response

    def _save_diary(self, mood, response):
        """Save diary entry as JSON."""
        entry = {"mood": mood, "response": response, "timestamp": "2024-04-15T10:00:00"}
        os.makedirs("data/diary", exist_ok=True)
        with open("data/diary/2024-04-15.json", "w") as f:
            json.dump(entry, f)
