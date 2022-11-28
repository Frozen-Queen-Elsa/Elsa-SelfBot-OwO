from version import Version
from requests import get
from color import color
from menu import UI
from time import sleep
from re import findall
from inputimeout import TimeoutOccurred, inputimeout
import json

ui = UI()


class information:
    def __init__(self):
        self.wbm = [13, 18]
        self.OwOID = '408785106942164992'
        self.totalcmd = 0
        self.totaltext = 0
        self.username = ""
        self.userid = ""
        self.guild_id=""
        self.guild_name=""
        self.checknogem = False
        self.stopped = False
        self.version = int(''.join(map(str, Version)))
        self.wait_time_daily = 60
        self.wait_time_huntbot = 60
        self.channel2 = []
        # CASINO
        self.checknocash = False
        self.totalwon = 0
        self.totallost = 0
        self.checknocash = False
        self.countcfmaxlost = 0
        self.countosmaxlost = 0
        self.currentcfbet = 0
        self.currentosbet = 0
        # Gems
        self.checkgemtime = 0
        self.checkusegem = 0
        self.skipcheckgem = 0

        with open('owosettings.json', "r") as file:
            data = json.load(file)
            self.token = data['token']
            self.channel = data['channel']
            # Sleepmode
            self.sleep = data['sleep']
            # Spam exp
            self.exp = data['exp']
            # runner
            self.runner = data['runner']
            # Pray
            self.praycurse = data['praycurse']
            # prefix
            self.prefix = data['prefix']
            # sell
            self.sell = data['sell']
            # UseGem
            self.gem = data['gem']
            # Casino
            self.casino = data['casino']
            # Sound
            self.sound = data['sound']
            # Webhook
            self.webhook = data['webhook']
            # Solve
            self.solve = data['solve']
            # 2Captcha
            self.twocaptcha = data['twocaptcha']
            # Huntbot
            self.huntbot = data['huntbot']
        self.tokenbackup = self.token
        self.channelspambackup = self.exp['channelspamid']

        self.listfabled = [
            'fabled',
            'dboar',
            'deagle',
            'dfrog',
            'dgorilla',
            'dwolf'
        ]
        self.listhidden = [
            'hidden',
            'hkoala',
            'hlizzard',
            'hsnake',
            'hsquid',
            'hmonkey'
        ]
        self.listbotrank = [
            'botrank',
            'dinobot',
            'giraffbot',
            'hedgebot',
            'lobbot',
            'slothbot'
        ]
        self.listdistored = [
            'distorted',
            'glitchparrot',
            'glitchotter',
            'glitchraccoon',
            'glitchflamingo',
            'glitchzebra'
        ]


    def Version(self):
        response = get("https://raw.githubusercontent.com/ahihiyou20/discord-selfbot-owo-bot/development/source/src/version.py")
        version = response.text
        version = findall(r'\b\d+\b', version)
        return int(''.join(version))

    def check(self):
        version = self.Version()
        if self.token and self.channel == 'nothing':
            print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
            sleep(2)
            from newinformation import main
            main()
        else:
            response = get('https://discord.com/api/v9/users/@me', headers={"Authorization": self.token})
            if response.status_code != 200:
                print(f"{color.fail} !!! [ERROR] !!! {color.reset} Invalid Token")
                sleep(2)

a = information()
a.check()
