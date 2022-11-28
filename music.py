from playsound import playsound
from information import information
client = information()

class musics:
    def __init__(self, bot):
        self.bot = bot

    def captchamusic(self):
        if client.sound == 'yes':
            playsound('KhueMocLang.mp3')
            #playsound('Files/Captcha.mp3')

    def solvedmusic(self):
        if client.sound == 'yes':
            playsound('Solved.mp3')

    def kiepdoden(self):
        if client.sound == 'yes':
            playsound("KiepDoDen.mp3")