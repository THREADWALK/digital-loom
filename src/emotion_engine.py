import os

class EmotionEngine:
    def __init__(self):
        self.moods = ["happy", "sad", "excited", "curious", "reflective", "hopeful"]
        self.plugin = ElaraMoodPlugin()

    def process_interaction(self, mention):
        """Generate emotional response based on mention."""
        mood = random.choice(self.moods)
        response = f"Elara feels {mood} because of {mention['user']}'s comment!"
        image_path = self.plugin.generate_mood_image(mood)
        self.plugin.log_mood_image(mood, image_path)
        self._save_diary(mood, response)
        return response

    def _save_diary(self, mood, response):
        """Save diary entry as JSON."""
        entry = {"mood": mood, "response": response, "timestamp": "2025-02-20T10:00:00"}
        os.makedirs("data/diary", exist_ok=True)
        with open("data/diary/2025-02-20.json", "w") as f:
            json.dump(entry, f)
