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
    print("🛰️ Scouting Pollinations API...")
    try:
        # Fetch Text Models
        text_resp = requests.get("https://gen.pollinations.ai/text/models", timeout=10).json()
        text_models = [m["name"] for m in text_resp if "name" in m]
        
        # Fetch Image & Video Models
        img_vid_resp = requests.get("https://gen.pollinations.ai/image/models", timeout=10).json()
        
        image_models = []
        video_models = []
        
        for m in img_vid_resp:
            model_id = m.get("name")
            if not model_id: continue
            if m.get("type") == "video":
                video_models.append(model_id)
            else:
                image_models.append(model_id)
                
        # Safety defaults
        if "flux" not in image_models: image_models.insert(0, "flux")
        if "wan" not in video_models: video_models.insert(0, "wan")
        if "openai" not in text_models: text_models.insert(0, "openai")

        return {"image": image_models, "video": video_models, "text": text_models}
    except Exception as e:
        print(f"❌ API Fetch Failed: {e}")
        return None

def update_json_file(models):
    print("💾 Updating models.json...")
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(models, f, indent=4)

def update_readme(models):
    print("📝 Updating README.md...")
    if not os.path.exists(README_FILE):
        return

    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_section(header, new_list, text):
        # Regex to find the list between "Supported Models:**" and "* **Parameters"
        # It handles the markdown list format
        pattern = f"(###.*?{header}.*?\n\\* \\*\\*Supported Models:\\*\\*\n)(.*?)(?=\n\\* \\*\\*Parameters:\\*\\*)"
        formatted_list = "\n".join([f"  * `{m}`" for m in new_list])
        return re.sub(pattern, f"\\1{formatted_list}", text, flags=re.DOTALL | re.IGNORECASE)

    content = replace_section("Image Gen", models["image"], content)
    content = replace_section("Video Gen", models["video"], content)
    content = replace_section("Text Gen", models["text"], content)

    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def git_commit_and_push():
    print("🚀 Pushing updates...")
    try:
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=REPO_DIR)
        if not status.stdout.strip():
            print("   ✅ No changes detected.")
            return

        date_str = datetime.now().strftime("%Y-%m-%d")
        subprocess.run(["git", "add", "models.json", "README.md"], cwd=REPO_DIR)
        subprocess.run(["git", "commit", "-m", f"Auto-Update: Sync models.json with API ({date_str})"], cwd=REPO_DIR)
        subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR)
        subprocess.run(["git", "push", "huggingface", "main"], cwd=REPO_DIR)
        print("🎉 Update Pushed!")
    except Exception as e:
        print(f"❌ Git Push Failed: {e}")

if __name__ == "__main__":
    models = fetch_api_models()
    if models:
        update_json_file(models)
        update_readme(models)
        git_commit_and_push()