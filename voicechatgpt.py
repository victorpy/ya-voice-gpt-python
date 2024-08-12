from openai import OpenAI 
import speech_recognition as sr
import pyttsx3

# OpenAI API key
client = OpenAI(
    api_key = "<your-openao-api-key>"
)

# Text-to-speech engine
engine = pyttsx3.init()

def listen_and_respond():
    """
    Listen for audio input, recognize it and respond using OpenAI
    """
    # Create speech recognizer object
    r = sr.Recognizer()

    # Listen for input
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    # Try to recognize the audio
    try:
        prompt = r.recognize_google(audio, language="en-EN", show_all=False)
        print("You asked:", prompt)

        # Use OpenAI to create a response
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = [ # Change the prompt parameter to messages parameter
                {"role": "system", "content": "You are a helpful AI asistant."},
                {"role": "user", "content": f"Please analyze the following text and answer accordingly:{prompt}",}, 
            ],
            temperature=0,
            max_tokens=128,
            n=1,
            stop=None,
            timeout=10,
        )
        
        # Get the response text
        print(response)
        response_text = str(response.choices[0].message.content).strip('\n\n')
        print(response_text)

        # Speak the response
        engine.say(response_text)
        engine.runAndWait()
        print()

    # Catch if recognition fails
    except sr.UnknownValueError:
        response_text = "Sorry, I didn't understand what you said"
        print(response_text)
        engine.say(response_text)
        engine.runAndWait()
        print()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def main():
    while True:
        listen_and_respond()

if __name__ == "__main__":
    main()