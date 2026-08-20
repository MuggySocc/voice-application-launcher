import unittest
from unittest.mock import patch
import launcher


class TestLauncher(unittest.TestCase):

    def test_launch_executable(self):
        app = {"type":"executable",
            "target":r"C:\fake\steam.exe"}
        with patch("launcher.subprocess.Popen") as mock_open:
            launcher.launch_application(app)
            mock_open.assert_called_once_with(app["target"])

    def test_launch_steam(self):
        app = {"type":"steam",
               "target":"1422450"}
        with patch("launcher.os.startfile") as mock_startfile:
            launcher.launch_application(app)
            mock_startfile.assert_called_once_with(f"steam://rungameid/{app['target']}")
