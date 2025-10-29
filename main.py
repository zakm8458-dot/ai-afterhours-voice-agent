# main.py
# After-hours AI voice agent using Pipecat framework

from pipecat import Pipeline
from pipecat.sources.microphone import MicrophoneSource
from pipecat.sinks.speaker import SpeakerSink
from pipecat.llms import OpenAI
from pipecat.stt import WhisperASR
from pipecat.tts import CoquiTTS


def main():
    """Run a simple voice assistant that listens to the user, uses a language model to generate a response, and speaks back."""
    # Initialize the speech-to-text engine (Whisper via Groq or local install)
    stt = WhisperASR()

    # Initialize the language model. Replace with a free/open-source model provider or local model.
    llm = OpenAI(model="gpt-3.5-turbo")

    # Initialize the text-to-speech engine (Coqui TTS is open source)
    tts = CoquiTTS()

    # Set up microphone as input and speaker as output
    source = MicrophoneSource()
    sink = SpeakerSink()

    # Create the pipeline
    pipeline = Pipeline(source=source, llm=llm, stt=stt, tts=tts, sink=sink)

    # Run the pipeline
    pipeline.run()


if __name__ == "__main__":
    main()
