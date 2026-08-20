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

## Installation

### Prerequisites

Before installing the project, make sure you have:

- Python 3.11 or later
- Git
- An NVIDIA GPU for GPU-accelerated transcription
- A compatible NVIDIA driver
- CUDA 12 libraries required by faster-whisper/CTranslate2

### 1. Clone the repository

```powershell
git clone <https://github.com/MuggySocc/voice-application-launcher>
cd VoiceLauncher
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

Using PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell prevents the activation script from running, temporarily allow scripts for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then run the activation command again.

### 4. Install Python dependencies

```powershell
python -m pip install -r requirements.txt
```

This installs the Python packages required by the application, including faster-whisper, NumPy, sounddevice, and pynput.

### 5. Configure NVIDIA CUDA

GPU-accelerated transcription requires the CUDA libraries used by faster-whisper/CTranslate2.

Make sure the required CUDA libraries are installed and available to Windows. The application currently uses CUDA for local Whisper inference.

> **Note:** CUDA installation and library requirements may vary depending on the installed version of faster-whisper/CTranslate2 and the NVIDIA software available on the system.

### 6. Configure applications

Open `config.py` and add the applications or games you want the voice launcher to recognize.

Applications can be configured using supported launch methods such as Windows executables or Steam App IDs.

### 7. Run the application

With the virtual environment activated:

```powershell
python main.py
```

Once the launcher is running, hold the configured hotkey and speak a supported command such as:

```text
launch steam
```