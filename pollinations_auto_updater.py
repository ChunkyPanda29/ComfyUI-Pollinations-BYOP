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
    print("🛰️ Scouting Pollinations API for new models...")
    try:
        # 1. Fetch Text Models
        text_resp = requests.get("https://gen.pollinations.ai/text/models", timeout=10).json()
        text_models = [m["name"] for m in text_resp if "name" in m]
        
        # 2. Fetch Image & Video Models
        img_vid_resp = requests.get("https://gen.pollinations.ai/image/models", timeout=10).json()
        
        image_models = []
        video_models = []
        
        for m in img_vid_resp:
            model_id = m.get("name")
            if not model_id: continue
            
            # FIXED LOGIC: Detect video models via output_modalities array
            out_modalities = m.get("output_modalities", [])
            if "video" in out_modalities:
                video_models.append(model_id)
            else:
                image_models.append(model_id)
                
        # Safety defaults to ensure nodes don't break if API is empty
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

    def replace_md_list(section_id, new_list, text):
        """Surgically replaces the bulleted list in the README based on section headers."""
        escaped_id = re.escape(section_id)
        # Matches from header + Supported Models line until the Parameters line or section break
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
        # 1. Add everything (Includes new folders: images/, workflows/)
        subprocess.run(["git", "add", "."], cwd=REPO_DIR)
        
        # 2. Check if there are actually changes to commit
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=REPO_DIR)
        if not status.stdout.strip():
            print("   ✅ Local state matches previous commit. No push needed.")
            return

        # 3. Create the commit
        date_str = datetime.now().strftime("%Y-%m-%d")
        subprocess.run(["git", "commit", "-m", f"Auto-Sync: Models, Assets, and Workflows ({date_str})"], cwd=REPO_DIR)
        
        # 4. Pull first to resolve any cloud-side changes (Force our version)
        print("   Merging cloud changes...")
        subprocess.run(["git", "pull", "origin", "main", "-X", "ours", "--no-edit"], cwd=REPO_DIR)
        
        # 5. Push to GitHub
        print("   Pushing to GitHub (origin)...")
        subprocess.run(["git", "push", "origin", "main"], cwd=REPO_DIR)
        
        # 6. Push to HuggingFace
        print("   Pushing to HuggingFace...")
        subprocess.run(["git", "push", "huggingface", "main", "--force"], cwd=REPO_DIR)
        
        print("🎉 Full sync complete! All folders and models are now live.")
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