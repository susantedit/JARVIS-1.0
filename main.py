import os
import eel

from engine.features import *
from engine.command import *
from engine.auth import recoganize
def start():
    
    eel.init("www")

    playAssistantSound()
    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Let's begin the face authentication process. Kindly sit in front of the camera, look straight ahead, and remain still while I capture your facial data")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face authentication has been successfully completed. Your identity has been verified, and you now have secure access to the system ")
            eel.hideFaceAuthSuccess()
            speak(" welcome, Sir. Your AI assistant is online and ready. How may I assist you today?")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("I'm sorry, the face authentication was not successful. Kindly try again")
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)