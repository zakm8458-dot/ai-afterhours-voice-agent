# ai-afterhours-voice-agent

This repository contains a prototype implementation of an AI‑powered after‑hours customer‑service voice agent built using only free/open‑source components. The goal is to create a voice agent that can listen to callers, use a language model to generate helpful responses, and speak back to the caller.  

## Components  

- **Speech‑to‑text (ASR)** – The code uses the WhisperASR class from the [Pipecat](https://github.com/pipecat-ai/pipecat) framework. You can configure it to use an open‑source Whisper model or Groq’s free Whisper API.  
- **Language model (LLM)** – Pipecat’s OpenAI wrapper is used by default, but you can swap this for a local open‑source model (e.g., Mistral) or any LLM supported by Pipecat. The FreeCodeCamp article on the EchoKit server notes that you can orchestrate your own language model and other services ([www.freecodecamp.org](https://www.freecodecamp.org/news/how-to-build-a-voice-ai-agent-using-open-source-tools/)).  
- **Text‑to‑speech (TTS)** – The example uses Coqui TTS because it is an open‑source TTS engine. You can replace it with any other TTS supported by Pipecat (e.g., ElevenLabs) while staying on a free tier.  
- **Pipeline orchestration** – Pipecat provides a `Pipeline` class that ties together the ASR, LLM, and TTS components into a streaming audio pipeline.  

## Installation  

1. Clone this repository.  
2. Install dependencies (Pipecat and Coqui TTS) with pip:  

   ```bash
   pip install -r requirements.txt
   ```  

   If you want to use the optional EchoKit server or Vocode for telephony integration, follow the instructions in their respective documentation.  

3. Obtain any required API keys for the services you choose (e.g., Groq Whisper for ASR, ElevenLabs for TTS) and set them as environment variables as required by Pipecat.  

## Usage  

The `main.py` file contains a simple example that listens to your microphone, sends the audio to an ASR engine, forwards the transcript to a language model, and speaks the response through your speakers. Run it with:  

```bash
python main.py
```  

This example is intended for local testing. For a production deployment, you will need to:  

1. Replace the ASR, LLM, and TTS components with your preferred (and free) services.  
2. Integrate a telephony layer (e.g., SIP server like Asterisk or FreeSWITCH) so that incoming phone calls can be routed into the Pipecat pipeline.  
3. Build conversation flows and a knowledge base tailored to the businesses you support.  
4. Deploy the application on a hosting environment capable of running the voice agent continuously (GitHub Codespaces, Replit, or your own VM on a free tier).  

## Next Steps  

- Expand `main.py` into a modular server that exposes an API endpoint or WebSocket for telephony integration.  
- Use an orchestrator like [EchoKit](https://github.com/echokit/echokit-server) to coordinate multiple models and manage streaming audio ([www.freecodecamp.org](https://www.freecodecamp.org/news/how-to-build-a-voice-ai-agent-using-open-source-tools/)).  
- Explore the [Vocode](https://github.com/vocodedev/vocode-python) and [Pipecat](https://github.com/pipecat-ai/pipecat) projects for additional examples and integrations ([github.com](https://github.com/vocodedev/vocode-core#:~:text=,Microsoft%20Azure%20%20109%20Google), [github.com](https://github.com/pipecat-ai/pipecat#:~:text=Voice%20%26%20Multimodal%20AI%20Agents,Swift)). 
