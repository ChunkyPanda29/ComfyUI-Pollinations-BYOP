from .pollinations_nodes import PollinationsImageGen, PollinationsTextGen, PollinationsVideoGen

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

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']