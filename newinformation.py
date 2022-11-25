from menu import UI
from json import load, dump
from time import sleep
from color import color

ui = UI()


# [0] Exit And Save
# [1] Change All Settings
# [2] Change Token
# [3] Change Channel
# [4] Change Sleep Mode
# [5] Change Exp Mode
# [6] Change Runner Mode
# [7] Change Pray/Curse Mode
# [8] Change Sell Settings
# [9] Change Prifix Commands
# [10] Change Gem Mode
# [11] Change Casino Time
# [12] Change Sound Channel
# [13] Change Webhook Mode
# [14] Change TwoCaptcha Captcha
# [15] Change Stop Captcha

def main():
    with open("settings.json", "r") as f:
        data = load(f)
    ui.newData()
    choice = input(f"{color.okgreen}Enter Your Choice:  {color.reset}")
    if choice == "0":

        pass
    elif choice == "1":
        token(data,True)
        channel(data,True)
        sleep(data,True)
        exp(data,True)
        runner(data,True)
        praycurse(data,True)
        sell(data,True)
        prefix(data,True)
        gem(data,True)
        casino(data,True)
        sound(data,True)
        webhook(data,True)
        twocaptcha(data,True)
        stop(data,True)




    elif choice == "2":
        token(data, False)
    elif choice == "3":
        channel(data, False)
    elif choice == "4":
        sleep(data, False)
    elif choice == "5":
        exp(data, False)
    elif choice == "6":
        runner(data, False)
    elif choice == "7":
        praycurse(data, False)
    elif choice == "8":
        sell(data, False)
    elif choice == "9":
        prefix(data, False)
    elif choice == "10":
        gem(data, False)
    elif choice == "11":
        casino(data, False)
    elif choice == "12":
        sound(data, False)
    elif choice == "13":
        webhook(data, False)
    elif choice == "14":
        twocaptcha(data, False)
    elif choice == "15":
        stop(data, False)

    else:
        print(f"{color.fail}[INFO] {color.reset}Invalid Choice")


def token(data, all):
    data['token'] = input("Please Enter Your Account Token: ")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def c(data, all):
    data['channel'] = input("Please Enter Your Channel ID: ")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def runner(data, all):
    data['rhunt'] = input("Do you want to owo hunt automatic?: (YES/NO)")
    data['rbattle'] = input("Do you want to owo battle automatic?: (YES/NO)")
    data['rowo'] = input("Do you want to say owo automatic?: (YES/NO)")
    data['rbuyring'] = input("Do you want to buy ring (item1) automatic?: (YES/NO)")

    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def pm(data, all):

    data['pm'] = input("Toggle Automatically Send Pray/Curse/No (PRAY/CURSE/NO): ")
    if data['pm'].lower() == "pray" or data['pm'].lower() == "curse":
        data['prayid'] = input("Do You Want To Pray/Curse A Specified User? If Yes Enter UserID. Otherwise Enter \"None\":")
    else:
        data['prayid'] = "none"
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def gm(data, all):
    data['gm'] = input("Toggle Automatically Use Gems Mode (YES/NO): ")
    if data['gm'].lower() == "yes":
        data['wcrate'] = input("Toggle Automatically Open Weapon Crate Mode (YES/NO):")
        data['lbox'] = input("Toggle Automatically Open Loot Box Mode (YES/NO):")
        data['usegem'] = input("Muốn xài gem cùi trước hay gem xin trước (DO you prefer using gem from MIN or MAX) [MIN/MAX]:")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def em(data, all):
    data['em'] = input("Toggle Automatically Send Random Text To Level Up (YES/NO): ")
    if data['em'].lower() == 'yes':
        data['channelspam'] = input("Input channel id you want to spam exp(should be a private server): ")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def sm(data, all):
    data['sm'] = input("Toggle Sleep Mode (YES/NO): ")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def webhook(data, all):
    data['webhook'] = input("Toggle Discord Webhook, Enter Webhook Link If You Want It To Ping You If OwO Asked Captcha. Otherwise Enter \"None\": ")
    if data['webhook'].lowwer() != "none":
        data['webhookping'] = input("Do You Want To Ping A Specified User When OwO Asked Captcha? If Yes Enter User ID. Otherwise Enter \"None\": ")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def huntbot(data, all):
    data['rhuntbot'] = input("Toggle Automatically Send Huntbot/Autohunt (YES/NO): ")
    if data['rhuntbot'].lower() == "yes":
        data['sacrifice'] = input("Toggle Automatically Sacrifice all pet after huntbot (YES/NO): ")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def oc(data, all):
    data['prefix'] = input("Toggle Selfbot Commands, You Can Control Your Selfbot Using Commands (YES/NO): ")
    if data['prefix'].lower() == "yes":
        data['prefix'] = input("Enter Your Selfbot Prefix: ")
        data['allowedid'] = input("Do You Want Allow An User To Use Your Selfbot Commands? If Yes Enter The Account ID, Otherwise Enter \"None\": ")
        print("Great! You Can View Selfbot Commands At Option [3] Info At The Main Menu!")
        sleep(1)
    else:
        data['prefix'] = "NO"
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def daily(data, all):
    data['daily'] = input("Toggle Automatically Claim Daily (YES/NO): ")
    if data['daily'].lower() == "no":
        data['daily'] = "None"
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def stop(data, all):
    data['stop'] = input("Toggle Stop After A Specifice Time (YES/NO): ")
    if data['stop'].lower() == "yes":
        data['stop'] = input("Enter Stop Time (Seconds): ")
    else:
        data['stop'] = "NO"
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def sell(data, all):
    data['sell'] = input("Toggle Automatically Sell Animal (YES/NO): ")
    if data['sell'].lower() != "no":
        print("Animal Type: C, U, R, M... (Type \"all\" To Sell All Animals)")
        print("C = Common, U = Uncommon, ect...")
        data['sell'] = input("Enter Animal Type: ")
        file = open("settings.json", "w")
        dump(data, file)
        file.close()
    else:
        data['sell'] = "None"
        file = open("settings.json", "w")
        dump(data, file)
        file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def solve(data, all):
    data['solve'] = input("Toggle Automatically Solve Captcha With AI (YES/NO): ")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def casinom(data, all):
    data['casinom'] = input("Do you want to play Casino (YES/NO): ")
    if data['casinom'].lower() == "yes":
        data['channelocf'] = input("Do you want to play Casino in the special server? If Yes Enter Channel ID, Otherwise Enter \"None\" ")
        data['maxbet'] = input("Are you prefer all in to die or reset bet when the bet > 150k ? (AllIn/Reset): ")
        data['cfm'] = input("Do you want to play CoinFlip (YES/NO/): ")
        if data['cfm'].lower() == 'yes':
            print(f"{color.okcyan}[INFO] {color.reset}Input Coinflip Information")
            data['cfbet'] = input("Enter Your Bet Amount for CoinFlip (Must Be Integer): ")
            data['cfrate'] = input("Enter Your Bet Rate Multiple for CoinFlip (Ngã ở đâu x? ở đó) (Best is x4) (x2 is not good) (Must Be Integer): ")

        data['osm'] = input("Do you want to play Owo Slot (YES/NO/): ")
        if data['osm'].lower() == 'yes':
            print(f"{color.okcyan}[INFO] {color.reset}Input Coinflip Information")
            data['osbet'] = input("Enter Your Bet Amount for OwoSlot (Must Be Integer): ")
            data['osrate'] = input("Enter Your Bet Rate Multiple for OwoSlot (Ngã ở đâu x? ở đó) (Best is x3) (x2 is not good) (Must Be Integer): ")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def sound(data, all):
    data['sound'] = input("Do you want to ping by music?: (YES/NO)")

    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


def api(data, all):
    data['api'] = input("Do you have API 2Capcha, Enter API 2 Capcha If You have. Otherwise Enter \"None\". :")
    file = open("settings.json", "w")
    dump(data, file)
    file.close()
    print(f"{color.okcyan}[INFO] {color.reset}Successfully Saved!")
    if not all:
        main()


if __name__ == "__main__":
    main()

