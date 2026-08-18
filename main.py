from pynput import keyboard
import sounddevice as sd

sample_rate = 16000


def handle_key_press(key):
    if key == keyboard.Key.f8:
        print(key, "Is being held down")


def handle_key_release(key):
    if key == keyboard.Key.f8:
        print(key, "Is being released")

print("voice Launcher started")

listener = keyboard.Listener(on_press=handle_key_press, on_release=handle_key_release)




listener.start()

print(sd.query_devices())

listener.join()