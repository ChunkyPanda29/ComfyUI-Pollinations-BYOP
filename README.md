# 🌸 ComfyUI-Pollinations-BYOP

[![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom_Node-blue)](https://github.com/comfyanonymous/ComfyUI)
[![Pollinations.ai](https://img.shields.io/badge/API-Pollinations.ai-pink)](https://pollinations.ai/)
[![Pollinations GitHub](https://img.shields.io/badge/Source-Pollinations_Repo-black)](https://github.com/pollinations/pollinations)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

The latest ComfyUI custom node suite for **[Pollinations.ai](https://pollinations.ai/)** with full **BYOP (Bring Your Own Pollen)** support. 

Generate high-quality images, text, videos and audio using state-of-the-art models (like **Flux**, **DeepSeek**, and **Wan 2.6**) directly inside ComfyUI—**without using any of your local GPU VRAM.** 

Whether you are running on an 8GB laptop or a cloud server, this node suite offloads the heavy compute lifting to the Pollinations API.

---

## ✨ Features
* **Zero Local VRAM Required:** Generation happens entirely in the cloud.
* **Multimodal Generation:** Create Images, Videos, Audio and Text all from within your node tree.
* **BYOP Support:** Seamlessly integrate your Pollinations API Key to use your own "Pollen" quota, bypassing anonymous rate limits and supporting the ecosystem.
* **Lightning Fast:** Outputs load directly as standard ComfyUI `IMAGE` and `STRING` formats, ready for immediate downstream processing (Upscaling, I2V, Compositing).

---

## 🧩 Nodes Included & Supported Models

### 1. 🌸🖼️ Pollinations Image Gen (BYOP)
Generates high-fidelity images directly to a ComfyUI `IMAGE` tensor.
* **Supported Models:** 
  * `Catniti/agnes-image-2.1-flash`
  * `JustScriptzz/phoenix-1.0`
  * `MarcosFRG/flux-1-schnell`
  * `MarcosFRG/flux-2-klein-4b`
  * `MarcosFRG/lucid-origin`
  * `MarcosFRG/lucid-origin:paid 💎`
  * `MarcosFRG/phoenix-1.0`
  * `MarcosFRG/phoenix-1.0:paid 💎`
  * `MarcosFRG/sdxl-lightning`
  * `NamanSoni78/Imagine-4`
  * `NamanSoni78/Z-Image-Turbo 💎`
  * `alibaba/wan-2.7-image 💎`
  * `alibaba/wan-2.7-image-pro 💎`
  * `amazon/nova-canvas-v1`
  * `black-forest-labs/flux.1-kontext-pro`
  * `black-forest-labs/flux.1-schnell`
  * `black-forest-labs/flux.2-flex 💎`
  * `black-forest-labs/flux.2-klein-4b`
  * `black-forest-labs/flux.2-pro 💎`
  * `bytedance/seedream-4.0 💎`
  * `bytedance/seedream-4.5 💎`
  * `bytedance/seedream-5.0-lite 💎`
  * `bytedance/seedream-5.0-pro 💎`
  * `chigwell/gpt-image-2 💎`
  * `google/gemini-2.5-flash-image 💎`
  * `google/gemini-3-pro-image 💎`
  * `google/gemini-3.1-flash-image 💎`
  * `google/gemini-3.1-flash-lite-image 💎`
  * `ideogram-ai/ideogram-v4-balanced 💎`
  * `ideogram-ai/ideogram-v4-quality 💎`
  * `ideogram-ai/ideogram-v4-turbo 💎`
  * `krea/krea-2-medium 💎`
  * `lykon/dreamshaper-8-lcm`
  * `microsoft/mai-image-2.5-flash`
  * `openai/gpt-image-1-mini`
  * `openai/gpt-image-1.5`
  * `openai/gpt-image-2`
  * `openai/gpt-image-2.5-flare 💎`
  * `openai/gpt-image-2.5-sunburst 💎`
  * `prunaai/p-image 💎`
  * `prunaai/p-image-edit 💎`
  * `qwen/qwen-image 💎`
  * `qwen/qwen-image-3 💎`
  * `recraft/recraft-v4.1-vector 💎`
  * `rekty/rekty-dev-3 💎`
  * `rekty/rekty-dev-v2 💎`
  * `sharktide/gpt-image-2.5-flare-input-cheap 💎`
  * `sharktide/gpt-image-2.5-sunburst-input-cheap 💎`
  * `sharktide/inferenceport-ai-gpt-image-2.5-flare 💎`
  * `sharktide/inferenceport-ai-gpt-image-2.5-sunburst 💎`
  * `sharktide/inferenceport-ai-gpt-image-router 💎`
  * `sharktide/inferenceport-ai-image-ultra 💎`
  * `sharktide/inferenceport-ai-lightning-image-plus`
  * `tongyi-mai/z-image-turbo`
  * `vendouple/anima`
  * `vendouple/animagine`
  * `vendouple/lucid-origin`
  * `vendouple/luma-photon-1`
  * `vendouple/qwen-image-3.0-pro 💎`
  * `vendouple/uncensored-image-v2`
  * `x-ai/grok-imagine-image 💎`
  * `x-ai/grok-imagine-image-2.0 💎`
  * `x-ai/grok-imagine-image-quality 💎`
* **Parameters:** `prompt`, `model`, `width`, `height`, `seed`, `api_key`, `negative_prompt`

### 2. 🌸🎞️ Pollinations Video Gen (BYOP)
Generates high-quality AI video.
* **Supported Models:**
  * `NamanSoni78/Seedance-2.5`
  * `alibaba/happyhorse-1.1 💎`
  * `alibaba/wan-2.2-fast 💎`
  * `alibaba/wan-2.6 💎`
  * `alibaba/wan-2.7 💎`
  * `alibaba/wan-3.0 💎`
  * `amazon/nova-reel-v1`
  * `bytedance/seedance-1-pro-fast 💎`
  * `bytedance/seedance-2.0 💎`
  * `bytedance/seedance-2.0-fast 💎`
  * `bytedance/seedance-2.0-mini 💎`
  * `bytedance/seedance-2.5 💎`
  * `google/gemini-omni-1.1-flash 💎`
  * `google/veo-3.1-fast 💎`
  * `minimax/minimax-h3 💎`
  * `minimax/minimax-h3-max-turbo 💎`
  * `prunaai/p-video 💎`
  * `x-ai/grok-imagine-video 💎`
  * `x-ai/grok-imagine-video-1.5 💎`
* **Parameters:** `prompt`, `model`, `seed`, `api_key`

### 3. 🌸🤖 Pollinations Text Gen (BYOP)
Leverage top-tier LLMs for prompt expansion, dynamic tagging, or scriptwriting inside your workflow.
* **Supported Models:**
  * `AkshayCoder48/L3-70B-Euryale-v2.1`
  * `AkshayCoder48/Lorbus-Qwen3.6-27B-int4-AutoRound`
  * `AkshayCoder48/Nemo`
  * `AkshayCoder48/Qwen3.5-9B-Q4_K_M.gguf`
  * `AkshayCoder48/chat-model-reasoning`
  * `AkshayCoder48/chat-model-reasoning-with-search`
  * `AkshayCoder48/chatgpt`
  * `AkshayCoder48/chatgpt-search`
  * `AkshayCoder48/claude-fable-5`
  * `AkshayCoder48/claude-opus-4-8`
  * `AkshayCoder48/claude-opus-5`
  * `AkshayCoder48/claude-search`
  * `AkshayCoder48/claude-sonnet-5`
  * `AkshayCoder48/code-pair`
  * `AkshayCoder48/cohere-north-mini-code:free`
  * `AkshayCoder48/deepseek-search`
  * `AkshayCoder48/deepseek-v4-pro`
  * `AkshayCoder48/free-clips 💎`
  * `AkshayCoder48/free-voice`
  * `AkshayCoder48/gemini`
  * `AkshayCoder48/gemini-2.5-flash`
  * `AkshayCoder48/gemini-3-flash`
  * `AkshayCoder48/gemini-3.1-flash-lite`
  * `AkshayCoder48/gemini-3.6-flash`
  * `AkshayCoder48/gemini-search`
  * `AkshayCoder48/glm-5-2`
  * `AkshayCoder48/gpt-4o-latest`
  * `AkshayCoder48/gpt-5-4`
  * `AkshayCoder48/gpt-5-5`
  * `AkshayCoder48/gpt-5-6-luna`
  * `AkshayCoder48/gpt-5.4-mini-no-login`
  * `AkshayCoder48/gpt-5.6-sol`
  * `AkshayCoder48/gpt-o4-mini-no-login`
  * `AkshayCoder48/grok-4-3`
  * `AkshayCoder48/grok-search`
  * `AkshayCoder48/jollygen`
  * `AkshayCoder48/kilo-auto-free`
  * `AkshayCoder48/kilo-auto-small`
  * `AkshayCoder48/kimi-k3`
  * `AkshayCoder48/llama3-8b`
  * `AkshayCoder48/meta`
  * `AkshayCoder48/meta-search`
  * `AkshayCoder48/midnight-rose`
  * `AkshayCoder48/perplexity`
  * `AkshayCoder48/perplexity-search`
  * `AkshayCoder48/poolside-laguna-s-2.1:free`
  * `AkshayCoder48/prompt-to-art 💎`
  * `AkshayCoder48/qwen`
  * `AkshayCoder48/qwen3-coder-480b`
  * `AkshayCoder48/researcher 💎`
  * `AkshayCoder48/transcriber`
  * `AkshayCoder48/v3`
  * `AkshayCoder48/vexa`
  * `Bakhshi7889/gemma-4-31b-it`
  * `Catniti/auto-router-1`
  * `Catniti/claude-sonnet-5`
  * `Catniti/gemma-4-31b`
  * `Catniti/gpt-oss-120b`
  * `Catniti/qwen3.7-flash`
  * `Circuit-Overtime/OreoLook`
  * `CloudCompile/moondream3.1`
  * `JustScriptzz/agnes-2.5-flash`
  * `JustScriptzz/deepseek-v4-pro`
  * `JustScriptzz/glm-5-2`
  * `JustScriptzz/gpt-oss-120b`
  * `JustScriptzz/grok-4.6`
  * `JustScriptzz/kimi-k2-7-code`
  * `JustScriptzz/kimi-k3`
  * `JustScriptzz/moondream-3.1`
  * `Lorodn4x/claude-sonnet-5 💎`
  * `Lorodn4x/deepseek-v4-pro-0813`
  * `Lorodn4x/minimax-m3`
  * `MarcosFRG/deepseek-v4-flash-0731`
  * `MarcosFRG/deepseek-v4-flash-0731:paid 💎`
  * `MarcosFRG/deepseek-v4-pro-0813`
  * `MarcosFRG/gemini-2.5-flash-lite`
  * `MarcosFRG/gemini-2.5-flash-lite:paid 💎`
  * `MarcosFRG/gemini-3-flash-preview`
  * `MarcosFRG/gemini-3.1-flash-lite`
  * `MarcosFRG/gemini-3.1-pro-preview 💎`
  * `MarcosFRG/gemma-4-26b-a4b`
  * `MarcosFRG/gemma-4-26b-a4b:paid 💎`
  * `MarcosFRG/gemma-4-31b`
  * `MarcosFRG/gemma-4-31b:paid 💎`
  * `MarcosFRG/glm-4.6v-flash`
  * `MarcosFRG/glm-5.3`
  * `MarcosFRG/glm-5.3-flash`
  * `MarcosFRG/metraxai`
  * `MarcosFRG/mimo-v2.5`
  * `MarcosFRG/moondream-3.1`
  * `MarcosFRG/nemotron-3.5-lightning 💎`
  * `MarcosFRG/north-mini-code`
  * `MarcosFRG/qwen3.8-27b`
  * `MarcosFRG/qwen3.8-27b:paid 💎`
  * `MarcosFRG/qwen3.8-flash`
  * `MarcosFRG/qwen3.8-flash:paid 💎`
  * `Minor-fun/deepseek-v3.2`
  * `Minor-fun/gemma-4-31B-it`
  * `NamanSoni78/Claude-Fable-5.1`
  * `NamanSoni78/Claude-Sonnet-5`
  * `NamanSoni78/deepseek-v4-flash-0731`
  * `NamanSoni78/deepseek-v4-pro-0813`
  * `NamanSoni78/devin-ai`
  * `NamanSoni78/gemini-3.8-flash`
  * `NamanSoni78/gpt-5.4-nano`
  * `NamanSoni78/gpt-6-astra`
  * `NamanSoni78/kimi-k3`
  * `NamanSoni78/nemotron-3-ultra-550b-a55b`
  * `Spit-fires/muse-glimmer`
  * `YoannDev90/muse-glimmer-30b:free`
  * `YoannDev90/poolside-laguna-s-2.1:free`
  * `amazon/nova-2-lite-v1`
  * `amazon/nova-micro-v1`
  * `anthropic/claude-fable-5 💎`
  * `anthropic/claude-fable-5.1 💎`
  * `anthropic/claude-haiku-4.5 💎`
  * `anthropic/claude-opus-4.6 💎`
  * `anthropic/claude-opus-4.7 💎`
  * `anthropic/claude-opus-5 💎`
  * `anthropic/claude-sonnet-4.6 💎`
  * `anthropic/claude-sonnet-5 💎`
  * `chigwell/claude-fable-5 💎`
  * `chigwell/claude-fable-5-1 💎`
  * `chigwell/claude-haiku-4-5`
  * `chigwell/claude-opus-4-8 💎`
  * `chigwell/claude-opus-5 💎`
  * `chigwell/claude-sonnet-4-6 💎`
  * `chigwell/claude-sonnet-5 💎`
  * `chigwell/gemini-3-flash 💎`
  * `chigwell/gemini-3.1-flash-lite 💎`
  * `chigwell/gemini-3.5-flash-low 💎`
  * `chigwell/gemini-3.7-flash 💎`
  * `chigwell/gemini-3.8-flash-high 💎`
  * `chigwell/glm-5.3 💎`
  * `chigwell/gpt-5.5 💎`
  * `chigwell/gpt-5.6-sol 💎`
  * `chigwell/gpt-5.6-terra 💎`
  * `chigwell/gpt-6-astra 💎`
  * `chigwell/grok-4.5 💎`
  * `chigwell/grok-4.6 💎`
  * `chigwell/kimi-k3 💎`
  * `chigwell/llm7-fast`
  * `chigwell/llm7-pro 💎`
  * `chigwell/minimax-m2.7 💎`
  * `cohere/command-a-plus`
  * `deepseek/deepseek-v4-flash`
  * `deepseek/deepseek-v4-flash-vision-exp`
  * `deepseek/deepseek-v4-pro`
  * `gggff123/Gemini-3.7-Flash`
  * `gggff123/Glm-5.3`
  * `gggff123/Inkling`
  * `gggff123/gpt-5-nano`
  * `gggff123/step-3.7-flash`
  * `google/gemini-2.5-flash-lite 💎`
  * `google/gemini-2.5-flash-lite:search 💎`
  * `google/gemini-3-flash-preview 💎`
  * `google/gemini-3.1-pro-preview 💎`
  * `google/gemini-3.5-flash-lite 💎`
  * `google/gemini-3.7-flash 💎`
  * `google/gemini-3.8-flash 💎`
  * `google/gemma-4-26b-a4b-it 💎`
  * `google/gemma-4-31b-it 💎`
  * `immature-yt/alara-nova-1`
  * `inception/mercury-2 💎`
  * `inception/mercury-2.5-preview 💎`
  * `iotserver24/deepseek-fast`
  * `iotserver24/deepseek-v4f`
  * `iotserver24/glm-5.3 💎`
  * `iotserver24/kimi-k3 💎`
  * `iotserver24/route-r3ap3r`
  * `iotserver24/stealth-code`
  * `meituan/longcat-2.0 💎`
  * `meta/llama-3.3-70b-instruct`
  * `meta/llama-4-maverick 💎`
  * `meta/llama-4-scout 💎`
  * `meta/muse-glimmer-30b`
  * `meta/muse-spark-1.2 💎`
  * `mikl-shortcuts/ministral-3`
  * `minimax/minimax-m2.7 💎`
  * `minimax/minimax-m3`
  * `mistralai/mistral-large-3`
  * `mistralai/mistral-small-3.2 💎`
  * `mistralai/mistral-small-4 💎`
  * `moonshotai/kimi-k2.6`
  * `moonshotai/kimi-k2.7-code`
  * `moonshotai/kimi-k3`
  * `morriszdweck/osaii-api-fast`
  * `morriszdweck/osaii-api-smart`
  * `morriszdweck/osaii-swarm`
  * `novastardev/olmo-3.1-32b`
  * `nvidia/nemotron-3-ultra 💎`
  * `nvidia/nemotron-3.5-lightning`
  * `openai/gpt-5-nano`
  * `openai/gpt-5.4`
  * `openai/gpt-5.4-mini`
  * `openai/gpt-5.4-nano`
  * `openai/gpt-5.5`
  * `openai/gpt-5.6-luna`
  * `openai/gpt-5.6-sol`
  * `openai/gpt-5.6-terra`
  * `openai/gpt-6-astra`
  * `openai/gpt-audio-1.5`
  * `openai/gpt-audio-mini`
  * `openai/gpt-oss-20b`
  * `pegalink/gemini-3.1-pro-preview 💎`
  * `pegalink/gemini-3.5-flash-lite`
  * `pegalink/gemini-3.8-flash 💎`
  * `pegalink/gemini-pro-coder 💎`
  * `perplexity/sonar`
  * `perplexity/sonar-pro`
  * `perplexity/sonar-reasoning-pro`
  * `pollinations/midijourney`
  * `pollinations/midijourney-large`
  * `poolside/laguna-s-2.1 💎`
  * `qwen/qwen3-coder-30b-a3b-instruct`
  * `qwen/qwen3-coder-next 💎`
  * `qwen/qwen3-vl-235b-a22b-thinking 💎`
  * `qwen/qwen3-vl-30b-a3b-instruct 💎`
  * `qwen/qwen3.7-flash 💎`
  * `qwen/qwen3.7-max 💎`
  * `qwen/qwen3.7-plus 💎`
  * `qwen/qwen3.8-2.4t-a95b`
  * `qwen/qwen3.8-27b 💎`
  * `qwen/qwen3.8-flash 💎`
  * `qwen/qwen3.8-max 💎`
  * `qwen/qwen3.8-max-0902 💎`
  * `qwen/qwen3guard-gen-8b`
  * `sharktide/inferenceport-ai-codestral-2508`
  * `sharktide/inferenceport-ai-command-r-plus`
  * `sharktide/inferenceport-ai-gemini-2.5-flash`
  * `sharktide/inferenceport-ai-kimi-k2.7-code`
  * `sharktide/inferenceport-ai-lightning-text-v2`
  * `sharktide/inferenceport-ai-minimax-m3`
  * `sharktide/inferenceport-ai-qwen-3.6-27b`
  * `sharktide/inferenceport.ai-gpt-oss-20b`
  * `smplstuff/falcon-h1-tiny`
  * `smplstuff/title-generator`
  * `stepfun/step-3.5-flash 💎`
  * `stepfun/step-3.7-flash 💎`
  * `thinkingmachines/inkling 💎`
  * `thinkingmachines/inkling-small 💎`
  * `tomdacatto/claude-haiku-4.5`
  * `tomdacatto/claude-opus-4-6`
  * `tomdacatto/claude-opus-4-7`
  * `tomdacatto/claude-opus-5`
  * `tomdacatto/claude-sonnet-5`
  * `tomdacatto/ezra`
  * `tomdacatto/fable-5.1`
  * `tomdacatto/gpt-6-astra`
  * `tomdacatto/llama-3.1-8B`
  * `tomdacatto/muse-spark-1.3-contributor`
  * `tomdacatto/muse-spark-1.3-contributor-paid 💎`
  * `tomdacatto/qwen-3.8-27B-fast`
  * `vendouple/deepseek-v3.2`
  * `vendouple/deepseek-v4-flash`
  * `vendouple/deepseek-v4-pro`
  * `vendouple/gemini-3.8-flash`
  * `vendouple/gemma-4-31b-sdft-heretic-rp`
  * `vendouple/glm-5.3`
  * `vendouple/gpt-5.6-luna`
  * `vendouple/gpt-5.6-sol`
  * `vendouple/gpt-6-astra`
  * `vendouple/grok-4.6`
  * `vendouple/kimi-k2.6`
  * `vendouple/kimi-k3`
  * `vendouple/muse-glimmer-30b:free`
  * `vendouple/qwen-3.8-max`
  * `voodoohop/airforce-doubao-pro`
  * `voodoohop/airforce-qwen3-max`
  * `voodoohop/anyvm-deepseek-chat`
  * `voodoohop/email-overview 💎`
  * `x-ai/grok-4.20`
  * `x-ai/grok-4.3`
  * `x-ai/grok-4.6`
  * `xiaomi/mimo-v2.5 💎`
  * `xiaomi/mimo-v2.5-pro 💎`
  * `z-ai/glm-5.2`
  * `z-ai/glm-5.3`
  * `z-ai/glm-5.3-flash`
  * `zero2launch/gemini-3.6-flash 💎`
  * `zero2launch/gemini-3.7-flash`
* **Parameters:** `prompt`, `system_instruction`, `model`, `temperature`, `seed`, `api_key`

### 4.🌸🔊 Pollinations Audio Gen (BYOP)
Text-to-speech, music generation, and audio transcription.
* **Supported Models:**
  * `NamanSoni78/aura-2-amalthea-en`
  * `NamanSoni78/aura-2-atlas-en`
  * `NamanSoni78/aura-2-orpheus-en`
  * `NamanSoni78/aura-2-thalia-en`
  * `NamanSoni78/nova-3`
  * `NamanSoni78/whisper-large-v3`
  * `NamanSoni78/whisper-large-v3-turbo`
  * `assemblyai/universal-2`
  * `assemblyai/universal-3.5-pro`
  * `elevenlabs/eleven-flash-v2.5 💎`
  * `elevenlabs/eleven-multilingual-sts-v2 💎`
  * `elevenlabs/eleven-multilingual-v2 💎`
  * `elevenlabs/eleven-text-to-sound-v2 💎`
  * `elevenlabs/eleven-v3 💎`
  * `elevenlabs/eleven-v3:dialogue 💎`
  * `elevenlabs/music-v2 💎`
  * `elevenlabs/scribe-v2 💎`
  * `elevenlabs/voice-isolator 💎`
  * `fish-audio/s2.1-pro 💎`
  * `google/lyria-3-clip-preview 💎`
  * `hexgrad/kokoro-82m 💎`
  * `openai/gpt-transcribe`
  * `openai/whisper-large-v3`
  * `qwen/qwen3-tts-flash 💎`
  * `qwen/qwen3-tts-instruct-flash 💎`
  * `sesame/csm-1b 💎`
  * `stability-ai/stable-audio-3 💎`
  * `stability-ai/stable-audio-3-medium 💎`
  * `x-ai/grok-transcribe 💎`
  * `x-ai/grok-tts 💎`
---

## 📸 Screenshots

![🌸🖼️ Pollinations Image Gen](images/Pollinations_Image_Gen_(BYOP).png) 

![🌸🎞️ Pollinations Video Gen](images/Pollinations_Video_Gen_URL_(BYOP).png)

![🌸🤖 Pollinations Text Gen](images/Pollinations_Text_Gen_(BYOP).png) 
 
![🌸🔊 Pollinations Audio Gen](images/Pollinations_Audio_Gen_(BYOP).png)  

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

## 🔐 Official BYOP (Bring Your Own Pollen) Integration

This node suite implements the official [Pollinations BYOP specification](https://github.com/pollinations/pollinations/blob/main/BRING_YOUR_OWN_POLLEN.md) with support for:

- ✅ **Device Code Flow** - Browser-free authentication for headless/CLI environments
- ✅ **App Key Attribution** - Track your app's traffic for tier upgrades
- ✅ **User Info Retrieval** - Display username, email, and balance

---

## 🔑 How to get your API Key (BYOP)

Pollinations operates on a unique **"Pollen"** economy. While anonymous generation is free, it is heavily rate-limited. By using your own API key, you unlock your personal daily/weekly free Pollen grants, allowing for faster and more consistent generation.

### Method 1: BYOP Login Node (Recommended)
The easiest way - no copy/pasting keys!

1. Add the **🔐🌸 Pollinations BYOP Login** node to your workflow
2. Toggle **"Click to Login"** → the node will show you a URL and code
3. Go to the URL on any device and enter the code
4. Return to ComfyUI - your key is now saved automatically!

### Method 2: Manual Key Entry
1. Go to **[enter.pollinations.ai](https://enter.pollinations.ai/)**.
2. Sign in using your Discord or Google account.
3. Once logged in, your API key will be visible on your dashboard.
4. Copy the key and paste it into the `api_key` field of the ComfyUI node.
5. *That's it! Your ComfyUI workflow is now fueled by your own Pollen.*

---

## 🔐 API Key Configuration (Set Once)

You no longer need to paste your API Key into every node. You have three ways to set it:

### Method 1: ComfyUI Settings Menu (Easiest)
1. Open ComfyUI.
2. Click the **Settings** (gear icon) in the ComfyUI menu.
3. Scroll down to the **"Pollinations (BYOP)"** section.
4. Paste your API key into the textbox. 
5. The key is now saved locally and will be used automatically by all Pollinations nodes!

### Method 2: Environment Variable
Set an environment variable on your system (useful for cloud servers like RunPod):
`POLLINATIONS_API_KEY=sk_your_key_here`

### Method 3: Node-Level Override
If you want to use a different key for a specific node, just paste it into the `api_key` field on the node itself. This will always take priority over global settings.

---

## ❓ FAQ

**Q: Does this cost money?**  
**A:** No! Pollinations provides free anonymous generations, and every registered user receives a free allowance of "Pollen" every week. You only pay if you decide to use the Paid Models 💎 or scale up massively and buy extra Pollen.

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
