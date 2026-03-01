# 🌸 ComfyUI-Pollinations-BYOP

[![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom_Node-blue)](https://github.com/comfyanonymous/ComfyUI)
[![Pollinations.ai](https://img.shields.io/badge/API-Pollinations.ai-pink)](https://pollinations.ai/)
[![Pollinations GitHub](https://img.shields.io/badge/Source-Pollinations_Repo-black)](https://github.com/pollinations/pollinations)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

The official ComfyUI custom node suite for **[Pollinations.ai](https://pollinations.ai/)** with full **BYOP (Bring Your Own Pollen)** support. 

Generate high-quality images, text, and videos using state-of-the-art models (like **Flux**, **DeepSeek**, and **Wan 2.6**) directly inside ComfyUI—**without using any of your local GPU VRAM.** 

Whether you are running on an 8GB laptop or a cloud server, this node suite offloads the heavy compute lifting to the Pollinations API.

---

## ✨ Features
* **Zero Local VRAM Required:** Generation happens entirely in the cloud.
* **Multimodal Generation:** Create Images, Videos, and Text all from within your node tree.
* **BYOP Support:** Seamlessly integrate your Pollinations API Key to use your own "Pollen" quota, bypassing anonymous rate limits and supporting the ecosystem.
* **Lightning Fast:** Outputs load directly as standard ComfyUI `IMAGE` and `STRING` formats, ready for immediate downstream processing (Upscaling, I2V, Compositing).

---

## 🧩 Nodes Included & Supported Models

### 1. 🌸 Pollinations Image Gen (BYOP)
Generates high-fidelity images directly to a ComfyUI `IMAGE` tensor.
* **Supported Models:** 
  * `flux`
  * `gptimage`
  * `gptimage-large 💎`
  * `grok-imagine`
  * `imagen-4`
  * `klein`
  * `klein-large`
  * `kontext 💎`
  * `nanobanana 💎`
  * `nanobanana-pro 💎`
  * `seedream 💎`
  * `seedream-pro 💎`
  * `zimage`
* **Parameters:** `prompt`, `model`, `width`, `height`, `seed`, `api_key`, `negative_prompt`

### 2. 🌸 Pollinations Video Gen (BYOP)
Generates high-quality AI video.
* **Supported Models:**
  * `grok-video`
  * `ltx-2 💎`
  * `seedance`
  * `seedance-pro 💎`
  * `veo 💎`
  * `wan 💎`
* **Parameters:** `prompt`, `model`, `seed`, `api_key`

### 3. 🌸 Pollinations Text Gen (BYOP)
Leverage top-tier LLMs for prompt expansion, dynamic tagging, or scriptwriting inside your workflow.
* **Supported Models:**
  * `claude 💎`
  * `claude-fast`
  * `claude-large 💎`
  * `deepseek`
  * `gemini 💎`
  * `gemini-fast`
  * `gemini-large 💎`
  * `gemini-search`
  * `glm`
  * `grok 💎`
  * `kimi`
  * `midijourney`
  * `minimax`
  * `mistral`
  * `nomnom`
  * `nova-fast`
  * `openai`
  * `openai-audio`
  * `openai-fast`
  * `openai-large`
  * `perplexity-fast`
  * `perplexity-reasoning`
  * `polly`
  * `qwen-character`
  * `qwen-coder`
  * `qwen-safety`
* **Parameters:** `prompt`, `system_instruction`, `model`, `temperature`, `seed`, `api_key`

---

## 📸 Screenshots

![🌸🖼️ Pollinations Image Gen](images/Pollinations_Image_Gen_(BYOP).png) 

![🌸🤖 Pollinations Text Gen](images/Pollinations_Text_Gen_(BYOP).png) 

![🌸🎞️ Pollinations Video Gen](images/Pollinations_Video_Gen_URL_(BYOP).png) 
   
---

## ⚙️ Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open the **ComfyUI Manager**.
2. Click **Install Custom Nodes**.
3. Search for `Pollinations BYOP`.
4. Click Install and restart ComfyUI.

### Method 2: Manual Git Clone
1. Navigate to your ComfyUI `custom_nodes` directory in your terminal:
   ```bash
   cd ComfyUI/custom_nodes
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/ChunkyPanda29/ComfyUI-Pollinations-BYOP.git
   ```
3. Restart ComfyUI.

---

## 🛠️ How to Use

1. Double-click your ComfyUI canvas and search for **`Pollinations`**.
2. Select your desired node (**Image**, **Video**, or **Text**).
3. **prompt:** Enter your creative description.
4. **model:** Select your desired engine from the dropdown list.
5. **api_key (Optional but Recommended):** Paste your Pollinations API key here (See instructions below).
6. Connect the output to a **Save Image**, **Video Combine**, or **Show Text** node.
7. Click **Queue Prompt**!

---

## 🔑 How to get your API Key (BYOP)

Pollinations operates on a unique **"Pollen"** economy. While anonymous generation is free, it is heavily rate-limited. By using your own API key, you unlock your personal daily/weekly free Pollen grants, allowing for faster and more consistent generation.

1. Go to **[enter.pollinations.ai](https://enter.pollinations.ai/)**.
2. Sign in using your Discord or Google account.
3. Once logged in, your API key will be visible on your dashboard.
4. Copy the key and paste it into the `api_key` field of the ComfyUI node.
5. *That's it! Your ComfyUI workflow is now fueled by your own Pollen.*

---

## ❓ FAQ

**Q: Does this cost money?**  
**A:** No! Pollinations provides free anonymous generations, and every registered user receives a free allowance of "Pollen" every week. You only pay if you decide to scale up massively and buy extra Pollen.

**Q: Why does my generation fail or timeout?**  
**A:** If you are leaving the `api_key` field blank, you are using the anonymous public tier, which can experience high traffic or strict rate limits. **Adding your free API key solves this.**

**Q: Does this download large models to my hard drive?**  
**A:** No. This is a pure API node. Your local installation size will remain exactly the same, making it perfect for budget 8GB VRAM setups.

**Q: Can I chain these nodes together?**  
**A:** Yes! A popular workflow is to use the **Text Gen** node to expand a simple idea into a highly detailed visual prompt, then feed that string directly into the **Image Gen** node, and finally pass that image output into a Video generation node.

---

## 🤝 Contributing
Feel free to submit pull requests or open issues! Devs who contribute to Pollinations integrations can earn "Dev Points" to unlock Seed Status and greater API limits.
```
