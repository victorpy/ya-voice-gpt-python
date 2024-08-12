# voice-chatgpt-python

This program uses speech recognition and text-to-speech with the OpenAI API and model `gpt-3.5-turbo` to generate voice responses to voice user prompts.
The program was tested (2024-08) in a Mac Book PRO 2020 with Intel processor and macOS Ventura 13.4. 

## Requirements
- Python 3.10
- SpeechRecognition
- py3-tts
- OpenAI API key
- portaudio (for pyaudio)
- pyaudio

## Installation
1. Install Python 3.10
2. Install the portaudio for mac running the following:
```
brew install portaudio
```
3. Install required libraries by running the following command:
```
pip install -r requirements.txt
```
4. Get an OpenAI API key from [OpenAI](https://beta.openai.com/signup/).

## Usage
1. Run the program by executing the following command:
```
python voicechatgpt.py
```
2. Speak into the microphone when prompted.

## References
[1] https://github.com/enoobis/voice-chatgpt-python