import torch
from diffusers import StableDiffusionPipeline

# Load the Stable Diffusion model (move to CUDA if available)
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float32) 
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt):
    # Image generation process
    image = pipe(prompt).images[0]
    # Save the image
    image.save("generated_image.png")
    print(f"Image generated and saved as 'generated_image.png'!")

# Get prompt from the user
user_prompt = input("Enter the description for the image to generate: ")
generate_image(user_prompt)
