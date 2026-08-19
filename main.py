from pynput import keyboard
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
import os
import subprocess

os.add_dll_directory(r'C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.8\bin')

model = WhisperModel("base.en", device="cuda")

sample_rate = 16000

audio_chunks = []

applications = {
    "deadlock": {"type": "steam",
                 "target": "1422450"},
    "steam": {"type":"executable",
              "target":r"C:\Program Files (x86)\Steam\steam.exe"}
}

print(applications["deadlock"]["target"])

allowed_actions = ["launch", "open", "start"]
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

            if not audio_chunks:
                print("No audio recorded")
                return
            recording = np.concatenate(audio_chunks)
            process_recording(recording)   


def parse_command(transcript):
    print(transcript)
    words = transcript.split()
    if len(words) < 2:
        print("Incomplete command")
        return None, None
    if not words:
        print("No command Recognized")
        return None, None
    action = words[0]
    target = " ".join(words[1:])
    return action,target   

    
def process_recording(recording):
    text_parts = []
    audio = recording.squeeze()
    segments, info = model.transcribe(audio)
    for segment in segments:
        text_parts.append(segment.text)
    transcript = " ".join(text_parts).strip().lower().replace(".","").replace(",","")
    action, target = parse_command(transcript)
    if target in applications and action in allowed_actions:
        launch_applcation(applications[target])
    else:
        print("Application not found")

def launch_applcation(app):
    if app["type"] == "executable":
        try:
            subprocess.Popen(app["target"])
        except FileNotFoundError:
            print("Executable could not be found")    
    elif app["type"] == "steam":
        steam_uri = f"steam://rungameid/{app['target']}"
        os.startfile(steam_uri)
        #subprocess.Popen(app["target"])
        


stream = sd.InputStream(
    samplerate=sample_rate,
    channels=1,
    callback=handle_audio
)
listener = keyboard.Listener(on_press=handle_key_press, on_release=handle_key_release)     

print("voice Launcher started")
listener.start()

listener.join()



