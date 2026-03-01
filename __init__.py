from .pollinations_nodes import PollinationsImageGen, PollinationsTextGen, PollinationsVideoGen, PollinationsAudioGen

NODE_CLASS_MAPPINGS = {
    "PollinationsImageGen": PollinationsImageGen,
    "PollinationsTextGen": PollinationsTextGen,
    "PollinationsVideoGen": PollinationsVideoGen,
    "PollinationsAudioGen": PollinationsAudioGen
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PollinationsImageGen": "🌸🖼️ Pollinations Image Gen (BYOP)",
    "PollinationsTextGen": "🌸🤖 Pollinations Text Gen (BYOP)",
    "PollinationsVideoGen": "🌸🎞️ Pollinations Video Gen URL (BYOP)",
    "PollinationsAudioGen": "🌸🔊 Pollinations Audio Gen (BYOP)"
}

# CRITICAL: This tells ComfyUI to load the JavaScript from the /js folder
WEB_DIRECTORY = "./js"

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']