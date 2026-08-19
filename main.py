from pynput import keyboard
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

model = WhisperModel("base.en", device="cuda")

sample_rate = 16000

audio_chunks = []



is_recording = False

def handle_audio(indata, frames, time, status):
    audio_chunks.append(indata.copy())

def handle_key_press(key):
    global is_recording
    if key == keyboard.Key.f8:
        if not is_recording:
            audio_chunks.clear()
            print(key, "Is being held down")
            stream.start()
            is_recording = True
            return(is_recording)

def handle_key_release(key):
    global is_recording
    if key == keyboard.Key.f8:
        if is_recording:
            print(key, "Is being released")
            stream.stop()
            is_recording = False
            print(len(audio_chunks))
            recording = np.concatenate(audio_chunks)
            process_recording(recording)

def process_recording(recording):
    audio = recording.squeeze()
    segments, info = model.transcribe(audio)
    for segment in segments:
        print(segment.text)
    

stream = sd.InputStream(
    samplerate=sample_rate,
    channels=1,
    callback=handle_audio
)
listener = keyboard.Listener(on_press=handle_key_press, on_release=handle_key_release)     

print("voice Launcher started")
    
listener.start()

print(sd.query_devices())

listener.join()



