import ctypes
from ctypes import *
import speech_recognition as sr
r = sr.Recognizer()


winmm= windll.winmm
print('waveInGetNumDevs=',winmm.waveInGetNumDevs())


m = sr.Microphone
for i, microphone_name in enumerate(m.list_microphone_names()):
    if microphone_name == "Line In (Conexant ISST Audio)":
        print('mic is there')
        m = m(device_index=i)
