from .pollinations_nodes import PollinationsImageGen, PollinationsTextGen, PollinationsVideoGen, PollinationsAudioGen, PollinationsBYOPLogin

NODE_CLASS_MAPPINGS = {
    "PollinationsImageGen": PollinationsImageGen,
    "PollinationsTextGen": PollinationsTextGen,
    "PollinationsVideoGen": PollinationsVideoGen,
    "PollinationsAudioGen": PollinationsAudioGen,
    "PollinationsBYOPLogin": PollinationsBYOPLogin
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PollinationsImageGen": "🌸🖼️ Pollinations Image Gen (BYOP)",
    "PollinationsTextGen": "🌸🤖 Pollinations Text Gen (BYOP)",
    "PollinationsVideoGen": "🌸🎞️ Pollinations Video Gen URL (BYOP)",
    "PollinationsAudioGen": "🌸🔊 Pollinations Audio Gen (BYOP)",
    "PollinationsBYOPLogin": "🔐🌸 Pollinations BYOP Login"
}

# CRITICAL: This tells ComfyUI to load the JavaScript from the /js folder
WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']