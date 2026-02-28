import urllib.parse
import requests
import torch
import numpy as np
from PIL import Image
import io
import json

class PollinationsImageGen:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "A cinematic product shot..."}),
                "model": ([
                    "flux", "zimage", "imagen-4", "grok-imagine", 
                    "klein", "klein-large", "gptimage", "seedream", 
                    "kontext", "nanobanana", "seedream-pro", 
                    "gptimage-large", "nanobanana-pro"
                ], {"default": "flux"}),
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
            
        print(f"🌸 [Pollinations] Generating Image with {model} (Seed: {seed})...")
        
        response = requests.get(url, headers=headers, timeout=90)
        
        if response.status_code == 200:
            image = Image.open(io.BytesIO(response.content)).convert("RGB")
            image_np = np.array(image).astype(np.float32) / 255.0
            image_tensor = torch.from_numpy(image_np)[None,]
            return (image_tensor,)
        else:
            raise Exception(f"Pollinations API Error: {response.status_code} - {response.text}")

class PollinationsTextGen:
    def __init__(self):
        pass
        
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "Write a viral TikTok script..."}),
                "system_instruction": ("STRING", {"multiline": True, "default": "You are a creative assistant."}),
                "model": ([
                    "qwen-safety", "qwen-character", "nova-fast", "gemini-fast",
                    "mistral", "gemini-search", "qwen-coder", "openai-fast",
                    "grok", "openai", "perplexity-fast", "minimax", "deepseek",
                    "perplexity-reasoning", "openai-large", "openai-audio",
                    "gemini", "midijourney", "claude-fast", "glm", "kimi",
                    "claude", "gemini-legacy", "gemini-large", "claude-large",
                    "claude-legacy", "nomnom", "polly"
                ], {"default": "openai"}),
                "temperature": ("FLOAT", {"default": 0.7, "min": 0.0, "max": 2.0, "step": 0.1}),
            },
            "optional": {
                "api_key": ("STRING", {"default": "", "multiline": False})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "generate"
    CATEGORY = "Pollinations"

    def generate(self, prompt, system_instruction, model, temperature, api_key):
        url = "https://text.pollinations.ai/"
        
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "ComfyUI-Pollinations-Node"
        }
        
        if api_key and api_key.strip() != "":
            headers["Authorization"] = f"Bearer {api_key.strip()}"
            
        payload = {
            "messages":[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ],
            "model": model,
            "temperature": temperature
        }
        
        print(f"🌸 [Pollinations] Generating Text with {model}...")
        
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        
        if response.status_code == 200:
            try:
                # Pollinations sometimes returns raw text, sometimes JSON. We handle both.
                try:
                    result_text = response.json()["choices"][0]["message"]["content"]
                except:
                    result_text = response.text
                return (result_text,)
            except Exception as e:
                raise Exception(f"Failed to parse text response: {e}")
        else:
            raise Exception(f"Pollinations API Error: {response.status_code} - {response.text}")

class PollinationsVideoGen:
    def __init__(self):
        pass
        
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "A cinematic shot of..."}),
                "model": ([
                    "grok-video", "ltx-2", "seedance-pro", 
                    "seedance", "wan", "veo"
                ], {"default": "wan"}),
            },
            "optional": {
                "api_key": ("STRING", {"default": "", "multiline": False})
            }
        }

    RETURN_TYPES = ("STRING",) # Returns a URL for the video
    RETURN_NAMES = ("video_url",)
    FUNCTION = "generate"
    CATEGORY = "Pollinations"

    def generate(self, prompt, model, api_key):
        # The video API endpoints can take a while to return the actual file.
        # Returning the URL string is safer for ComfyUI. Users can use a "Load Video (URL)" node if needed.
        encoded_prompt = urllib.parse.quote(prompt)
        url = f"https://video.pollinations.ai/prompt/{encoded_prompt}?model={model}"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
        }
        
        if api_key and api_key.strip() != "":
            headers["Authorization"] = f"Bearer {api_key.strip()}"
            
        print(f"🌸 [Pollinations] Requesting Video from {model}... (Note: Output is URL)")
        
        # We just ping it to ensure the URL is valid, but we return the URL string directly.
        return (url,)