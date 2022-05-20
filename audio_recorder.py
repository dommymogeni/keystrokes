# importing all the neccessary and required libraries
import speech_recognition as sr
import time
import sounddevice as sd

# getting the microphone devices attached to your pc
microphone = sr.Microphone.list_microphone_names()
print(microphone)

chunk = 1024 # recording in chunks of 1024 samples
fps = 48000 # frames per second to be recorded
duration = 360 # getting the duration to be used during the recording of the audio
fn = "audio.wav" # file the recording is going to be saved in


# rec() is used in the recording of the audio and it takes other arguments with it
audio_rec = sd.rec(int(duration * fps), samplerate = fps, channels = 2, dtype='float64')
sd.wait() # used in checking if the recording is over

with open(fn, "w") as file:
    file.write(audio_rec)
