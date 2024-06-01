import speech_recognition as sr

recognizer = sr.Recognizer()
try:
   with sr.Microphone() as mic:
      print("Listening...")
      recognizer.adjust_for_ambient_noise(mic, duration=0.2)
      audio = recognizer.listen(mic)
      text = recognizer.recognize_google(audio)
      text = text.lower()
      print(f"Text:\n{text}")

except sr.UnknownValueError():
   recognizer = sr.Recognizer()
   print("Could not understand audio")