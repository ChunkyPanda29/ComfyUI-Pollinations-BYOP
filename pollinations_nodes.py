import urllib.parse
import requests
import torch
import numpy as np
from PIL import Image
import io
import json
import os
import logging
from server import PromptServer
from aiohttp import web

# SILENCE LOGGERS
logging.getLogger("requests").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)

# --- CONFIGURATION HANDLERS ---

def get_config_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "pollinations_config.json")

def get_models():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(current_dir, "models.json")
    try:
        if os.path.exists(json_path):
            with open(json_path, 'r', encoding='utf-8') as f:
                return json.load(f)
    except: pass
    return {"image": ["flux"], "video": ["wan"], "text": ["openai"], "audio": ["elevenlabs"]}

def get_api_key(manual_key):
    if manual_key and manual_key.strip() != "":
        return manual_key.strip()
    config_path = get_config_path()
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
                key = config.get("api_key")
                if key: return key.strip()
        except: pass
    return os.environ.get("POLLINATIONS_API_KEY", "")

# --- SERVER API ROUTE FOR SETTINGS ---

@PromptServer.instance.routes.post("/pollinations/save_key")
async def save_pollinations_key(request):
    json_data = await request.json()
    api_key = json_data.get("api_key")
    config_path = get_config_path()
    try:
        with open(config_path, 'w') as f:
            json.dump({"api_key": api_key}, f)
        return web.json_response({"status": "success"})
    except Exception as e:
        return web.json_response({"status": "error", "message": str(e)}, status=500)

# --- IMAGE UPLOADER ---

def upload_to_pollinations(image_tensor):
    try:
        i = 255. * image_tensor.cpu().numpy().squeeze()
        img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        resp = requests.post("https://media.pollinations.ai/upload", 
                             files={"file": ("image.png", buffered.getvalue(), "image/png")})
        if resp.status_code == 200: return resp.json().get("url")
    except: pass
    return None

# --- NODE CLASSES ---

class PollinationsImageGen:
    @classmethod
    def INPUT_TYPES(s):
        model_data = get_models()
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "a cat in space"}),
                "model": (model_data["image"], {"default": "flux"}),
                "width": ("INT", {"default": 1024, "min": 256, "max": 4096, "step": 8}),
                "height": ("INT", {"default": 1024, "min": 256, "max": 4096, "step": 8}),
                "seed": ("INT", {"default": 42, "min": -1, "max": 2147483647}),
            },
            "optional": {
                "api_key": ("STRING", {"default": "", "multiline": False, "placeholder": "Optional: Overrides Global Settings"}),
                "image_input": ("IMAGE",),
                "negative_prompt": ("STRING", {"multiline": True, "default": ""})
            }
        }
    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("image", "url")
    FUNCTION = "generate"
    CATEGORY = "Pollinations/Image"

    def generate(self, prompt, model, width, height, seed, api_key="", image_input=None, negative_prompt=""):
        final_key = get_api_key(api_key)
        model = model.replace("💎", "").strip()
        encoded_prompt = urllib.parse.quote(prompt.replace("\n", " ").strip())
        url = f"https://gen.pollinations.ai/image/{encoded_prompt}?model={model}&width={width}&height={height}&seed={seed}&nologo=true"
        if image_input is not None:
            img_url = upload_to_pollinations(image_input)
            if img_url: url += f"&image={urllib.parse.quote(img_url)}"
        if negative_prompt.strip(): url += f"&negative_prompt={urllib.parse.quote(negative_prompt.strip())}"
        headers = {"User-Agent": "Mozilla/5.0"}
        if final_key: headers["Authorization"] = f"Bearer {final_key}"
        try:
            r = requests.get(url, headers=headers, timeout=120)
            if r.status_code == 200:
                img = Image.open(io.BytesIO(r.content)).convert("RGB")
                return (torch.from_numpy(np.array(img).astype(np.float32) / 255.0)[None,], url)
        except: pass
        return (torch.zeros((1, 512, 512, 3)), url)

class PollinationsAudioGen:
    @classmethod
    def INPUT_TYPES(s):
        model_data = get_models()
        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "Hello world"}),
                "model": (model_data["audio"], {"default": "elevenlabs"}),
                "voice": (["alloy", "echo", "fable", "onyx", "nova", "shimmer", "sarah", "rachel", "charlie"], {"default": "sarah"}),
            },
            "optional": {"api_key": ("STRING", {"default": ""})}
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("audio_url",)
    FUNCTION = "generate"
    CATEGORY = "Pollinations/Audio"

    def generate(self, text, model, voice, api_key=""):
        final_key = get_api_key(api_key)
        model = model.replace("💎", "").strip()
        url = f"https://gen.pollinations.ai/audio/{urllib.parse.quote(text.strip())}?model={model}&voice={voice}"
        if final_key: url += f"&key={final_key}"
        return (url,)

class PollinationsVideoGen:
    @classmethod
    def INPUT_TYPES(s):
        model_data = get_models()
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "cinematic sunset"}),
                "model": (model_data["video"], {"default": "wan"}),
            },
            "optional": {
                "api_key": ("STRING", {"default": ""}),
                "image_input": ("IMAGE",),
                "duration": ("INT", {"default": 5, "min": 2, "max": 15}),
                "seed": ("INT", {"default": 42, "min": -1, "max": 2147483647}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("video_url",)
    FUNCTION = "generate"
    CATEGORY = "Pollinations/Video"

    def generate(self, prompt, model, api_key="", image_input=None, duration=5, seed=42):
        final_key = get_api_key(api_key)
        model = model.replace("💎", "").strip()
        url = f"https://gen.pollinations.ai/video/{urllib.parse.quote(prompt.strip())}?model={model}&duration={duration}&seed={seed}"
        if image_input is not None:
            img_url = upload_to_pollinations(image_input)
            if img_url: url += f"&image={urllib.parse.quote(img_url)}"
        if final_key: url += f"&key={final_key}"
        return (url,)

class PollinationsTextGen:
    @classmethod
    def INPUT_TYPES(s):
        model_data = get_models()
        return {
            "required": {
                "prompt": ("STRING", {"multiline": True, "default": "Hi!"}),
                "model": (model_data["text"], {"default": "openai"}),
                "system_instruction": ("STRING", {"multiline": True, "default": "You are a helpful assistant."}),
            },
            "optional": {"api_key": ("STRING", {"default": ""})}
        }
    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"
    CATEGORY = "Pollinations/Text"

    def generate(self, prompt, model, system_instruction, api_key=""):
        final_key = get_api_key(api_key)
        model = model.replace("💎", "").strip()
        url = "https://gen.pollinations.ai/v1/chat/completions"
        headers = {"Content-Type": "application/json"}
        if final_key: headers["Authorization"] = f"Bearer {final_key}"
        payload = {"model": model, "messages": [{"role": "system", "content": system_instruction}, {"role": "user", "content": prompt}]}
        try:
            r = requests.post(url, json=payload, headers=headers)
            return (r.json()["choices"][0]["message"]["content"],)
        except: return ("Error connecting to Text API",)