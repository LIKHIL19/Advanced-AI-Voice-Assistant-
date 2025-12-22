import speech_recognition as sr

def listen(timeout: int = 5) -> str:
    """
    Capture audio from the microphone and convert to text using Google STT.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=timeout)
    return recognizer.recognize_google(audio)