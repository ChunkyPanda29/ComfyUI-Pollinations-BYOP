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
    print("🛰️ Scouting Pollinations API for new models (Premium Aware)...")
    try:
        # 1. Fetch Text Models
        text_resp = requests.get("https://gen.pollinations.ai/text/models", timeout=10).json()
        # We append 💎 if paid_only is True
        text_models = [
            f"{m['name']} 💎" if m.get("paid_only") else m["name"] 
            for m in text_resp if "name" in m
        ]
        
        # 2. Fetch Image & Video Models
        img_vid_resp = requests.get("https://gen.pollinations.ai/image/models", timeout=10).json()
        
        image_models = []
        video_models = []
        
        for m in img_vid_resp:
            model_id = m.get("name")
            if not model_id: continue
            
            # Append diamond for paid models
            display_name = f"{model_id} 💎" if m.get("paid_only") else model_id
            
            # Detect video models via output_modalities array
            out_modalities = m.get("output_modalities", [])
            if "video" in out_modalities:
                video_models.append(display_name)
            else:
                image_models.append(display_name)
                
        # Safety defaults (Clean IDs - 💎 logic handled later in script if missing)
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

    def replace_md_list(section_id, new_list, text):
        escaped_id = re.escape(section_id)
        pattern = rf"(###.*?{escaped_id}.*?\n\* \*\*Supported Models:\*\*.*?\n)(.*?)(\n\* \*\*Parameters|\n---|\n##)"
        formatted_list = "\n".join([f"  * `{m}`" for m in new_list])
        return re.sub(pattern, f"\\1{formatted_list}\\3", text, flags=re.DOTALL | re.IGNORECASE)

    content = replace_md_list("Image Gen", models["image"], content)
    content = replace_md_list("Video Gen", models["video"], content)
    content = replace_md_list("Text Gen", models["text"], content)

    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

def git_sync_everything():
    print("🚀 Synchronizing local machine to GitHub and HuggingFace...")
    try:
        subprocess.run(["git", "add", "."], cwd=REPO_DIR)
        
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=REPO_DIR)
        if not status.stdout.strip():
            print("   ✅ Local state matches previous commit.")
            return

        date_str = datetime.now().strftime("%Y-%m-%d")
        subprocess.run(["git", "commit", "-m", f"Auto-Sync: Premium Labels & Models ({date_str})"], cwd=REPO_DIR)
        
        print("   Merging cloud changes...")
        subprocess.run(["git", "pull", "origin", "main", "-X", "ours", "--no-edit"], cwd=REPO_DIR)
        
        print("   Pushing to GitHub (origin)...")
        subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR)
        
        print("   Pushing to HuggingFace...")
        subprocess.run(["git", "push", "huggingface", "main", "--force"], cwd=REPO_DIR)
        
        print("🎉 Full sync complete!")
    except Exception as e:
        print(f"❌ Git Sync Failed: {e}")

if __name__ == "__main__":
    print(f"=== Pollinations Engine Updater: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
    os.chdir(REPO_DIR)
    
    live_models = fetch_api_models()
    if live_models:
        update_json_file(live_models)
        update_readme(live_models)
        git_sync_everything()