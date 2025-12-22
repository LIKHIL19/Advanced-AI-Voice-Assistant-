import threading
import pyttsx3
# Global variables for TTS control
tts_engine = None
speaking_thread = None
pause_speaking_flag = False
current_text = None

def initialize_tts():
    global tts_engine
    if tts_engine is None:
        tts_engine = pyttsx3.init()
        tts_engine.setProperty('rate', 150)
        tts_engine.setProperty('volume', 1.0)

def _cleanup_engine():
    global tts_engine
    if tts_engine is not None:
        try:
            tts_engine.stop()
        except:
            pass
        tts_engine = None

def speak(text: str, lang: str = "en"):
    global speaking_thread, pause_speaking_flag, tts_engine, current_text
    current_text = text
    pause_speaking_flag = False
    
    try:
        _cleanup_engine()
        tts_engine = pyttsx3.init()
        tts_engine.setProperty('rate', 150)
        tts_engine.setProperty('volume', 1.0)
        tts_engine.setProperty('voice', 'hi' if lang == "hi" else 'en' if lang == "en" else 'es')
        
        if speaking_thread is not None and speaking_thread.is_alive():
            speaking_thread.join(timeout=1.0)
        speaking_thread = threading.Thread(target=_speak_thread, args=(text,))
        speaking_thread.start()
    except Exception as e:
        print(f"Error initializing TTS: {e}")

def _speak_thread(text: str):
    global pause_speaking_flag, tts_engine
    try:
        if not pause_speaking_flag and tts_engine is not None:
            tts_engine.say(text)
            tts_engine.runAndWait()
    except Exception as e:
        print(f"Error in speech: {e}")
    finally:
        _cleanup_engine()

def pause_speaking():
    global pause_speaking_flag, tts_engine
    if tts_engine is not None:
        pause_speaking_flag = True
        _cleanup_engine()

def resume_speaking():
    global pause_speaking_flag, current_text
    if pause_speaking_flag and current_text:
        pause_speaking_flag = False
        speak(current_text)