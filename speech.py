import commands
import config
import launcher
import os
from faster_whisper import WhisperModel
import numpy as np
import logging

logger = logging.getLogger(__name__)

sample_rate = 16000

aliaes_names = list(config.aliaes.keys())
app_names = list(config.applications.keys())

all_names = app_names + aliaes_names

hotwords = " ".join(all_names)

is_recording = False

audio_chunks = []

model = None

def initialize():
    global model
    model = load_model()

def get_cuda():
    
    cuda_path = os.environ.get("CUDA_PATH")
    
    if cuda_path:
        cuda_bin = os.path.join(cuda_path, "bin")
        return cuda_bin
    else:
        logger.info("CUDA_PATH not found")

def get_device():
    cuda_bin = get_cuda()
    if cuda_bin:
        os.add_dll_directory(cuda_bin)
        device = "cuda"
        logger.info("Using CUDA for transcription")
        return device
    else:
        device = "cpu"
        logger.info("CUDA unavailable, using CPU")
        return device

def load_model():
    device = get_device()
    model = WhisperModel("small.en", device=device)
    return model

def handle_audio(indata, frames, time, status):
    if is_recording:
        audio_chunks.append(indata.copy())
    else:
        return

def process_recording(recording):
    text_parts = []
    audio = recording.squeeze()
    segments, info = model.transcribe(audio,hotwords=hotwords)
    for segment in segments:
        text_parts.append(segment.text)
    transcript = " ".join(text_parts).strip().lower().replace(".","").replace(",","")
    logger.info(transcript)
    action, target = commands.parse_command(transcript)
    if target in config.applications and action in config.allowed_actions:
        launcher.launch_application(config.applications[target])
    else:
        logger.error("Application not found")

def start_recording():
    global is_recording

    if not is_recording:
        audio_chunks.clear()
        
        is_recording = True

def stop_recording():
    global is_recording

    if is_recording:
        
        is_recording = False

        if not audio_chunks:
            logger.error("No audio recorded")
            return
        recording = np.concatenate(audio_chunks)
        process_recording(recording)
