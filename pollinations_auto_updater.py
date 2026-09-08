import requests
import json
import re
import os
import subprocess
from datetime import datetime

# --- CONFIGURATION ---
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(REPO_DIR, "models.json")
README_FILE = os.path.join(REPO_DIR, "README.md")

def display_names(model):
    # ComfyUI validates saved workflow values against the dropdown's enum.
    names = [model["name"], *(model.get("aliases") or [])]
    return [f"{name} 💎" if model.get("paid_only") else name for name in names]

def fetch_api_models():
    print("🛰️ Scouting Pollinations Official API (Quad-Modal Pass)...")
    try:
        # 1. Text Models
        text_resp = requests.get("https://gen.pollinations.ai/text/models", timeout=10).json()
        text_models = [name for m in text_resp if "name" in m for name in display_names(m)]
        
        # 2. Image & Video Models
        img_vid_resp = requests.get("https://gen.pollinations.ai/image/models", timeout=10).json()
        image_models, video_models = [], []
        for m in img_vid_resp:
            name = m.get("name")
            if not name: continue
            if "video" in m.get("output_modalities", []):
                video_models.extend(display_names(m))
            else:
                image_models.extend(display_names(m))

        # 3. Audio Models
        audio_resp = requests.get("https://gen.pollinations.ai/audio/models", timeout=10).json()
        audio_models = [name for m in audio_resp if "name" in m for name in display_names(m)]

        return {
            "image": sorted(set(image_models)),
            "video": sorted(set(video_models)),
            "text": sorted(set(text_models)),
            "audio": sorted(set(audio_models))
        }
    except Exception as e:
        print(f"❌ API Fetch Failed: {e}")
        return None

def update_readme(models):
    print("📝 Updating README.md...")
    if not os.path.exists(README_FILE): return
    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_md_list(marker, new_list, text):
        # Escapes the marker and looks for the "Supported Models" block immediately after
        pattern = rf"({re.escape(marker)}.*?\n\* \*\*Supported Models:\*\*.*?\n)(.*?)(\n\* \*\*Parameters|\n---|\n##|\Z)"
        formatted_list = "\n".join([f"  * `{m}`" for m in new_list])
        return re.sub(pattern, f"\\1{formatted_list}\\3", text, flags=re.DOTALL)

    content = replace_md_list("1. 🌸🖼️ Pollinations Image Gen", models["image"], content)
    content = replace_md_list("2. 🌸🎞️ Pollinations Video Gen", models["video"], content)
    content = replace_md_list("3. 🌸🤖 Pollinations Text Gen", models["text"], content)
    content = replace_md_list("4.🌸🔊 Pollinations Audio Gen", models["audio"], content)

    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def git_sync_everything():
    print("🚀 Synchronizing machine to Cloud...")
    try:
        subprocess.run(["git", "add", "."], cwd=REPO_DIR)
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=REPO_DIR)
        if not status.stdout.strip():
            print("   ✅ No changes detected.")
            return
        date_str = datetime.now().strftime("%Y-%m-%d")
        subprocess.run(["git", "commit", "-m", f"Auto-Sync: Full Quad-Modal Refresh ({date_str})"], cwd=REPO_DIR)
        subprocess.run(["git", "pull", "origin", "main", "-X", "ours", "--no-edit"], cwd=REPO_DIR)
        subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR)
        subprocess.run(["git", "push", "huggingface", "main", "--force"], cwd=REPO_DIR)
        print("🎉 Full sync complete!")
    except Exception as e:
        print(f"❌ Git Sync Failed: {e}")

if __name__ == "__main__":
    os.chdir(REPO_DIR)
    live_models = fetch_api_models()
    if live_models:
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(live_models, f, indent=4)
        update_readme(live_models)
        git_sync_everything()
