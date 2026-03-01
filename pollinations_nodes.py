import urllib.parse
import requests
import torch
import numpy as np
from PIL import Image
import io
import json
import time
import logging
import os

# SILENCE LOGGERS (Prevent WinError 233)
logging.getLogger("requests").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)

def load_model_list(category, default_list):
    """Safely loads model lists from models.json relative to this file."""
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
        # Default fallback if JSON fails
        defaults = ["flux", "turbo", "klein"]
        model_list = load_model_list("image", defaults)
        
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "A cinematic product shot..."}),
                "model": (model_list, {"default": "flux"}),
                "width": ("INT", {"default": 1024, "min": 256, "max": 4096, "step": 8}),
                "height": ("INT", {"default": 1024, "min": 256, "max": 4096, "step": 8}),
                "seed": ("INT", {"default": 42, "min": 0, "max": 0xffffffffffffffff}),
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
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?model={model}&width={width}&height={height}&seed={seed}&nologo=true"
        
        if negative_prompt and negative_prompt.strip() != "":
             encoded_neg = urllib.parse.quote(negative_prompt)
             url += f"&nofeed={encoded_neg}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "image/jpeg, image/png, image/*"
        }
        
        if api_key and api_key.strip() != "":
            headers["Authorization"] = f"Bearer {api_key.strip()}"
            
        try:
            response = requests.get(url, headers=headers, timeout=120)
            if response.status_code == 200:
                image_bytes = io.BytesIO(response.content)
                image = Image.open(image_bytes).convert("RGB")
                image_np = np.array(image).astype(np.float32) / 255.0
                image_tensor = torch.from_numpy(image_np)[None,]
                return (image_tensor,)
            else:
                error_img = torch.zeros((1, 512, 512, 3))
                error_img[:, :, :, 0] = 1.0 
                return (error_img,)
        except Exception:
            error_img = torch.zeros((1, 512, 512, 3))
            error_img[:, :, :, 2] = 1.0 
            return (error_img,)

class PollinationsTextGen:
    @classmethod
    def INPUT_TYPES(s):
        defaults = ["openai", "claude", "mistral"]
        model_list = load_model_list("text", defaults)

        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "Write a viral TikTok script..."}),
                "system_instruction": ("STRING", {"multiline": True, "default": "You are a creative assistant."}),
                "model": (model_list, {"default": "openai"}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 2.0, "step": 0.1}),
                "seed": ("INT", {"default": 42, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "api_key": ("STRING", {"default": "", "multiline": False})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "generate"
    CATEGORY = "Pollinations"

    def generate(self, prompt, system_instruction, model, temperature, seed, api_key):
        url = "https://text.pollinations.ai/"
        headers = {"Content-Type": "application/json", "User-Agent": "ComfyUI-Pollinations-Node"}
        
        if api_key and api_key.strip() != "":
            headers["Authorization"] = f"Bearer {api_key.strip()}"
            
        payload = {
            "messages": [
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ],
            "model": model,
            "temperature": temperature,
            "seed": seed
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=60)
            if response.status_code == 200:
                if 'application/json' in response.headers.get('Content-Type', ''):
                     try:
                         result_text = response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
                         return (result_text,)
                     except:
                         return (response.text,)
                else:
                     return (response.text,)
            else:
                return (f"Error: {response.status_code}",)
        except Exception as e:
            return (f"Exception: {e}",)

class PollinationsVideoGen:
    @classmethod
    def INPUT_TYPES(s):
        defaults = ["wan", "luma", "kling"]
        model_list = load_model_list("video", defaults)

        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "A cinematic shot of..."}),
                "model": (model_list, {"default": "wan"}),
                "seed": ("INT", {"default": 42, "min": 0, "max": 0xffffffffffffffff}),
            },
            "optional": {
                "api_key": ("STRING", {"default": "", "multiline": False})
            }
        }

    RETURN_TYPES = ("STRING",) 
    RETURN_NAMES = ("video_url",)
    FUNCTION = "generate"
    CATEGORY = "Pollinations"

    def generate(self, prompt, model, seed, api_key):
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://video.pollinations.ai/prompt/{encoded_prompt}?model={model}&seed={seed}"
        return (url,)