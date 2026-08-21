import speech
import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import config


class TestSpeech(unittest.TestCase):

    def test_cuda(self):
        with patch("speech.get_cuda", return_value=r"C:\fake\cuda\bin") as mock_cuda:
            with patch("speech.os.add_dll_directory") as mock_add_dll:
                result = speech.get_device()
                mock_cuda.assert_called_once_with()
                self.assertEqual(result,"cuda")
                mock_add_dll.assert_called_once_with("C:\\fake\\cuda\\bin")

    def test_cpu(self):
        with patch("speech.get_cuda", return_value = None) as mock_get_cuda:
            with patch("speech.os.add_dll_directory") as mock_add_dll:
                result = speech.get_device()
                self.assertEqual(result, "cpu")
                mock_add_dll.assert_not_called()

    def test_process_recording_valid_command(self):
        fake_segment = MagicMock()
        fake_segment.text = "launch steam"
        fake_model = MagicMock()
        fake_model.transcribe.return_value = ([fake_segment], None)
        fake_recording = np.array([[0.0]])

        with patch("speech.model", fake_model):
            with patch("speech.launcher.launch_application") as mock_launch:
                speech.process_recording(fake_recording)
                mock_launch.assert_called_once_with(config.applications["steam"])

    def test_process_recording_invalid_command(self):
        fake_segment = MagicMock()
        fake_segment.text = "launch potato"

        fake_model = MagicMock()
        fake_model.transcribe.return_value = ([fake_segment], None)

        fake_recording = np.array([[0.0]])

        with patch("speech.model", fake_model):
            with patch("speech.launcher.launch_application") as mock_launch:
                speech.process_recording(fake_recording)
                mock_launch.assert_not_called()
