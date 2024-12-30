import speech_recognition as sr

def speech_to_text():
    """
    Converts speech to text using a microphone input.

    Returns:
        str: The text from the user's speech.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak now...")
        audio = recognizer.listen(source)
    
    try:
        # Use Google's free speech-to-text API
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand your speech."
    except sr.RequestError:
        return "Sorry, the speech service is unavailable."

