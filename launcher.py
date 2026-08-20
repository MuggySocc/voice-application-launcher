import subprocess
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

logger = logging.getLogger(__name__)

def launch_application(app):
    if app["type"] == "executable":
        try:
            subprocess.Popen(app["target"])
        except FileNotFoundError:
            logger.error("Executable not found")
    elif app["type"] == "steam": 
        if app["target"] and app["target"].isdigit():
            steam_uri = f"steam://rungameid/{app['target']}"
            os.startfile(steam_uri)
        else:
            logger.error("Steam App ID not found")