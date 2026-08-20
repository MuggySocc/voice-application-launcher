import subprocess
import os

def launch_applcation(app):
    if app["type"] == "executable":
        try:
            subprocess.Popen(app["target"])
        except FileNotFoundError:
            print("Executable could not be found")    
    elif app["type"] == "steam":
        steam_uri = f"steam://rungameid/{app['target']}"
        os.startfile(steam_uri)
        #subprocess.Popen(app["target"])