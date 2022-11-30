from signal import signal, SIGINT
import os
from os import execl, name, system
from time import sleep, strftime, localtime, time
from requests import get, post
from base64 import b64encode
import atexit
import random
from re import findall
import json
import threading

import base64
import requests

from colorama import init

init()




try:
    from playsound import playsound
    from twocaptcha import TwoCaptcha
    from inputimeout import inputimeout, TimeoutOccurred
    from discum import *
    from discum.utils.slash import SlashCommander
    from discord_webhook import DiscordWebhook
except Exception as e:

    from setup import install
    install()
    from playsound import playsound
    from twocaptcha import TwoCaptcha
    from inputimeout import inputimeout, TimeoutOccurred
    from discum import *
    from discum.utils.slash import SlashCommander
    from discord_webhook import DiscordWebhook


from information import information
from menu import UI
from color import color
from casino import casinos
from gem import gems
from webhook import webhooks
from music import musics
from function import functions
from runner import runners
from spam import spam
from exception import exception

client = information()
ui = UI()
function = functions()


if client.twocaptcha['enable']:
    api_key = os.getenv('APIKEY_2CAPTCHA', client.twocaptcha['api'])
    solver = TwoCaptcha(api_key, defaultTimeout=100, pollingInterval=5)


token = client.token
# Bot Information
bot = discum.Client(token=token, log=False, build_num=0, x_fingerprint="None", user_agent=[
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36/PAsMWa7l-11',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 YaBrowser/20.8.3.115 Yowser/2.5 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.7.2) Gecko/20100101 / Firefox/60.7.2'])
casino = casinos(bot)
gem = gems(bot)
webhook = webhooks(bot)
music = musics(bot)
runner = runners(bot)
spam = spam(bot)

kiepdoden = music.kiepdoden()
solvedmusic = music.solvedmusic()
captchamusic = music.captchamusic()


def at(self):
    return f'\033[0;43m{strftime("%d %b %Y %H:%M:%S", localtime())}\033[0;21m'
@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
        for i in range(len(bot.gateway.session.DMIDs)):
            if client.OwOID in bot.gateway.session.DMs[bot.gateway.session.DMIDs[i]]['recipients']:
                client.dmsid = bot.gateway.session.DMIDs[i]
        user = bot.gateway.session.user
        client.username = user['username']
        client.userid = user['id']
        client.guild_id = bot.getChannel(client.channel).json()['guild_id']
        client.guild_name = bot.gateway.session.guild(client.guild_id).name

        ui.slowPrinting(f"\nLogged in as {color.yellow}{user['username']}#{user['discriminator']}{color.reset}")
        sleep(1)


        print('═' * 25)




@bot.gateway.command
def CheckHuntBot(resp):
    def getPassword(img, lenghth,code):
        count = 0
        timeanswer = time()
        while True:
            count += 1
            r = solver.normal(img, numeric=2, minLen=lenghth, maxLen=lenghth, phrase=0, caseSensitive=0, calc=0, lang='en' )

            if r['code'].isalpha():
                if len(r['code']) == lenghth:
                    if r['code'] !=code:
                        print('Check result 2captcha')
                        return r
                    else:
                        solver.report(r['captchaId'], False)
                        print(f'Time: {count}. The result {r["code"]} is not right.Try again')
                else:
                    solver.report(r['captchaId'], False)
                    print(f'Time: {count}. The length of result {r["code"]} is not right.Try again')
            else:
                solver.report(r['captchaId'], False)
                print(f'Time: {count}. The result {r["code"]} contants number.Try again')

    def solvepassword(image_url,msgs):
        if not client.twocaptcha['enable'] and client.solve['enable']:
            user = bot.gateway.session.user
            from api import CAPI
            api = CAPI(client.userid, client.solve['server'])
            encoded_string = b64encode(get(image_url).content).decode('utf-8')
            r = api.solve(Json={'data': encoded_string, 'len': msgs[msgs.find("letter word") - 2]})
            if r:
                ui.slowPrinting(f"{color.okcyan}[INFO] {color.reset}Solved Password huntbot [Code: {r['code']}]")
                bot.typingAction(str(client.channel))
                sleep(3)
                bot.sendMessage(str(client.channel), f"owo hb 30000 {r['code']}")
                print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo hb 30000 {r['code']}")
                msgs = bot.getMessages(str(client.channel), num=10)
                msgs = msgs.json()
                for i in range(len(msgs)):
                    if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'I WILL BE BACK IN' in msgs[i]['content'] and not client.stopped:
                        api.report(Json={'captchaId': r['captchaId'], 'correct': 'True'})
                        print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [INFO] {color.reset} Password huntbot is right")
                    if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'WRONG PASSWORD' in msgs[i]['content'] and not client.stopped:
                        api.report(Json={'captchaId': r['captchaId'], 'correct': 'False'})
                        print(f"{at()}{color.okcyan} User: {client.username}{color.warning} [WARNING] {color.reset} Password huntbot is wrong")
                    if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'have enough' in msgs[i]['content'] and not client.stopped:
                        print(f"{at()}{color.okcyan} User: {client.username}{color.warning} [WARNING] {color.reset} You dont have enough Cowocy")
        if client.twocaptcha['enable']:
            encoded_string = b64encode(get(image_url).content).decode('utf-8')
            countlen = 5 #password always has 5 characters
            captchabalance = solver.balance()
            if captchabalance == 0:
                print(f'Balance 2CAPCHA : {captchabalance} $ Out of money')
                webhook.webhookPing(f"<@{client.webhook['pingid']}> [FAIL]Out of money . User: {client.username} <@{client.userid}>")
                webhook.webhookPing(f"=========================================================================================")
                print(f"{at()}{color.okcyan} User: {client.username}{color.warning} [WARNING] {color.reset} You dont have enough Money in 2Captcha Balance")
                # Solve by 2Captcha
                r = getPassword(encoded_string, countlen,0)

                captchabalance = solver.balance()
                print(f'Balance TwoCaptcha : {captchabalance} $')
                print(f"{color.okcyan}[INFO] {color.reset}Solving Password at 1st chance: [Code: {r['code']}]")

                bot.typingAction(str(client.channel))
                sleep(3)
                bot.sendMessage(str(client.channel), f"owo hb 30000 {r['code']}")
                print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo hb 30000 {r['code']}")

                msgs = bot.getMessages(str(client.channel), num=10)
                msgs = msgs.json()
                for i in range(len(msgs)):
                    if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'I WILL BE BACK IN' in msgs[i]['content'] and not client.stopped:
                        solver.report(r['captchaId'], True)
                        print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [INFO] {color.reset} Password huntbot is right")

                    if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'WRONG PASSWORD' in msgs[i]['content'] and not client.stopped:
                        solver.report(r['captchaId'], False)
                        print(f"{at()}{color.okcyan} User: {client.username}{color.warning} [WARNING] {color.reset} Password huntbot is wrong.Try again")
                        r2 = getPassword(encoded_string, countlen,r['code'])
                        captchabalance = solver.balance()
                        print(f'Balance TwoCaptcha : {captchabalance} $')
                        print(f"{color.okcyan}[INFO] {color.reset}Solving Password at 2nd chance: [Code: {r2['code']}]")

                        bot.typingAction(str(client.channel))
                        sleep(3)
                        bot.sendMessage(str(client.channel), f"owo hb 30000 {r['code']}")
                        print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [SENT] {color.reset} owo hb 30000 {r['code']}")

                        msgs = bot.getMessages(str(client.channel), num=10)
                        msgs = msgs.json()
                        for i in range(len(msgs)):
                            if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'I WILL BE BACK IN' in msgs[i]['content'] and not client.stopped:
                                solver.report(r['captchaId'], True)
                                print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [INFO] {color.reset} Password huntbot is right")

                            if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'WRONG PASSWORD' in msgs[i]['content'] and not client.stopped:
                                solver.report(r['captchaId'], True)
                                print(f"{at()}{color.okcyan} User: {client.username}{color.okgreen} [INFO] {color.reset} Password huntbot is Wrong")

                            if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'have enough' in msgs[i]['content'] and not client.stopped:
                                print(f"{at()}{color.okcyan} User: {client.username}{color.warning} [WARNING] {color.reset} You dont have enough Cowocy")

                    if client.username in msgs[i]['content'] and msgs[i]['author']['id'] == client.OwOID and 'have enough' in msgs[i]['content'] and not client.stopped:
                        print(f"{at()}{color.okcyan} User: {client.username}{color.warning} [WARNING] {color.reset} You dont have enough 30k Cowocy")
