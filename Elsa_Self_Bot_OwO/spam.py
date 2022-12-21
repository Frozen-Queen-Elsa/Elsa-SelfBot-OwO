from information import information
from time import sleep, strftime, localtime
from color import color
from requests import get
import random

client = information()

class spam:
    def __init__(self, bot):
        self.bot = bot

    def at(self):
        return f'\033[0;43m{strftime("%d %b %Y %H:%M:%S", localtime())}\033[0;21m'

    def exp(self,channel_spam,username):

        try:
            response = get("https://zenquotes.io/api/random")

            if response.status_code == 200:
                json_data = response.json()

                data = json_data[0]
                self.bot.sendMessage(str(channel_spam), data['q'])
                print(f'{self.at()}{color.reset}{color.okcyan} User: {username}{color.okcyan} [SPAM] {color.reset}')
                client.totaltext += 1
                sleep(random.randint(1, 6))
                if channel_spam!=client.channel:
                    msgs = self.bot.getMessages(str(channel_spam), num=3)
                    msgs = msgs.json()
                    for i in range(len(msgs)):
                        if msgs[i]['author']['username'] == username:
                            self.bot.deleteMessage(channel_spam, msgs[i]['id'])
                            guildid = self.bot.getChannel(channel_spam).json()['guild_id']
                            guildname = self.bot.gateway.session.guild(guildid).name
                            print(f'{self.at()}{color.reset}{color.okcyan} User: {username}{color.fail} [Delete SPAM] {color.cyan}at server {color.yellow}{guildname}{color.reset}')
                            sleep(0.5)
        except:
            pass
