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
  * `alibaba/wan-2.7-image 💎`
  * `alibaba/wan-2.7-image-pro 💎`
  * `amazon/nova-canvas-v1`
  * `black-forest-labs/flux.1-kontext-pro`
  * `black-forest-labs/flux.1-schnell`
  * `black-forest-labs/flux.2-flex 💎`
  * `black-forest-labs/flux.2-klein-4b`
  * `black-forest-labs/flux.2-max 💎`
  * `black-forest-labs/flux.2-pro 💎`
  * `bytedance/seedream-4.0 💎`
  * `bytedance/seedream-4.5 💎`
  * `bytedance/seedream-5.0-lite 💎`
  * `bytedance/seedream-5.0-pro 💎`
  * `community/Catniti/agnes-image-2.5-flash`
  * `community/CloudCompile/agnes-image-2.0-flash`
  * `community/CloudCompile/flux-2-klein-4b`
  * `community/CloudCompile/flux-2-klein-9b`
  * `community/CloudCompile/sdxl-lightning`
  * `community/JustScriptzz/qwen-image-3.0-pro`
  * `community/MarcosFRG/flux-1-schnell`
  * `community/MarcosFRG/flux-1-schnell:paid 💎`
  * `community/MarcosFRG/flux-2-klein-4b`
  * `community/MarcosFRG/lucid-origin`
  * `community/MarcosFRG/lucid-origin:paid 💎`
  * `community/MarcosFRG/phoenix-1.0`
  * `community/MarcosFRG/phoenix-1.0:paid 💎`
  * `community/NamanSoni78/Imagine-4-low`
  * `community/NamanSoni78/Z-Image-Turbo`
  * `community/chigwell/firefly-gpt-image-2 💎`
  * `community/chigwell/gpt-image-2 💎`
  * `community/chigwell/gpt-image-2.5 💎`
  * `community/rekty/rekty-dev-3 💎`
  * `community/rekty/rekty-dev-v2 💎`
  * `community/sharktide/gpt-image-2.5-flare-input-cheap 💎`
  * `community/sharktide/gpt-image-2.5-sunburst-input-cheap 💎`
  * `community/sharktide/inferenceport-ai-gpt-image-2.5-flare 💎`
  * `community/sharktide/inferenceport-ai-gpt-image-2.5-sunburst 💎`
  * `community/sharktide/inferenceport-ai-gpt-image-router 💎`
  * `community/sharktide/inferenceport-ai-image-ultra 💎`
  * `community/sharktide/inferenceport-ai-lightning-image-plus`
  * `community/sharktide/inferenceport-ai-lightning-image-turbo`
  * `community/tomdacatto/nano-banana-pro`
  * `community/vendouple/anima`
  * `community/vendouple/grok-imagine`
  * `community/vendouple/lucid-origin`
  * `community/vendouple/luma-photon-1`
  * `community/vendouple/nano-banana-pro`
  * `community/vendouple/qwen-image-3.0-pro 💎`
  * `community/vendouple/uncensored-image-v2`
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
  * `tongyi-mai/z-image-turbo`
  * `x-ai/grok-imagine-image 💎`
  * `x-ai/grok-imagine-image-2.0 💎`
  * `x-ai/grok-imagine-image-quality 💎`
* **Parameters:** `prompt`, `model`, `width`, `height`, `seed`, `api_key`, `negative_prompt`

### 2. 🌸🎞️ Pollinations Video Gen (BYOP)
Generates high-quality AI video.
* **Supported Models:**
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
  * `community/NamanSoni78/Seedance-2.5`
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
  * `cohere/command-a-plus`
  * `community/AkshayCoder48/Qwen3.5-9B-Q4_K_M.gguf`
  * `community/AkshayCoder48/chat-model-reasoning`
  * `community/AkshayCoder48/chat-model-reasoning-with-search`
  * `community/AkshayCoder48/claude-sonnet-4`
  * `community/AkshayCoder48/code-pair`
  * `community/AkshayCoder48/codestral-latest`
  * `community/AkshayCoder48/cohere-north-mini-code:free`
  * `community/AkshayCoder48/deepseek-r1`
  * `community/AkshayCoder48/deepseek-v3`
  * `community/AkshayCoder48/deepseek-v3.1`
  * `community/AkshayCoder48/free-clips 💎`
  * `community/AkshayCoder48/free-voice`
  * `community/AkshayCoder48/gemini-2.5-flash`
  * `community/AkshayCoder48/gemini-2.5-pro`
  * `community/AkshayCoder48/gemini-3-flash`
  * `community/AkshayCoder48/gemini-3.1-flash-lite`
  * `community/AkshayCoder48/gemini-3.5-flash`
  * `community/AkshayCoder48/gemini-3.6-flash`
  * `community/AkshayCoder48/gpt-4o-latest`
  * `community/AkshayCoder48/gpt-5`
  * `community/AkshayCoder48/gpt-5-6-luna`
  * `community/AkshayCoder48/gpt-5.2`
  * `community/AkshayCoder48/gpt-oss-120b`
  * `community/AkshayCoder48/grok-4-3`
  * `community/AkshayCoder48/grok-4-6`
  * `community/AkshayCoder48/kilo-auto-free`
  * `community/AkshayCoder48/kilo-auto-small`
  * `community/AkshayCoder48/lfm-7b`
  * `community/AkshayCoder48/llama3-8b`
  * `community/AkshayCoder48/nvidia-nemotron-3-nano-omni-30b-a3b-reasoning-free`
  * `community/AkshayCoder48/nvidia-nemotron-3-super-120b-a12b-free`
  * `community/AkshayCoder48/nvidia-nemotron-3-ultra-550b-a55b-free`
  * `community/AkshayCoder48/o3-mini`
  * `community/AkshayCoder48/poolside-laguna-s-2.1:free`
  * `community/AkshayCoder48/prompt-to-art 💎`
  * `community/AkshayCoder48/qwen3-coder-480b`
  * `community/AkshayCoder48/researcher 💎`
  * `community/AkshayCoder48/sft-7b`
  * `community/AkshayCoder48/stepfun-step-3.7-flash-free`
  * `community/AkshayCoder48/toolbaz-v4.5-fast`
  * `community/AkshayCoder48/toolbaz_v4`
  * `community/AkshayCoder48/v3`
  * `community/AkshayCoder48/vexa`
  * `community/Bakhshi7889/gemma-4-31b-it`
  * `community/Catniti/agnes-3.0-flash`
  * `community/Catniti/catniti-ai-agent`
  * `community/Catniti/nemotron-3.5-lightning`
  * `community/CloudCompile/agnes-2.5-flash`
  * `community/CloudCompile/agnes-3.0-flash`
  * `community/CloudCompile/auto`
  * `community/CloudCompile/gemma-4-26b`
  * `community/CloudCompile/pollinations-code-agent-but-weird`
  * `community/Creatneworld/catgpt-comic 💎`
  * `community/Creatneworld/lamplighter 💎`
  * `community/Creatneworld/sirius-elevator-descent 💎`
  * `community/JustScriptzz/agnes-2.5-flash`
  * `community/JustScriptzz/glm-5.3-flash`
  * `community/JustScriptzz/gpt-oss-120b`
  * `community/JustScriptzz/grok-4.6`
  * `community/JustScriptzz/kimi-k2-7-code`
  * `community/JustScriptzz/moondream-3.1`
  * `community/MarcosFRG/deepseek-v4-flash-0731`
  * `community/MarcosFRG/deepseek-v4-flash-0731:paid 💎`
  * `community/MarcosFRG/deepseek-v4-pro-0813`
  * `community/MarcosFRG/gemini-3-flash-preview:paid 💎`
  * `community/MarcosFRG/gemini-3.1-flash-lite`
  * `community/MarcosFRG/gemini-3.1-pro-preview 💎`
  * `community/MarcosFRG/gemma-4-26b-a4b:paid 💎`
  * `community/MarcosFRG/gemma-4-31b`
  * `community/MarcosFRG/gemma-4-31b:paid 💎`
  * `community/MarcosFRG/glm-4.6v-flash`
  * `community/MarcosFRG/glm-5.2:paid 💎`
  * `community/MarcosFRG/glm-5.3`
  * `community/MarcosFRG/glm-5.3-flash`
  * `community/MarcosFRG/gpt-5.6-luna:paid 💎`
  * `community/MarcosFRG/gpt-6-astra:paid 💎`
  * `community/MarcosFRG/metraxai`
  * `community/MarcosFRG/minimax-m3:paid 💎`
  * `community/MarcosFRG/moondream-3.1`
  * `community/MarcosFRG/nemotron-3.5-lightning:paid 💎`
  * `community/MarcosFRG/qwen3.8-27b`
  * `community/MarcosFRG/qwen3.8-27b:paid 💎`
  * `community/MarcosFRG/qwen3.8-flash:paid 💎`
  * `community/MarcosFRG/qwen3.8-max 💎`
  * `community/Minor-fun/deepseek-v3.2`
  * `community/Minor-fun/gemma-4-31B-it`
  * `community/NamanSoni78/Claude-Fable-5.1`
  * `community/NamanSoni78/Claude-Sonnet-5`
  * `community/NamanSoni78/DeepSeek-V4.1-Flash`
  * `community/NamanSoni78/Glm-5.3-Thinking-Max`
  * `community/NamanSoni78/devin-agi-agent`
  * `community/NamanSoni78/devin-ai`
  * `community/NamanSoni78/fugu-ultra-v2`
  * `community/NamanSoni78/gemini-3.8-flash`
  * `community/NamanSoni78/gpt-5.6-Luna`
  * `community/NamanSoni78/gpt-6-astra-pro`
  * `community/NamanSoni78/opus-5-max`
  * `community/Spit-fires/muse-glimmer`
  * `community/YoannDev90/agentic-gt`
  * `community/YoannDev90/ling-3.0-flash-vl`
  * `community/YoannDev90/muse-glimmer-30b:free`
  * `community/YoannDev90/poolside-laguna-s-2.1:free`
  * `community/YoannDev90/qwen3.7-flash`
  * `community/ZapGaming/gpt-oss-120b-ultrafast 💎`
  * `community/ZapGaming/llama3.1-8b-xturbo`
  * `community/ZapGaming/mercury-2.5-ultrafast`
  * `community/aikhusus2025-ctrl/ember-perch`
  * `community/aikhusus2025-ctrl/place-painter`
  * `community/aikhusus2025-ctrl/sirius-elevator`
  * `community/aikhusus2025-ctrl/sirius-scorekeeper`
  * `community/chigwell/claude-fable-5 💎`
  * `community/chigwell/claude-haiku-4-5`
  * `community/chigwell/claude-opus-4-8 💎`
  * `community/chigwell/claude-opus-5 💎`
  * `community/chigwell/claude-sonnet-4-6 💎`
  * `community/chigwell/claude-sonnet-5 💎`
  * `community/chigwell/gemini-3-flash 💎`
  * `community/chigwell/gemini-3.1-flash-lite 💎`
  * `community/chigwell/gemini-3.7-flash 💎`
  * `community/chigwell/gemini-3.8-flash-high 💎`
  * `community/chigwell/glm-5.3 💎`
  * `community/chigwell/gpt-5.5 💎`
  * `community/chigwell/gpt-5.6-sol 💎`
  * `community/chigwell/gpt-5.6-terra 💎`
  * `community/chigwell/gpt-6-astra 💎`
  * `community/chigwell/grok-4.5 💎`
  * `community/chigwell/grok-4.6 💎`
  * `community/chigwell/kimi-k3 💎`
  * `community/chigwell/llm7-fast`
  * `community/chigwell/llm7-pro 💎`
  * `community/chigwell/minimax-m2.7 💎`
  * `community/fadyabohamza-netizen/frugal`
  * `community/gggff123/Glm-5.3`
  * `community/gggff123/gpt-5-nano`
  * `community/gggff123/qwen3.8-27b:free`
  * `community/immature-yt/alara-nova-1`
  * `community/iotserver24/deepseek-fast`
  * `community/iotserver24/route-r3ap3r`
  * `community/iotserver24/supercharge`
  * `community/mikl-shortcuts/ministral-3`
  * `community/morriszdweck/osaii-api-fast`
  * `community/morriszdweck/osaii-api-smart`
  * `community/morriszdweck/osaii-swarm`
  * `community/pegalink/gemini-3.1-pro-preview 💎`
  * `community/pegalink/gemini-3.5-flash-lite`
  * `community/pegalink/gemini-3.8-flash 💎`
  * `community/pegalink/gemini-pro-coder 💎`
  * `community/pegalink/hy4-preview 💎`
  * `community/pegalink/hy4-preview-coding 💎`
  * `community/pegalink/jimmy`
  * `community/pollinations-router/floret`
  * `community/pollinations-router/midijourney`
  * `community/pollinations-router/polli`
  * `community/scriptsnsenses-sys/glm-5.3-flash-free`
  * `community/scriptsnsenses-sys/gpt-5.6-sol-free`
  * `community/scriptsnsenses-sys/muse-spark-1.2-contributor-free`
  * `community/sharktide/3D-agent`
  * `community/sharktide/inferenceport-ai-codestral-2508`
  * `community/sharktide/inferenceport-ai-command-r-plus`
  * `community/sharktide/inferenceport-ai-gemini-2.5-flash`
  * `community/sharktide/inferenceport-ai-kimi-k2.7-code`
  * `community/sharktide/inferenceport-ai-kimi-k2.7-code-deep-logician`
  * `community/sharktide/inferenceport-ai-lightning-text-v2`
  * `community/sharktide/inferenceport-ai-lightning-text-v2-expanded-knowledge`
  * `community/sharktide/inferenceport-ai-mimo-v2.5`
  * `community/sharktide/inferenceport-ai-minimax-m3`
  * `community/sharktide/inferenceport-ai-qwen-3.8-27b`
  * `community/sharktide/inferenceport.ai-gpt-oss-20b`
  * `community/smplstuff/title-generator`
  * `community/tomdacatto/ezra`
  * `community/tomdacatto/llama-3.1-8B`
  * `community/tomdacatto/qwen-3.8-27B-fast`
  * `community/tomdacatto/tiered-health-router`
  * `community/vendouple/claude-opus-5 💎`
  * `community/vendouple/deepseek-v3.2`
  * `community/vendouple/deepseek-v4-pro`
  * `community/vendouple/fable-5.1`
  * `community/vendouple/gemini-3.8-flash`
  * `community/vendouple/gemma-4-31b-isometry-rp`
  * `community/vendouple/glm-5.3`
  * `community/vendouple/gpt-5.6-sol`
  * `community/vendouple/grok-4.6`
  * `community/vendouple/kimi-k3`
  * `community/vendouple/muse-glimmer-30b:free`
  * `community/vendouple/qwen-3.8-max`
  * `community/voodoohop/airforce-doubao-pro`
  * `community/voodoohop/airforce-grok-4-fast`
  * `community/voodoohop/airforce-qwen3-max`
  * `community/voodoohop/anyvm-deepseek-chat`
  * `community/voodoohop/catgpt-comic 💎`
  * `community/voodoohop/email-overview 💎`
  * `community/xiaotian1171/bottle-courier`
  * `community/xiaotian1171/triage-router`
  * `deepseek/deepseek-v4-flash`
  * `deepseek/deepseek-v4-flash-vision-exp`
  * `deepseek/deepseek-v4-pro`
  * `deepseek/deepseek-v4.1-flash`
  * `google/gemini-2.5-flash-lite 💎`
  * `google/gemini-2.5-flash-lite:search 💎`
  * `google/gemini-3-flash-preview 💎`
  * `google/gemini-3.1-pro-preview 💎`
  * `google/gemini-3.5-flash-lite 💎`
  * `google/gemini-3.7-flash 💎`
  * `google/gemini-3.8-flash 💎`
  * `google/gemma-4-26b-a4b-it 💎`
  * `google/gemma-4-31b-it 💎`
  * `inception/mercury-2 💎`
  * `inception/mercury-2.5-preview 💎`
  * `meituan/longcat-2.0 💎`
  * `meta/llama-3.3-70b-instruct`
  * `meta/llama-4-maverick 💎`
  * `meta/llama-4-scout 💎`
  * `meta/muse-glimmer-30b`
  * `meta/muse-spark-1.2 💎`
  * `minimax/minimax-m2.7 💎`
  * `minimax/minimax-m3`
  * `mistralai/mistral-large-3`
  * `mistralai/mistral-small-3.2 💎`
  * `mistralai/mistral-small-4 💎`
  * `moonshotai/kimi-k2.6`
  * `moonshotai/kimi-k2.7-code`
  * `moonshotai/kimi-k3`
  * `nvidia/nemotron-3-ultra 💎`
  * `nvidia/nemotron-3.5-lightning`
  * `openai/gpt-4o-mini 💎`
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
  * `stepfun/step-3.5-flash 💎`
  * `stepfun/step-3.7-flash 💎`
  * `tencent/hy3 💎`
  * `tencent/hy4-preview 💎`
  * `thinkingmachines/inkling 💎`
  * `thinkingmachines/inkling-small 💎`
  * `typesafe/jev-1.13`
  * `x-ai/grok-4.20`
  * `x-ai/grok-4.3`
  * `x-ai/grok-4.6`
  * `x-ai/grok-4.7 💎`
  * `xiaomi/mimo-v2.5 💎`
  * `xiaomi/mimo-v2.5-pro 💎`
  * `z-ai/glm-5.2`
  * `z-ai/glm-5.3`
  * `z-ai/glm-5.3-flash`
* **Parameters:** `prompt`, `system_instruction`, `model`, `temperature`, `seed`, `api_key`

### 4.🌸🔊 Pollinations Audio Gen (BYOP)
Text-to-speech, music generation, and audio transcription.
* **Supported Models:**
  * `assemblyai/universal-2`
  * `assemblyai/universal-3.5-pro`
  * `community/NamanSoni78/FISH-AUDIO-S2.1-PRO`
  * `community/NamanSoni78/flux-jack-en`
  * `community/NamanSoni78/whisper-large-v3`
  * `community/NamanSoni78/whisper-large-v3-turbo`
  * `elevenlabs/eleven-flash-v2.5 💎`
  * `elevenlabs/eleven-multilingual-sts-v2 💎`
  * `elevenlabs/eleven-multilingual-v2 💎`
  * `elevenlabs/eleven-text-to-sound-v2 💎`
  * `elevenlabs/eleven-v3 💎`
  * `elevenlabs/eleven-v3:dialogue 💎`
  * `elevenlabs/music-v2 💎`
  * `elevenlabs/music-v2.5 💎`
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
