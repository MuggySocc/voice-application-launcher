import speech
import unittest
from unittest.mock import patch

class TestSpeech(unittest.TestCase):

    def test_cuda(self):
        with patch("speech.get_cuda", return_value=r"C:\fake\cuda\bin") as mock_cuda:
            with patch("speech.os.add_dll_directory") as mock_add_dll:
                result = speech.get_device()
                mock_cuda.assert_called_once_with()
                self.assertEqual(result,"cuda")
                mock_add_dll.assert_called_once_with("C:\\fake\\cuda\\bin")

    def test_cpu(self):
        with patch("speech.get_cuda", return_value = None) as mock_cpu:
            with patch("speech.os.add_dll_directory") as mock_add_dll:
                result = speech.get_device()
                self.assertEqual(result, "cpu")
                mock_add_dll.assert_not_called()

