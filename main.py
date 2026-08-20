from pynput import keyboard
import sounddevice as sd
from faster_whisper import WhisperModel
import os
import speech
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

logger = logging.getLogger(__name__)

def handle_key_press(key):
    if key == keyboard.Key.f8:
        speech.start_recording()

def handle_key_release(key):
    if key == keyboard.Key.f8:
        speech.stop_recording()

stream = sd.InputStream(
    samplerate=speech.sample_rate,
    channels=1,
    callback=speech.handle_audio
)
listener = keyboard.Listener(on_press=handle_key_press, on_release=handle_key_release)

logger.info("Voice application started")

stream.start()
listener.start()

listener.join()



