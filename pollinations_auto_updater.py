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

def fetch_api_models():
    print("🛰️ Scouting Pollinations Official API (Quad-Modal Pass)...")
    try:
        # 1. Text Models
        text_resp = requests.get("https://gen.pollinations.ai/text/models", timeout=10).json()
        text_models = [f"{m['name']} 💎" if m.get("paid_only") else m["name"] for m in text_resp if "name" in m]
        
        # 2. Image & Video Models
        img_vid_resp = requests.get("https://gen.pollinations.ai/image/models", timeout=10).json()
        image_models, video_models = [], []
        for m in img_vid_resp:
            name = m.get("name")
            if not name: continue
            display = f"{name} 💎" if m.get("paid_only") else name
            if "video" in m.get("output_modalities", []):
                video_models.append(display)
            else:
                image_models.append(display)

        # 3. Audio Models (NEW)
        audio_resp = requests.get("https://gen.pollinations.ai/audio/models", timeout=10).json()
        audio_models = [f"{m['name']} 💎" if m.get("paid_only") else m["name"] for m in audio_resp if "name" in m]

        # Safety Fallbacks
        if not text_models: text_models = ["openai"]
        if not image_models: image_models = ["flux"]
        if not video_models: video_models = ["wan"]
        if not audio_models: audio_models = ["elevenlabs"]

        return {
            "image": sorted(image_models), 
            "video": sorted(video_models), 
            "text": sorted(text_models),
            "audio": sorted(audio_models)
        }
    except Exception as e:
        print(f"❌ API Fetch Failed: {e}")
        return None

def update_readme(models):
    print("📝 Updating README.md...")
    if not os.path.exists(README_FILE): return
    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_md_list(section_id, new_list, text):
        escaped_id = re.escape(section_id)
        # Regex looks for the section header down to the next parameter or section break
        pattern = rf"(###.*?{escaped_id}.*?\n\* \*\*Supported Models:\*\*.*?\n)(.*?)(\n\* \*\*Parameters|\n---|\n##)"
        formatted_list = "\n".join([f"  * `{m}`" for m in new_list])
        return re.sub(pattern, f"\\1{formatted_list}\\3", text, flags=re.DOTALL | re.IGNORECASE)

    content = replace_md_list("Image Gen", models["image"], content)
    content = replace_md_list("Video Gen", models["video"], content)
    content = replace_md_list("Text Gen", models["text"], content)
    content = replace_md_list("Audio Gen", models["audio"], content)

    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def git_sync_everything():
    print("🚀 Synchronizing local machine to Cloud...")
    try:
        subprocess.run(["git", "add", "."], cwd=REPO_DIR)
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=REPO_DIR)
        if not status.stdout.strip():
            print("   ✅ Local state matches previous commit.")
            return
        date_str = datetime.now().strftime("%Y-%m-%d")
        subprocess.run(["git", "commit", "-m", f"Auto-Sync: Quad-Modal Update ({date_str})"], cwd=REPO_DIR)
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