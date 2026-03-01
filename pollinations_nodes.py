import urllib.parse
import requests
import torch
import numpy as np
from PIL import Image
import io
import json
import os
import logging

# SILENCE LOGGERS to prevent any console/pipe conflicts
logging.getLogger("requests").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)

def load_model_list(category, default_list):
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(current_dir, "models.json")
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get(category, default_list)
    except Exception:
        pass
    return default_list

class PollinationsImageGen:
    @classmethod
    def INPUT_TYPES(s):
        model_list = load_model_list("image", ["flux", "zimage", "klein-large"])
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "a cat in space"}),
                "model": (model_list, {"default": "flux"}),
                "width": ("INT", {"default": 1024, "min": 256, "max": 4096, "step": 8}),
                "height": ("INT", {"default": 1024, "min": 256, "max": 4096, "step": 8}),
                "seed": ("INT", {"default": 42, "min": -1, "max": 2147483647}),
            },
            "optional": {
                "api_key": ("STRING", {"default": "", "multiline": False}),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""})
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "generate"
    CATEGORY = "Pollinations"

    def generate(self, prompt, model, width, height, seed, api_key, negative_prompt=""):
        # Clean the model name by removing the diamond emoji and extra spaces
        model = model.replace("💎", "").strip()
        # 1. Official Path Construction
        encoded_prompt = urllib.parse.quote(prompt.replace("\n", " ").strip())
        
        # Base URL from official api.json
        base_url = f"https://gen.pollinations.ai/image/{encoded_prompt}"
        
        # 2. Query Parameters (Official Spec)
        params = {
            "model": model,
            "width": width,
            "height": height,
            "seed": seed,
            "nologo": "true"
        }
        
        if negative_prompt and negative_prompt.strip() != "":
             params["negative_prompt"] = negative_prompt.strip()

        # 3. Headers (Crucial for WAF bypass and BYOP)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        }
        
        if api_key and api_key.strip() != "":
            headers["Authorization"] = f"Bearer {api_key.strip()}"
            
        try:
            response = requests.get(base_url, params=params, headers=headers, timeout=120)
            
            if response.status_code == 200:
                image = Image.open(io.BytesIO(response.content)).convert("RGB")
                image_np = np.array(image).astype(np.float32) / 255.0
                return (torch.from_numpy(image_np)[None,],)
            else:
                # Return Black square with Red pixel in corner on error
                err_img = np.zeros((width, height, 3), dtype=np.float32)
                err_img[0,0] = [1.0, 0, 0] 
                return (torch.from_numpy(err_img)[None,],)
                
        except Exception:
            return (torch.zeros((1, 512, 512, 3)),)

class PollinationsTextGen:
    @classmethod
    def INPUT_TYPES(s):
        model_list = load_model_list("text", ["openai", "deepseek", "gemini"])
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "Hello!"}),
                "model": (model_list, {"default": "openai"}),
                "system_instruction": ("STRING", {"multiline": True, "default": "You are a helpful assistant."}),
                "seed": ("INT", {"default": 42, "min": -1, "max": 9007199254740991}),
            },
            "optional": {
                "api_key": ("STRING", {"default": "", "multiline": False})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "generate"
    CATEGORY = "Pollinations"

    def generate(self, prompt, model, system_instruction, seed, api_key):
        # Clean the model name by removing the diamond emoji and extra spaces
        model = model.replace("💎", "").strip()
        url = "https://gen.pollinations.ai/v1/chat/completions"
        headers = {"Content-Type": "application/json"}
        if api_key and api_key.strip() != "":
            headers["Authorization"] = f"Bearer {api_key.strip()}"
            
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ],
            "seed": seed
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            if response.status_code == 200:
                return (response.json()["choices"][0]["message"]["content"],)
            return (f"Error: {response.status_code}",)
        except Exception as e:
            return (str(e),)

class PollinationsVideoGen:
    @classmethod
    def INPUT_TYPES(s):
        model_list = load_model_list("video", ["wan", "seedance", "veo"])
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "a sunset timelapse"}),
                "model": (model_list, {"default": "wan"}),
            },
            "optional": {
                "api_key": ("STRING", {"default": "", "multiline": False})
            }
        }

    RETURN_TYPES = ("STRING",) 
    RETURN_NAMES = ("video_url",)
    FUNCTION = "generate"
    CATEGORY = "Pollinations"

    def generate(self, prompt, model, api_key):
        # Clean the model name by removing the diamond emoji and extra spaces
        model = model.replace("💎", "").strip()
        encoded_prompt = urllib.parse.quote(prompt.strip())
        url = f"https://gen.pollinations.ai/video/{encoded_prompt}?model={model}"
        if api_key and api_key.strip() != "":
            url += f"&key={api_key.strip()}"
        return (url,)

NODE_CLASS_MAPPINGS = {
    "PollinationsImageGen": PollinationsImageGen,
    "PollinationsTextGen": PollinationsTextGen,
    "PollinationsVideoGen": PollinationsVideoGen
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PollinationsImageGen": "🌸🖼️ Pollinations Image Gen (BYOP)",
    "PollinationsTextGen": "🌸🤖 Pollinations Text Gen (BYOP)",
    "PollinationsVideoGen": "🌸🎞️ Pollinations Video Gen URL (BYOP)"
}