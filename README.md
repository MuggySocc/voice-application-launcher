# Voice Application Launcher

Voice Application Launcher allows users to add multiple applications and launch them using voice commands. Hold a hotkey and speak a command such as "launch Steam." The speech is recognized locally, matched to a configured application or game, and launched automatically.

## Features

- Aliases for configured applications
- Multiple launch methods
- Command validation
- Error handling
- GPU-accelerated local transcription
- Hotkey detection
- Application and game launching

## Technologies

- Python — core application language
- faster-whisper — local speech-to-text transcription
- CUDA — GPU acceleration for speech recognition
- NumPy — audio data processing
- sounddevice — microphone input and audio streaming
- pynput — global keyboard/hotkey detection
- Python subprocess — launching executable applications
- Python os — Windows URI handling

## How It Works

1. The user holds the configured hotkey to begin recording.
2. Audio chunks are captured from the microphone and combined using NumPy.
3. faster-whisper transcribes the recorded audio into text locally.
4. The transcript is parsed into an action and target.
5. The action and target are validated against the configured commands, applications, and aliases.
6. If valid, the appropriate launch method is selected and the application or game is launched.
7. Invalid or incomplete commands are handled without crashing the application.

## Project Structure

- `main.py` — Starts the application and handles hotkey detection.
- `speech.py` — Handles microphone input, audio recording, and local speech-to-text transcription.
- `commands.py` — Parses transcribed speech into an action and target and handles command normalization.
- `launcher.py` — Determines the appropriate launch method and launches executables or Steam games.
- `config.py` — Stores application definitions, aliases, allowed actions, and other configuration settings.
