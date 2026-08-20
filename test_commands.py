import unittest
import commands

class TestCommands(unittest.TestCase):

    def test_launch_steam(self):
        result = commands.parse_command("launch steam")
        self.assertEqual(result,("launch", "steam"))

    def test_launch_deadlock(self):
        result = commands.parse_command("launch dead lock")
        self.assertEqual(result, ("launch", "deadlock"))

    def test_incomplete_command(self):
        result = commands.parse_command("launch")
        self.assertEqual(result, (None, None))