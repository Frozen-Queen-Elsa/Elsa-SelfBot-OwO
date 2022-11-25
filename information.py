from version import Version
from requests import get
from color import color
from menu import UI
from time import sleep
from re import findall
from inputimeout import TimeoutOccurred, inputimeout
import json

class information:
	def __init__(self):
		#BASIC
		self.OwOID = '408785106942164992'
		self.totalcmd = 0
		self.totaltext = 0
		self.username=""
		self.userid = ""
		self.checknogem=False
		self.stopped = False
		self.startloop=False
		self.dmsID = None
		#self.version = int(''.join(map(str, Version)))
		self.wait_time_daily = 60
		self.channel2 = []
		self.CheckRunningAuto=False
		self.FlagRunAuto=False
		
		#CASINO
		self.checknocash=False
		self.totalwon=0
		self.totallost=0
		self.checknocash=False
		self.countcfmaxlost=0
		self.countosmaxlost=0
		self.currentcfbet=0
		self.currentosbet=0
  
		#Gems
		self.checkgemtime=0
		self.checkusegem = 0
		self.skipcheckgem=0



		with open("settingsOWO.json", "r") as file:
			data = json.load(file)
			self.token=data['token']
			self.channel=data['channel']
			#Sleepmode
			self.sleep=data['sleep']
			#Spam exp
			self.exp=data['exp']
			#runner
			self.runner=data['runner']
			#Pray
			self.praycurse=data['praycurse']  
			#prefix
			self.prefix=data['prefix']
			#UseGem
			self.gem=data['gem']
			#Casino
			self.casino=data['casino']
			#Sound
			self.sound=data['sound']          
			#Webhook
			self.webhook=data['webhook'] 
			#2Captcha      
			self.twocaptcha=data['twocaptcha']

		self.listfabled=[
			'fabled',
			'dboar',
			'deagle',
			'dfrog',
			'dgorilla',
			'dwolf'
		]
		self.listhidden=[
			'hidden',
			'hkoala',
			'hlizzard',
			'hsnake',
			'hsquid',
			'hmonkey'	
		]
		self.listbotrank=[
			'botrank',
			'dinobot',
			'giraffbot',
			'hedgebot',
			'lobbot',
			'slothbot'	
		]
		self.listdistored=[
			'distorted',
			'glitchparrot',
			'glitchotter',
			'glitchraccoon',
			'glitchflamingo',
			'glitchzebra'	
		]   

a = information()

