import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as received_audio:
    print('Speak')
    audio = r.listen(received_audio)
try:
    print("Transcription: " + r.recognize_google(audio))   # recognize speech using Google Speech Recognition
except LookupError:                                 # speech is unintelligible
    print("Could not understand the audio coming from the target. No audio is being transmitted")

       # write audio to a WAV file
with open("microphone-results_2.wav", "wb") as recorded_wav_audio:
    recorded_wav_audio.write(audio.get_wav_data())
