import speech_recognition as sr

def check_permission():
    detect_mic = sr.Microphone.list_microphone_names()
    if not detect_mic:
        return False
    else:
        return True
    

def manage_audio():
    if check_permission():
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something:")
            rec.adjust_for_ambient_noise(source)
            try:
                audio = rec.listen(source, timeout=50)
                print("Transcription: " + rec.recognize_google(audio))
                text = rec.recognize_google(audio)
                return text
            except sr.UnknownValueError:
                print("Sorry, say again.")
            except sr.RequestError as e:
                print(f"Error {e}")
    else:
        print("Mic not available please check permissions and try again.")