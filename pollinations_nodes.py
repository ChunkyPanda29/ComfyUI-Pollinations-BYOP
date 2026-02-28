import urllib.parse
import requests
import torch
import numpy as np
from PIL import Image
import io

class PollinationsImageGen:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "A cinematic product shot..."}),
                "model": (["flux", "klein-large", "gptimage"], {"default": "flux"}),
                "width": ("INT", {"default": 1024, "min": 256, "max": 4096}),
                "height": ("INT", {"default": 1024, "min": 256, "max": 4096}),
                "seed": ("INT", {"default": 42, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "api_key": ("STRING", {"default": "", "multiline": False}), # BYOP integration
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "generate"
    CATEGORY = "Pollinations"

    def generate(self, prompt, model, width, height, seed, api_key):
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model={model}&width={width}&height={height}&seed={seed}&nologo=true"
        
        headers = {}
        # BYOP Logic: If the user provides a key, we use their Pollen!
        if api_key and api_key.strip() != "":
            headers["Authorization"] = f"Bearer {api_key.strip()}"
            
        print(f"🌸 [Pollinations] Generating with {model}...")
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content)).convert("RGB")
            # Convert PIL image to ComfyUI Tensor format
            image_np = np.array(image).astype(np.float32) / 255.0
            image_tensor = torch.from_numpy(image_np)[None,]
            return (image_tensor,)
        else:
            raise Exception(f"Pollinations API Error: {response.status_code} - {response.text}")