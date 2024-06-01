import os

class ElaraMoodPlugin:
    def __init__(self, model_id="runwayml/stable-diffusion-v1-5", output_dir="outputs/images"):
        """Initialize the plugin with a diffusion model."""
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
        if torch.cuda.is_available():
            self.pipe = self.pipe.to("cuda")

    def generate_mood_image(self, mood, prompt_template="A digital character named Elara, {mood} expression, vibrant colors, futuristic setting"):
        """Generate an image based on Elara's mood."""
        prompt = prompt_template.format(mood=mood.lower())
        image = self.pipe(prompt).images[0]
        output_path = os.path.join(self.output_dir, f"elara_{mood.lower()}_{int(torch.cuda.random.seed())}.png")
        image.save(output_path)
        return output_path
