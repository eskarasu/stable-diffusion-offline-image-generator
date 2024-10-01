# Stable Diffusion Image Generator

This repository contains a Python script that utilizes the `Stable Diffusion` model to generate images from text prompts. The model can run on both GPU (CUDA) and CPU, depending on availability.

## Features

- Supports both GPU (CUDA) and CPU inference.
- Generates high-quality images from user-provided text prompts.
- Saves the generated images to your local system.

## Requirements

- Python 3.8+
- `torch`
- `diffusers`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/eskarasu/stable-diffusion-offline-image-generator.git
    ```

2. Install the required packages:
    ```bash
    pip install torch diffusers
    ```

3. (Optional) Ensure you have CUDA support installed to leverage GPU acceleration.

## Usage

To run the script, execute the following command in the terminal:

```bash
python image_generator.py
```

The script will prompt you to input a description for the image you want to generate. After processing, the generated image will be saved as generated_image.png.

## Example

Enter the description for the image to generate: "A sunset over a mountain"

After a few moments, the generated image will be saved as generated_image.png.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
