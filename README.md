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
  * `MarcosFRG/flux-1-schnell`
  * `MarcosFRG/flux-1-schnell:paid 💎`
  * `MarcosFRG/flux-2-klein-4b`
  * `alibaba/wan-2.7-image 💎`
  * `alibaba/wan-2.7-image-pro 💎`
  * `aurora 💎`
  * `black-forest-labs/flux.1-kontext-pro`
  * `black-forest-labs/flux.1-schnell`
  * `black-forest-labs/flux.1.1-pro`
  * `black-forest-labs/flux.2-flex 💎`
  * `black-forest-labs/flux.2-klein-4b`
  * `black-forest-labs/flux.2-max 💎`
  * `black-forest-labs/flux.2-pro 💎`
  * `bytedance/seedream-4.0 💎`
  * `bytedance/seedream-4.5 💎`
  * `bytedance/seedream-5.0-lite 💎`
  * `bytedance/seedream-5.0-pro 💎`
  * `chigwell/gpt-image-2 💎`
  * `chigwell/gpt-image-2.5 💎`
  * `community/MarcosFRG/flux-1-schnell`
  * `community/MarcosFRG/flux-1-schnell:paid 💎`
  * `community/MarcosFRG/flux-2-klein-4b`
  * `community/chigwell/gpt-image-2 💎`
  * `community/chigwell/gpt-image-2.5 💎`
  * `community/rekty/rekty-dev-3 💎`
  * `community/rekty/rekty-dev-v2 💎`
  * `community/sharktide/gpt-image-2.5-flare-input-cheap 💎`
  * `community/sharktide/gpt-image-2.5-sunburst-input-cheap 💎`
  * `community/sharktide/inferenceport-ai-gpt-image-2.5-flare 💎`
  * `community/sharktide/inferenceport-ai-gpt-image-2.5-sunburst 💎`
  * `community/sharktide/inferenceport-ai-image-ultra 💎`
  * `community/sharktide/inferenceport-ai-lightning-image-plus`
  * `community/sharktide/inferenceport-ai-lightning-image-turbo`
  * `community/vendouple/anima 💎`
  * `community/vendouple/nano-banana-pro`
  * `community/vendouple/uncensored-image-v2`
  * `dreamshaper`
  * `flux`
  * `flux-2-flex 💎`
  * `flux-2-pro 💎`
  * `flux-klein`
  * `google/gemini-2.5-flash-image 💎`
  * `google/gemini-3-pro-image 💎`
  * `google/gemini-3.1-flash-image 💎`
  * `google/gemini-3.1-flash-lite-image 💎`
  * `gpt-image`
  * `gpt-image-1-mini`
  * `gpt-image-1.5`
  * `gpt-image-2`
  * `gpt-image-large`
  * `gptimage`
  * `gptimage-large`
  * `grok-aurora 💎`
  * `grok-imagine 💎`
  * `grok-imagine-image 💎`
  * `grok-imagine-image-2.0 💎`
  * `grok-imagine-image-pro 💎`
  * `grok-imagine-image-quality 💎`
  * `grok-imagine-pro 💎`
  * `ideogram-ai/ideogram-v4-balanced 💎`
  * `ideogram-ai/ideogram-v4-quality 💎`
  * `ideogram-ai/ideogram-v4-turbo 💎`
  * `ideogram-v4-balanced 💎`
  * `ideogram-v4-quality 💎`
  * `ideogram-v4-turbo 💎`
  * `inferenceport-ai/lightning-image-turbo 💎`
  * `klein`
  * `kontext`
  * `krea 💎`
  * `krea-2 💎`
  * `krea/krea-2-medium 💎`
  * `lykon/dreamshaper-8-lcm`
  * `microsoft/mai-image-2.5-flash`
  * `microsoft/mai-image-2.6`
  * `microsoft/mai-image-2.6-flash`
  * `nanobanana 💎`
  * `nanobanana-2 💎`
  * `nanobanana-2-lite 💎`
  * `nanobanana-lite 💎`
  * `nanobanana-pro 💎`
  * `nanobanana2 💎`
  * `nanobanana2lite 💎`
  * `openai/gpt-image-1-mini`
  * `openai/gpt-image-1.5`
  * `openai/gpt-image-2`
  * `openai/gpt-image-2.5-flare 💎`
  * `openai/gpt-image-2.5-sunburst 💎`
  * `p-image 💎`
  * `p-image-edit 💎`
  * `pruna 💎`
  * `pruna-edit 💎`
  * `pruna-image 💎`
  * `pruna-image-edit 💎`
  * `prunaai/p-image 💎`
  * `prunaai/p-image-edit 💎`
  * `qwen-image 💎`
  * `qwen-image-2512 💎`
  * `qwen-image-3 💎`
  * `qwen-image-edit 💎`
  * `qwen-image-edit-plus 💎`
  * `qwen-image-plus 💎`
  * `qwen/qwen-image 💎`
  * `qwen/qwen-image-2.1 💎`
  * `qwen/qwen-image-3 💎`
  * `recraft-svg 💎`
  * `recraft-v4.1-svg 💎`
  * `recraft-v4.1-vector 💎`
  * `recraft-vector 💎`
  * `recraft/recraft-v4.1-flash 💎`
  * `recraft/recraft-v4.1-vector 💎`
  * `rekty/rekty-dev-3 💎`
  * `rekty/rekty-dev-v2 💎`
  * `sana`
  * `seedream 💎`
  * `seedream-5-pro 💎`
  * `seedream-pro 💎`
  * `seedream-pro-5 💎`
  * `seedream5 💎`
  * `seedream5-pro 💎`
  * `sharktide/gpt-image-2.5-flare-input-cheap 💎`
  * `sharktide/gpt-image-2.5-sunburst-input-cheap 💎`
  * `sharktide/inferenceport-ai-gpt-image-2.5-flare 💎`
  * `sharktide/inferenceport-ai-gpt-image-2.5-sunburst 💎`
  * `sharktide/inferenceport-ai-image-ultra 💎`
  * `sharktide/inferenceport-ai-lightning-image-plus`
  * `sharktide/inferenceport-ai-lightning-image-turbo`
  * `tongyi-mai/z-image-turbo`
  * `vendouple/anima 💎`
  * `vendouple/nano-banana-pro`
  * `vendouple/uncensored-image-v2`
  * `wan-image 💎`
  * `wan-image-pro 💎`
  * `wan-img 💎`
  * `wan-img-pro 💎`
  * `wan2.7-image 💎`
  * `wan2.7-image-pro 💎`
  * `x-ai/grok-imagine-image 💎`
  * `x-ai/grok-imagine-image-2.0 💎`
  * `x-ai/grok-imagine-image-quality 💎`
  * `z-image`
  * `z-image-turbo`
  * `zimage`
* **Parameters:** `prompt`, `model`, `width`, `height`, `seed`, `api_key`, `negative_prompt`

### 2. 🌸🎞️ Pollinations Video Gen (BYOP)
Generates high-quality AI video.
* **Supported Models:**
  * `alibaba/happyhorse-1.1 💎`
  * `alibaba/wan-2.2-fast 💎`
  * `alibaba/wan-2.6 💎`
  * `alibaba/wan-2.7 💎`
  * `alibaba/wan-3.0 💎`
  * `bytedance/seedance-1-pro-fast 💎`
  * `bytedance/seedance-2.0 💎`
  * `bytedance/seedance-2.0-fast 💎`
  * `bytedance/seedance-2.0-mini 💎`
  * `bytedance/seedance-2.5 💎`
  * `google/gemini-omni-1.1-flash 💎`
  * `google/veo-3.1-fast 💎`
  * `grok-imagine-video 💎`
  * `grok-imagine-video-1.5 💎`
  * `grok-video-pro 💎`
  * `happy-horse-1.1 💎`
  * `happyhorse 💎`
  * `happyhorse-1.1 💎`
  * `heygen/heygen-video-1 💎`
  * `minimax-h3 💎`
  * `minimax/minimax-h3 💎`
  * `minimax/minimax-h3-max 💎`
  * `minimax/minimax-h3-max-turbo 💎`
  * `p-video 💎`
  * `p-video-1080p 💎`
  * `p-video-720p 💎`
  * `pruna-video 💎`
  * `pruna-video-1080p 💎`
  * `prunaai/p-video 💎`
  * `seedance-2 💎`
  * `seedance-2.0 💎`
  * `seedance-2.0-fast 💎`
  * `seedance-2.0-mini 💎`
  * `seedance-2.5 💎`
  * `seedance-pro 💎`
  * `veo 💎`
  * `veo-1080 💎`
  * `veo-1080p 💎`
  * `veo-3.1-fast 💎`
  * `veo-3.1-fast-1080p 💎`
  * `veo-720p 💎`
  * `video 💎`
  * `wan 💎`
  * `wan-2.2 💎`
  * `wan-2.7 💎`
  * `wan-3.0 💎`
  * `wan-fast 💎`
  * `wan-i2v 💎`
  * `wan-pro 💎`
  * `wan-pro-1080 💎`
  * `wan-pro-1080p 💎`
  * `wan2.2 💎`
  * `wan2.6 💎`
  * `wan2.7 💎`
  * `wan2.7-1080p 💎`
  * `x-ai/grok-imagine-video 💎`
  * `x-ai/grok-imagine-video-1.5 💎`
* **Parameters:** `prompt`, `model`, `seed`, `api_key`

### 3. 🌸🤖 Pollinations Text Gen (BYOP)
Leverage top-tier LLMs for prompt expansion, dynamic tagging, or scriptwriting inside your workflow.
* **Supported Models:**
  * `AkshayCoder48/code-pair`
  * `AkshayCoder48/free-clips 💎`
  * `AkshayCoder48/free-voice`
  * `AkshayCoder48/prompt-to-art 💎`
  * `AkshayCoder48/researcher 💎`
  * `Catniti/agnes-3.0-flash`
  * `Catniti/catniti-ai-agent`
  * `Catniti/nemotron-3.5-lightning`
  * `CloudCompile/pollinations-code-agent-but-weird`
  * `Creatneworld/catgpt-comic 💎`
  * `Creatneworld/lamplighter 💎`
  * `Creatneworld/pen`
  * `Creatneworld/sirius-elevator-descent 💎`
  * `Guest453/show-your-work`
  * `JustScriptzz/gpt-oss-120b`
  * `MarcosFRG/deepseek-v4-flash-0731`
  * `MarcosFRG/deepseek-v4-flash-0731:paid 💎`
  * `MarcosFRG/gemini-3-flash-preview:paid 💎`
  * `MarcosFRG/gemma-4-26b-a4b:paid 💎`
  * `MarcosFRG/gemma-4-31b:paid 💎`
  * `MarcosFRG/glm-5.3-flash`
  * `MarcosFRG/gpt-6-astra:paid 💎`
  * `MarcosFRG/metraxai`
  * `MarcosFRG/minimax-m3:paid 💎`
  * `MarcosFRG/nemotron-3.5-lightning:paid 💎`
  * `MarcosFRG/qwen3.8-27b:paid 💎`
  * `Takax62/minimax-m3-429b-vml`
  * `YoannDev90/agentic-gt`
  * `YoannDev90/poolside-laguna-s-2.1:free`
  * `ZapGaming/llama3.1-8b-xturbo`
  * `afanasevmylife/gazette`
  * `afanasevmylife/polyrouter`
  * `aikhusus2025-ctrl/ember-perch`
  * `aikhusus2025-ctrl/sirius-elevator`
  * `aikhusus2025-ctrl/sirius-scorekeeper`
  * `amazon-nova-2-lite`
  * `amazon-nova-micro`
  * `amazon/nova-2-lite-v1`
  * `amazon/nova-micro-v1`
  * `anthropic/claude-fable-5 💎`
  * `anthropic/claude-fable-5.1 💎`
  * `anthropic/claude-haiku-4.5 💎`
  * `anthropic/claude-opus-4.6 💎`
  * `anthropic/claude-opus-4.7 💎`
  * `anthropic/claude-opus-5 💎`
  * `anthropic/claude-opus-5.5 💎`
  * `anthropic/claude-sonnet-4.6 💎`
  * `anthropic/claude-sonnet-5 💎`
  * `anthropic/claude-sonnet-5.5 💎`
  * `chatgpt-5.6-luna`
  * `chatgpt-5.6-sol`
  * `chatgpt-5.6-terra`
  * `chatgpt-luna`
  * `chatgpt-sol`
  * `chatgpt-terra`
  * `chigwell/gpt-6.1-sol 💎`
  * `chigwell/llm7-pro 💎`
  * `claude 💎`
  * `claude-fable-5 💎`
  * `claude-fast 💎`
  * `claude-haiku 💎`
  * `claude-haiku-4.5 💎`
  * `claude-large 💎`
  * `claude-opus 💎`
  * `claude-opus-4.5 💎`
  * `claude-opus-4.6 💎`
  * `claude-opus-4.7 💎`
  * `claude-opus-4.8 💎`
  * `claude-opus-5 💎`
  * `claude-sonnet 💎`
  * `claude-sonnet-4.6 💎`
  * `claude-sonnet-5 💎`
  * `cohere-command-a-plus`
  * `cohere-command-a-plus-05-2026`
  * `cohere/command-a-plus`
  * `command-a-plus`
  * `command-a-plus-05-2026`
  * `community/AkshayCoder48/code-pair`
  * `community/AkshayCoder48/free-clips 💎`
  * `community/AkshayCoder48/free-voice`
  * `community/AkshayCoder48/prompt-to-art 💎`
  * `community/AkshayCoder48/researcher 💎`
  * `community/Catniti/agnes-3.0-flash`
  * `community/Catniti/catniti-ai-agent`
  * `community/Catniti/nemotron-3.5-lightning`
  * `community/CloudCompile/pollinations-code-agent-but-weird`
  * `community/Creatneworld/catgpt-comic 💎`
  * `community/Creatneworld/lamplighter 💎`
  * `community/Creatneworld/pen`
  * `community/Creatneworld/sirius-elevator-descent 💎`
  * `community/Guest453/show-your-work`
  * `community/JustScriptzz/gpt-oss-120b`
  * `community/MarcosFRG/deepseek-v4-flash-0731`
  * `community/MarcosFRG/deepseek-v4-flash-0731:paid 💎`
  * `community/MarcosFRG/gemini-3-flash-preview:paid 💎`
  * `community/MarcosFRG/gemma-4-26b-a4b:paid 💎`
  * `community/MarcosFRG/gemma-4-31b:paid 💎`
  * `community/MarcosFRG/glm-5.3-flash`
  * `community/MarcosFRG/gpt-6-astra:paid 💎`
  * `community/MarcosFRG/metraxai`
  * `community/MarcosFRG/minimax-m3:paid 💎`
  * `community/MarcosFRG/nemotron-3.5-lightning:paid 💎`
  * `community/MarcosFRG/qwen3.8-27b:paid 💎`
  * `community/Takax62/minimax-m3-429b-vml`
  * `community/YoannDev90/agentic-gt`
  * `community/YoannDev90/poolside-laguna-s-2.1:free`
  * `community/ZapGaming/llama3.1-8b-xturbo`
  * `community/afanasevmylife/gazette`
  * `community/afanasevmylife/polyrouter`
  * `community/aikhusus2025-ctrl/ember-perch`
  * `community/aikhusus2025-ctrl/sirius-elevator`
  * `community/aikhusus2025-ctrl/sirius-scorekeeper`
  * `community/chigwell/gpt-6.1-sol 💎`
  * `community/chigwell/llm7-pro 💎`
  * `community/fadyabohamza-netizen/frugal`
  * `community/gggff123/Inkling`
  * `community/gggff123/gpt-5-nano`
  * `community/gggff123/step-3.7-flash`
  * `community/immature-yt/alara-nova-1`
  * `community/iotserver24/route-r3ap3r`
  * `community/iotserver24/supercharge`
  * `community/kreggscode/jev-test-triage`
  * `community/mikl-shortcuts/ministral-3`
  * `community/morriszdweck/osaii-api-smart`
  * `community/morriszdweck/osaii-swarm`
  * `community/pegalink/gemini-3.1-pro-preview 💎`
  * `community/pegalink/gemini-3.8-flash 💎`
  * `community/pegalink/gemini-pro-coder 💎`
  * `community/pegalink/hy4-preview-coding 💎`
  * `community/pollinations-ai/floret`
  * `community/pollinations-ai/midijourney`
  * `community/pollinations-ai/polli`
  * `community/scriptsnsenses-sys/diffusiongema-26B-free`
  * `community/scriptsnsenses-sys/gpt-5.6-sol-free`
  * `community/sharktide/3D-agent`
  * `community/sharktide/inferenceport-ai-gemini-2.5-flash`
  * `community/sharktide/inferenceport-ai-kimi-k2.7-code-deep-logician 💎`
  * `community/sharktide/inferenceport-ai-lightning-text-v2`
  * `community/sharktide/inferenceport-ai-lightning-text-v2-expanded-knowledge`
  * `community/sharktide/inferenceport-ai-lightning-text-v2.1 💎`
  * `community/sharktide/inferenceport-ai-mimo-v2.5 💎`
  * `community/sharktide/inferenceport-ai-minimax-m3 💎`
  * `community/sharktide/inferenceport-ai-qwen-3.8-27b`
  * `community/sharktide/inferenceport.ai-gpt-oss-20b`
  * `community/smplstuff/title-generator`
  * `community/tomdacatto/Humanish-Roleplay-Llama-3.1-8B 💎`
  * `community/tomdacatto/Qwen3.8-Flash-Next 💎`
  * `community/tomdacatto/ezra`
  * `community/tomdacatto/gotcha-scout`
  * `community/tomdacatto/llama-3.1-8B`
  * `community/tomdacatto/tiered-health-router`
  * `community/vendouple/deepseek-v4-flash`
  * `community/vendouple/glm-5.3-flash`
  * `community/vendouple/gpt-6-sol`
  * `community/vendouple/gpt-6-sol:stable 💎`
  * `community/vendouple/gpt-6.1-sol:stable 💎`
  * `community/voodoohop/airforce-doubao-pro`
  * `community/voodoohop/airforce-grok-4-fast`
  * `community/voodoohop/airforce-qwen3-max`
  * `community/voodoohop/catgpt-comic 💎`
  * `community/voodoohop/email-overview 💎`
  * `community/xiaotian1171/triage-router`
  * `deepseek`
  * `deepseek-flash`
  * `deepseek-lite`
  * `deepseek-pro 💎`
  * `deepseek-v4`
  * `deepseek-v4-flash`
  * `deepseek-v4-lite`
  * `deepseek-v4-pro 💎`
  * `deepseek/deepseek-v4-flash`
  * `deepseek/deepseek-v4-flash-vision-exp 💎`
  * `deepseek/deepseek-v4-pro 💎`
  * `deepseek/deepseek-v4.1-flash`
  * `fadyabohamza-netizen/frugal`
  * `gemini 💎`
  * `gemini-2.5-flash-lite 💎`
  * `gemini-2.5-flash-lite-search 💎`
  * `gemini-2.5-flash-search 💎`
  * `gemini-2.5-pro 💎`
  * `gemini-3-flash 💎`
  * `gemini-3-flash-preview 💎`
  * `gemini-3.1-flash-lite 💎`
  * `gemini-3.1-flash-lite-preview 💎`
  * `gemini-3.1-flash-lite-search 💎`
  * `gemini-3.1-pro 💎`
  * `gemini-3.5-flash 💎`
  * `gemini-3.5-flash-lite 💎`
  * `gemini-3.5-flash-lite-search 💎`
  * `gemini-3.5-flash-search 💎`
  * `gemini-3.6-flash 💎`
  * `gemini-3.6-flash-search 💎`
  * `gemini-fast 💎`
  * `gemini-flash-lite 💎`
  * `gemini-flash-lite-3.1 💎`
  * `gemini-flash-lite-3.5 💎`
  * `gemini-large 💎`
  * `gemini-search 💎`
  * `gemini-search-fast 💎`
  * `gemini-search-large 💎`
  * `gemma 💎`
  * `gemma-4 💎`
  * `gemma-4-26b 💎`
  * `gemma-4-26b-a4b 💎`
  * `gemma-4-26b-a4b-it 💎`
  * `gemma-4-31b 💎`
  * `gemma-4-31b-it 💎`
  * `gemma-large 💎`
  * `gggff123/Inkling`
  * `gggff123/gpt-5-nano`
  * `gggff123/step-3.7-flash`
  * `glm 💎`
  * `glm-5.2 💎`
  * `glm-5.3`
  * `glm-5p2 💎`
  * `google/gemini-2.5-flash-lite 💎`
  * `google/gemini-2.5-flash-lite:search 💎`
  * `google/gemini-3-flash-preview 💎`
  * `google/gemini-3.1-pro-preview 💎`
  * `google/gemini-3.5-flash-lite 💎`
  * `google/gemini-3.7-flash 💎`
  * `google/gemini-3.8-flash 💎`
  * `google/gemma-4-26b-a4b-it 💎`
  * `google/gemma-4-31b-it 💎`
  * `gpt-4o-mini-audio-preview`
  * `gpt-4o-mini-audio-preview-2024-12-17`
  * `gpt-5-mini`
  * `gpt-5-nano`
  * `gpt-5-nano-2025-08-07`
  * `gpt-5.2`
  * `gpt-5.2-reasoning`
  * `gpt-5.4`
  * `gpt-5.4-mini`
  * `gpt-5.4-nano`
  * `gpt-5.4-reasoning`
  * `gpt-5.5`
  * `gpt-5.5-reasoning`
  * `gpt-5.6-luna`
  * `gpt-5.6-sol`
  * `gpt-5.6-terra`
  * `gpt-audio`
  * `gpt-audio-1.5`
  * `gpt-audio-2025-12-15`
  * `gpt-audio-mini`
  * `gpt-audio-mini-2025-12-15`
  * `gpt-oss`
  * `gpt-oss-20b`
  * `grok`
  * `grok-4`
  * `grok-4-1-fast`
  * `grok-4-1-fast-non-reasoning`
  * `grok-4-1-fast-reasoning`
  * `grok-4-20`
  * `grok-4-20-non-reasoning`
  * `grok-4-20-reasoning`
  * `grok-4-3`
  * `grok-4-5`
  * `grok-4-fast`
  * `grok-4.3`
  * `grok-4.5`
  * `grok-4.6`
  * `grok-fast`
  * `grok-large`
  * `grok-legacy`
  * `grok-non-reasoning`
  * `grok-reasoning`
  * `immature-yt/alara-nova-1`
  * `inception 💎`
  * `inception-mercury 💎`
  * `inception/mercury-2 💎`
  * `inception/mercury-2.5-preview 💎`
  * `inclusionai/ling-3.0-flash-vl 💎`
  * `inkling 💎`
  * `inkling-small 💎`
  * `inkling-small-20260730 💎`
  * `iotserver24/route-r3ap3r`
  * `iotserver24/supercharge`
  * `jaredpalmer/kev-4b`
  * `jev`
  * `kimi`
  * `kimi-code 💎`
  * `kimi-k2.6`
  * `kimi-k2.7 💎`
  * `kimi-k2.7-code 💎`
  * `kimi-k2p6`
  * `kimi-k2p7 💎`
  * `kimi-k3`
  * `kimi-large`
  * `kimi-reasoning`
  * `kimi-thinking`
  * `kreggscode/jev-test-triage`
  * `laguna 💎`
  * `laguna-s-2.1 💎`
  * `laguna-s2.1 💎`
  * `llama`
  * `llama-3.3`
  * `llama-3.3-70b`
  * `llama-4 💎`
  * `llama-4-maverick 💎`
  * `llama-4-maverick-17b-128e-instruct-fp8 💎`
  * `llama-4-scout 💎`
  * `llama-4-scout-17b-16e-instruct 💎`
  * `llama-maverick 💎`
  * `llama-maverick-17b 💎`
  * `llama-scout 💎`
  * `llama-scout-17b 💎`
  * `llama-v3p3-70b-instruct`
  * `longcat 💎`
  * `longcat-2 💎`
  * `longcat-2.0 💎`
  * `meituan/longcat-2.0 💎`
  * `mercury 💎`
  * `mercury-2 💎`
  * `meta/llama-3.3-70b-instruct`
  * `meta/llama-4-maverick 💎`
  * `meta/llama-4-scout 💎`
  * `meta/muse-glimmer-30b 💎`
  * `meta/muse-spark-1.2 💎`
  * `midijourney`
  * `midijourney-large`
  * `mikl-shortcuts/ministral-3`
  * `mimo 💎`
  * `mimo-2.5 💎`
  * `mimo-2.5-pro 💎`
  * `mimo-pro 💎`
  * `mimo-v2.5 💎`
  * `mimo-v2.5-pro 💎`
  * `minimax`
  * `minimax-3`
  * `minimax-m2.5 💎`
  * `minimax-m2.7 💎`
  * `minimax-m2p5 💎`
  * `minimax-m2p7 💎`
  * `minimax-m3`
  * `minimax/minimax-m2.7 💎`
  * `minimax/minimax-m3`
  * `minimax3`
  * `mistral 💎`
  * `mistral-4 💎`
  * `mistral-large`
  * `mistral-large-3`
  * `mistral-small 💎`
  * `mistral-small-2503 💎`
  * `mistral-small-2603 💎`
  * `mistral-small-3.1 💎`
  * `mistral-small-3.2 💎`
  * `mistral-small-3.2-24b-instruct-2506 💎`
  * `mistral-small-4 💎`
  * `mistralai/mistral-large-3`
  * `mistralai/mistral-small-3.2 💎`
  * `mistralai/mistral-small-4 💎`
  * `moonshotai/kimi-k2.6`
  * `moonshotai/kimi-k2.7-code 💎`
  * `moonshotai/kimi-k3`
  * `morriszdweck/osaii-api-smart`
  * `morriszdweck/osaii-swarm`
  * `muse-glimmer 💎`
  * `muse-spark 💎`
  * `muse-spark-1.1 💎`
  * `muse-spark-1.2 💎`
  * `nemotron 💎`
  * `nemotron-3-ultra 💎`
  * `nemotron-3-ultra-550b-a55b 💎`
  * `nemotron-3.5-lightning`
  * `nova`
  * `nova-2`
  * `nova-2-lite`
  * `nova-fast`
  * `nova-micro`
  * `nvidia-nemotron-3-ultra 💎`
  * `nvidia/nemotron-3-ultra 💎`
  * `nvidia/nemotron-3.5-lightning`
  * `openai`
  * `openai-audio`
  * `openai-audio-large`
  * `openai-fast`
  * `openai-large`
  * `openai-mini`
  * `openai-reasoning`
  * `openai/gpt-4o-mini 💎`
  * `openai/gpt-5-nano`
  * `openai/gpt-5.3-codex`
  * `openai/gpt-5.4`
  * `openai/gpt-5.4-mini`
  * `openai/gpt-5.4-nano`
  * `openai/gpt-5.5`
  * `openai/gpt-5.6-luna`
  * `openai/gpt-5.6-sol`
  * `openai/gpt-5.6-terra`
  * `openai/gpt-6-astra`
  * `openai/gpt-6-luna`
  * `openai/gpt-6-sol`
  * `openai/gpt-6.1-sol`
  * `openai/gpt-audio-1.5`
  * `openai/gpt-audio-mini`
  * `openai/gpt-oss-20b`
  * `ovh-reasoning`
  * `pegalink/gemini-3.1-pro-preview 💎`
  * `pegalink/gemini-3.8-flash 💎`
  * `pegalink/gemini-pro-coder 💎`
  * `pegalink/hy4-preview-coding 💎`
  * `perplexity 💎`
  * `perplexity-deep 💎`
  * `perplexity-fast 💎`
  * `perplexity-high 💎`
  * `perplexity-pro 💎`
  * `perplexity-reasoning 💎`
  * `perplexity/sonar 💎`
  * `perplexity/sonar-pro 💎`
  * `perplexity/sonar-reasoning-pro 💎`
  * `pollinations-ai/floret`
  * `pollinations-ai/midijourney`
  * `pollinations-ai/polli`
  * `pollinations/midijourney`
  * `pollinations/midijourney-large`
  * `poolside-laguna-s-2.1 💎`
  * `poolside/laguna-s-2.1 💎`
  * `qwen-coder`
  * `qwen-coder-large 💎`
  * `qwen-large 💎`
  * `qwen-max 💎`
  * `qwen-safety`
  * `qwen-vision 💎`
  * `qwen-vision-pro 💎`
  * `qwen-vl 💎`
  * `qwen-vl-pro 💎`
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
  * `qwen3-coder`
  * `qwen3-coder-30b-a3b-instruct`
  * `qwen3-coder-next 💎`
  * `qwen3-vl 💎`
  * `qwen3-vl-235b 💎`
  * `qwen3-vl-235b-a22b-thinking 💎`
  * `qwen3-vl-30b-a3b-instruct 💎`
  * `qwen3-vl-instruct 💎`
  * `qwen3-vl-plus 💎`
  * `qwen3-vl-pro 💎`
  * `qwen3.6 💎`
  * `qwen3.6-plus 💎`
  * `qwen3.7 💎`
  * `qwen3.7-flash 💎`
  * `qwen3.7-max 💎`
  * `qwen3.7-plus 💎`
  * `qwen3.8-2.4t-a95b`
  * `qwen3.8-27b 💎`
  * `qwen3.8-max 💎`
  * `qwen3guard-gen-8b`
  * `qwen3p6-plus 💎`
  * `qwen3p7-max 💎`
  * `qwen3p7-plus 💎`
  * `respan/span-01-lite`
  * `scriptsnsenses-sys/diffusiongema-26B-free`
  * `scriptsnsenses-sys/gpt-5.6-sol-free`
  * `sharktide/3D-agent`
  * `sharktide/inferenceport-ai-gemini-2.5-flash`
  * `sharktide/inferenceport-ai-kimi-k2.7-code-deep-logician 💎`
  * `sharktide/inferenceport-ai-lightning-text-v2`
  * `sharktide/inferenceport-ai-lightning-text-v2-expanded-knowledge`
  * `sharktide/inferenceport-ai-lightning-text-v2.1 💎`
  * `sharktide/inferenceport-ai-mimo-v2.5 💎`
  * `sharktide/inferenceport-ai-minimax-m3 💎`
  * `sharktide/inferenceport-ai-qwen-3.8-27b`
  * `sharktide/inferenceport.ai-gpt-oss-20b`
  * `smplstuff/title-generator`
  * `sonar 💎`
  * `sonar-deep 💎`
  * `sonar-pro 💎`
  * `sonar-reasoning 💎`
  * `sonar-reasoning-pro 💎`
  * `sonnet-5 💎`
  * `spark 💎`
  * `spark-1.1 💎`
  * `step-3.5-flash 💎`
  * `step-3.7-flash 💎`
  * `step-flash 💎`
  * `step-flash-3.5 💎`
  * `step-flash-3.7 💎`
  * `stepfun-3.5-flash 💎`
  * `stepfun-flash 💎`
  * `stepfun/step-3.5-flash 💎`
  * `stepfun/step-3.7-flash 💎`
  * `tencent/hy3 💎`
  * `tencent/hy4-preview 💎`
  * `thinkingmachines/inkling 💎`
  * `thinkingmachines/inkling-small 💎`
  * `tomdacatto/Humanish-Roleplay-Llama-3.1-8B 💎`
  * `tomdacatto/Qwen3.8-Flash-Next 💎`
  * `tomdacatto/ezra`
  * `tomdacatto/gotcha-scout`
  * `tomdacatto/llama-3.1-8B`
  * `tomdacatto/tiered-health-router`
  * `typesafe/jev`
  * `typesafe/jev-1.13`
  * `vendouple/deepseek-v4-flash`
  * `vendouple/glm-5.3-flash`
  * `vendouple/gpt-6-sol`
  * `vendouple/gpt-6-sol:stable 💎`
  * `vendouple/gpt-6.1-sol:stable 💎`
  * `voodoohop/airforce-doubao-pro`
  * `voodoohop/airforce-grok-4-fast`
  * `voodoohop/airforce-qwen3-max`
  * `voodoohop/catgpt-comic 💎`
  * `voodoohop/email-overview 💎`
  * `x-ai/grok-4.20`
  * `x-ai/grok-4.3`
  * `x-ai/grok-4.6`
  * `x-ai/grok-4.7 💎`
  * `xiaomi/mimo-v2.5 💎`
  * `xiaomi/mimo-v2.5-pro 💎`
  * `xiaomi/mimo-v2.6-flash 💎`
  * `xiaomi/mimo-v2.6-pro 💎`
  * `xiaotian1171/triage-router`
  * `z-ai/glm-5.2 💎`
  * `z-ai/glm-5.3`
  * `z-ai/glm-5.3-flash`
  * `z-ai/glm-5.3-flashx 💎`
* **Parameters:** `prompt`, `system_instruction`, `model`, `temperature`, `seed`, `api_key`

### 4.🌸🔊 Pollinations Audio Gen (BYOP)
Text-to-speech, music generation, and audio transcription.
* **Supported Models:**
  * `assemblyai-pro`
  * `assemblyai-u2`
  * `assemblyai-u3-pro`
  * `assemblyai-u3.5-pro`
  * `assemblyai-universal-2`
  * `assemblyai-universal-3-5-pro`
  * `assemblyai-universal-3-pro`
  * `assemblyai-universal-3.5-pro`
  * `assemblyai/universal-2`
  * `assemblyai/universal-3.5-pro`
  * `audio-cleanup 💎`
  * `csm 💎`
  * `csm-1b 💎`
  * `dialogue 💎`
  * `eleven 💎`
  * `eleven-dialogue 💎`
  * `eleven-flash 💎`
  * `eleven-multilingual-v2 💎`
  * `eleven-sfx 💎`
  * `eleven-sound-effects 💎`
  * `eleven-v2 💎`
  * `eleven-voice-changer 💎`
  * `eleven-voice-isolator 💎`
  * `elevenflash 💎`
  * `elevenlabs 💎`
  * `elevenlabs/eleven-flash-v2.5 💎`
  * `elevenlabs/eleven-multilingual-sts-v2 💎`
  * `elevenlabs/eleven-multilingual-v2 💎`
  * `elevenlabs/eleven-text-to-sound-v2 💎`
  * `elevenlabs/eleven-v3 💎`
  * `elevenlabs/eleven-v3:dialogue 💎`
  * `elevenlabs/music-v2 💎`
  * `elevenlabs/music-v2.5 💎`
  * `elevenlabs/scribe-v2 💎`
  * `elevenlabs/stem-separation 💎`
  * `elevenlabs/voice-isolator 💎`
  * `elevenmusic 💎`
  * `fal-ai/stable-audio-3/medium 💎`
  * `fish-audio-s2.1-pro 💎`
  * `fish-audio/s2.1-pro 💎`
  * `flash 💎`
  * `google/gemini-3.5-transcribe 💎`
  * `google/gemini-3.8-flash-lite-tts 💎`
  * `google/gemini-3.8-flash-tts 💎`
  * `google/lyria-3-clip-preview 💎`
  * `google/lyria-3.5 💎`
  * `gpt-transcribe`
  * `grok-transcribe 💎`
  * `grok-tts 💎`
  * `hexgrad-kokoro-82m 💎`
  * `hexgrad/kokoro-82m 💎`
  * `kokoro 💎`
  * `kokoro-82m 💎`
  * `kokoro-tts 💎`
  * `lyria 💎`
  * `lyria-3 💎`
  * `lyria-3-clip 💎`
  * `multilingual-v2 💎`
  * `music 💎`
  * `openai/gpt-transcribe`
  * `openai/tts-1`
  * `openai/tts-1-hd`
  * `openai/whisper-large-v3`
  * `qwen-tts 💎`
  * `qwen-tts-instruct 💎`
  * `qwen/qwen3-tts-flash 💎`
  * `qwen/qwen3-tts-instruct-flash 💎`
  * `qwen3-tts 💎`
  * `qwen3-tts-flash 💎`
  * `qwen3-tts-instruct 💎`
  * `qwen3-tts-instruct-flash 💎`
  * `scribe 💎`
  * `scribe-v2 💎`
  * `scribe_v2 💎`
  * `sesame-csm 💎`
  * `sesame-csm-1b 💎`
  * `sesame/csm-1b 💎`
  * `sfx 💎`
  * `sound-effects 💎`
  * `speech-to-speech 💎`
  * `stability-ai/stable-audio-3 💎`
  * `stability-ai/stable-audio-3-medium 💎`
  * `stability-audio 💎`
  * `stable-audio 💎`
  * `stable-audio-2.5 💎`
  * `stable-audio-3 💎`
  * `stable-audio-3-large 💎`
  * `stable-audio-3-medium 💎`
  * `stable-audio-large 💎`
  * `text-to-dialogue 💎`
  * `text-to-speech 💎`
  * `tts 💎`
  * `tts-1 💎`
  * `tts-1-hd 💎`
  * `tts-flash 💎`
  * `tts-multilingual 💎`
  * `universal-2`
  * `universal-3-5-pro`
  * `universal-3-pro`
  * `universal-3.5-pro`
  * `voice-changer 💎`
  * `voice-isolator 💎`
  * `whisper`
  * `whisper-1`
  * `whisper-large-v3`
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
