import pyttsx3
import threading

class Speaker:
    def __init__(self, isSpeaking = False):
        self.engine = pyttsx3.init()
        self.voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',self.voices[1].id)
        self.engine.setProperty('rate', 300)

        self.speech_lock = threading.Lock()
        self.isSpeaking = isSpeaking

    def set_speed(self, speed = 300):
        self.engine.setProperty('rate', speed)
    
    def speak(self, content):
        if self.isSpeaking == False:
            print(content)   
            threading.Thread(target=self._speak_in_thread, args=(content,)).start()
    
    def _speak_in_thread(self, content):
        with self.speech_lock:
            self.isSpeaking = True
            self.engine.say(content)
            self.engine.runAndWait()
            self.isSpeaking = False