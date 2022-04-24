from __future__ import division
import requests, os, sys, random, time, socket, subprocess, pathlib, json, os.path, colorama, re, nexmo,queue, vonage,threading,datetime
import smtplib, ssl
from email.mime.text import MIMEText
from datetime import datetime
from nexmo import Sms
import time
from nexmo.sms import Sms
from bs4 import BeautifulSoup
from colorama import Fore, Style, Back
from os import path
from twilio.rest import Client
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import smtplib
from asciimatics.effects import Stars, Print
from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, \
    PalmFirework
from asciimatics.renderers import SpeechBubble, FigletText, Rainbow
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
from random import randint, choice
import sys
import configparser
from time import strftime, sleep
import time , sys
import time , sys


try:
    import requests
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install requests'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    


try:
    import asciimatics
    
except:
    def main():      
        import os, subprocess
        update_pip = 'pip install asciimatics'
        subprocess.call(update_pip, shell=True , stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()

try:
    import selenium
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install selenium'
        update_pip2 = 'pip install selenium-chrome'
        update_pip3 = 'pip install selenium-browser'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.call(update_pip2, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.call(update_pip3, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    
try:
    import phone_gen
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install phone-gen'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    
try:
    import phonenumbers
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install phonenumbers'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    
try:
    import termcolor
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install termcolor'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    
try:
    import pathlib
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install pathlib'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    
try:
    import colorama
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install colorama'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()
    
try:
    import licensing
    
except:
    def main():
        import os, subprocess
        update_pip = 'pip install licensing'
        subprocess.call(update_pip, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    main()

    
import sys
from pyfiglet import Figlet
from asciimatics.effects import Scroll, Mirage, Wipe, Cycle, Matrix, \
    BannerText, Stars, Print
from asciimatics.particles import DropScreen
from asciimatics.renderers import FigletText, SpeechBubble, Rainbow, Fire
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import time
import os
import tempfile
import requests
import pathlib
import subprocess
def create_path():
    if not os.path.exists('Crackers/twilio'):
        os.makedirs('Crackers/twilio')
    if not os.path.exists('Crackers/Nexmo'):
            os.makedirs('Crackers/Nexmo')
    if not os.path.exists('Crackers/send99'):
            os.makedirs('Crackers/send99')
    if not os.path.exists('Crackers/smsala'):
            os.makedirs('Crackers/smsala')
    if not os.path.exists('Crackers/plivo'):
            os.makedirs('Crackers/plivo')
    if not os.path.exists('Checker/Number-check'):
            os.makedirs('Checker/Number-check')
    if not os.path.exists('Checker/Amz-check'):
            os.makedirs('Checker/Amz-check')
    if not os.path.exists('Checker/PayPal-check'):
            os.makedirs('Checker/PayPal-check')


create_path()
colorama.init()

fg = [
    '\033[91;1m',  # RED     0
    '\033[92;1m',  # GREEN   1
    '\033[93;1m',  # YELLOW  2
    '\033[94;1m',  # BLUE    3
    '\033[95;1m',  # MAGENTA 4
    '\033[96;1m',  # CYAN    5
    '\033[97;1m'  # WHITE   6
]


def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
def _credits(screen):
    scenes = []

    text = Figlet(font="banner", width=200).renderText("xMarvel")
    width = max([len(x) for x in text.split("\n")])

    effects = [
        Print(screen,
              Fire(screen.height, 80, text, 0.4, 40, screen.colours),
              0,
              speed=1,
              transparent=False),
        Print(screen,
              FigletText("xMarvel", "banner"),
              screen.height - 9, x=(screen.width - width) // 2 + 1,
              colour=Screen.COLOUR_BLACK,
              bg=Screen.COLOUR_BLACK,
              speed=1),
        Print(screen,
              FigletText("xMarvel", "banner"),
              screen.height - 9,
              colour=Screen.COLOUR_WHITE,
              bg=Screen.COLOUR_WHITE,
              speed=1),
    ]
    scenes.append(Scene(effects, 30))

    effects = [
        Matrix(screen, stop_frame=200),
        Mirage(
            screen,
            FigletText("xMarvel"),
            screen.height // 2 - 3,
            Screen.COLOUR_GREEN,
            start_frame=100,
            stop_frame=200),
        Wipe(screen, start_frame=150),
        Cycle(
            screen,
            FigletText("xMarvel"),
            screen.height // 2 - 3,
            start_frame=200)
    ]
    scenes.append(Scene(effects, 100, clear=False))

    effects = [
        Print(screen,
              SpeechBubble("Press 'X' to Continue."), screen.height // 2 - 1, attr=Screen.A_BOLD)
    ]
    scenes.append(Scene(effects, -1))

    screen.play(scenes)



    


os.system('cls')

def Auth_check():
    from random import choice
    os.system('cls')
    clear = "\x1b[0m"

    colors = [36, 32, 34, 35, 31, 37]
    x = """ 

                        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                        ┃                ▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               ┃
                        ┃            ▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               ┃
                        ┃              █ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               ┃   
                        ┃             ▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            ┃
                        ┃            █   ▀▄    █     █   █    █  █  ▀███▀       ▀           ┃
                        ┃             ▀       ▀     █   ▀      █▐                           ┃
                        ┃                          ▀           ▐                            ┃
                        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
                        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
		          ┃	                    [+] Check License Key ...	              ┃
            	          ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                                                                                             
                           """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
        time.sleep(0.05)

    def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
        if iteration == total:
            print()

    items = list(range(0, 50))
    l = len(items)

    loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
    for i, item in enumerate(items):
        sleep(0.0000001)
        loadbar(i + 1, l, prefix='                          Progress:', suffix='Complete', length=l)

    def get_login():
        hwid = '71B8DB30-0649-11EC-9610-D98F38B383DF'
        if hwid:
            pass
        else:
            clear = "\x1b[0m"
            colors = [31]
            x = """

                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                      ┃                 Error! License Not I Database!"                   ┃
                      ┃       Please contact (@xMarveL_ADMiN IN Telegram ) for help.      ┃
                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                                                                                            
                                      """
            for N, line in enumerate(x.split("\n")):
                sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
                time.sleep(0.05)
            sys.exit()

    get_login()

    def Services():
        os.system('cls')
        fg = Fore.GREEN
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37]
        x = f""" 

                                ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                ┃                ▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               ┃
                                ┃            ▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               ┃
                                ┃              █ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               ┃   
                                ┃             ▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            ┃
                                ┃            █   ▀▄    █     █   █    █  █  ▀███▀       ▀           ┃
                                ┃             ▀       ▀     █   ▀      █▐                           ┃
                                ┃                          ▀           ▐                            ┃
                                ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
        ┏━━━━━━━━━━━━━┓
        ┃   Senders   ┃
        ┗━━━━━━━━━━━━━┛
                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    ┃  [   1   ]  Twilio Bulk Sender           [ 10 ] SMSPLACE  Sender [ NEW ]   ┃
                    ┃  [   2   ]  Nexmo Bulk Sender            [ 11 ] AMZ SNS Sender [ NEW ]     ┃
                    ┃  [   3   ]  Send99 Bulk Sender           [ 12 ] Karix Sender    [ New ]    ┃
                    ┃  [   4   ] xMarvel Private Sender        [ 13 ] Telesign Sender  [ New ]   ┃
                    ┃  [   5   ] SMSALA Bulk Sender            [ 14 ] Textbelt Sender  [ New ]   ┃
                    ┃  [   6   ] BulkSMS  Sender       	 [ 15 ] SMS77 Sms Sender[ NEW ]    ┃
                    ┃  [   7   ] BulkGate Sender               [ 16 ] SMSBEEP Sms Sender[ NEW ]  ┃
                    ┃  [   8   ] Plivo SENDER                  [ 17 ] PROOVL Sms Sender[ NEW ]   ┃
                    ┃  [   9   ] MSGBIRD SENDER                [ 18 ] phcomm Sms Sender[ NEW ]   ┃
                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        ┏━━━━━━━━━━━━━━━━┓
        ┃    Crackers    ┃
        ┗━━━━━━━━━━━━━━━━┛
                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    ┃    [   19   ] Twilio Mass Checker         [ 20 ] SEND99 Mass Checker       ┃
                    ┃    [   21   ] Nexmo Mass Checker          [ 22 ] SMSALA Mass Checker       ┃
                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                             ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        ┏━━━━━━━━━━━━━━━━┓
        ┃    Checkers    ┃ [ New ] 9/2021
        ┗━━━━━━━━━━━━━━━━┛
                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                    ┃  [   23   ] Amazon Number Checker           [   24   ] Fast Number Checker ┃
                    ┃  [   25   ] Number Carrier Checker          [   26   ] Number Generator    ┃
                    ┃                      [   27   ] PayPal Number Checker                      ┃
                    ┃  [   28   ] Yahoo Number Checker            [   29   ] Aol Number Checker  ┃
                    ┃  [   30   ] Office365 Number Checker        [   31   ] USAA Number Checker ┃
                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            
                             ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        ┏━━━━━━━━━━━━━━┓
        ┃    Others    ┃
        ┗━━━━━━━━━━━━━━┛
            [ 99 ] Check Updates 
                                   """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
            time.sleep(0.05)

    Services()
    def choose_service():
        fg = [
            '\033[91;1m',  # RED     0
            '\033[92;1m',  # GREEN   1
            '\033[93;1m',  # YELLOW  2
            '\033[94;1m',  # BLUE    3
            '\033[95;1m',  # MAGENTA 4
            '\033[96;1m',  # CYAN    5
            '\033[97;1m'  # WHITE   6
        ]
        pc_name = socket.gethostname()
        currnet_dir = pathlib.Path(__file__).parent.absolute()
        Choice = input(f'root@xMarvel:/{currnet_dir}/#  $ ')
        if Choice == '1':
            os.system('cls')
            print('''
                                {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
                                {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
                                {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
                                {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
                                {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
                                {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
                                {2} ┃                          {0}▀           ▐                            {2}┃
                                {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                                {2} ┃         {0}Twilio Bulk SENDER        {2}┃         {0}CODED BY xMarvel      {2}┃
                                {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

                                '''.format(fg[0], fg[1], fg[5], fg[4]))

            read_config = configparser.ConfigParser()
            read_config.read("Senders-configs/Twilio_Config.ini")

            SID = read_config.get("Section1", "Accountsid")
            secret_key = read_config.get("Section1", "SecretKey")
            Twilio_Number = read_config.get("Section1", "Twilionumber")
            MSG = read_config.get("Section1", "Message")
            auth = (SID, secret_key)
            curler_balance = requests.get("https://api.twilio.com/2010-04-01/Accounts/" + SID + "/Balance.json",auth=auth).text
            info_balance = json.loads(curler_balance)
            usdbalance = info_balance['balance']
            Msg_can_sent = round(float(usdbalance) / float(0.0075))
            all_data = "Account sid : "+SID+'|'+"Token: "+secret_key+'\n' +"balance : "+usdbalance+'\n'+"Phone Number : "+Twilio_Number+'\n'
            print(Fore.GREEN + '''
                                 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                 ┃                          [+] TWILIO CONFIG [+]                          ┃
                                 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
            ''')
            print(f'''
                                 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                 ┃    Account Sid                  ┃{SID}     ┃
                                 ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                                 ┃    Secret Key                   ┃{secret_key}       ┃
                                 ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                                 ┃    Number Or Sender ID          ┃{Twilio_Number}                           ┃
                                 ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                                 ┃    API Balance                  ┃{usdbalance}                                 ┃
                                 ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                                 ┃    SMS ABLE TO SENT [ USA ]     ┃{Msg_can_sent}                                   ┃
                                 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')

            cod = "+"
            reseee = Style.RESET_ALL
            list = input(f"          \033[0;37;45mYour Number List:~#{reseee} ")
            from twilio.rest import Client
            import time
            number = sum(1 for line in open(list))
            msg = MSG
            cod = "+"

            openit = open(list, 'r')
            for i in range(0, number):
                time.sleep(3)
                recipent = cod + str(openit.readline())
                account_sid = SID
                auth_token = secret_key
                locsf = Client(account_sid, auth_token)
                message = locsf.messages \
                    .create(
                    body=MSG,
                    from_=Twilio_Number,
                    to=recipent
                )
                sidd = message.sid
                print(f'''
                    -------------------------
                    \033[0;37;41mMessage ID :- {sidd}{reseee}
                    \033[0;37;41mNumber :- {recipent}{reseee}
                    \033[0;37;41mStatues :- Sent !{reseee}
                    -------------------------
                                    ''')
        elif Choice == '2':
            print('''
            {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
            {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
            {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
            {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
            {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
            {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
            {2} ┃                          {0}▀           ▐                            {2}┃
            {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {2} ┃         {0}Nexmo Bulk SENDER         {2}┃         {0}CODED BY xMarvel      {2}┃
            {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

            '''.format(fg[0], fg[1], fg[5], fg[4]))

            read_config = configparser.ConfigParser()
            read_config.read("Senders-configs/Nexmo_Config.ini")

            Api_key = read_config.get("Section1", "API_KEY")
            secret_key = read_config.get("Section1", "SecretKey")
            Sender_id = read_config.get("Section1", "Sender_Id")
            MSG = read_config.get("Section1", "Message")
            client = vonage.Client(key=Api_key, secret=secret_key)
            result = client.get_balance()
            usd_bal = (f"{result['value']:0.2f}")
            Msg_can_sent = round(float(usd_bal) / float(0.0065))
            print('''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃                          [+] Nexmo CONFIG [+]                           ┃
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                        ''')
            print(f'''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃    API KEY                      ┃{Api_key}                               ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Secret Key                   ┃{secret_key}                       ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Sender ID                    ┃{Sender_id}                                ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    API Balance                  ┃{usd_bal} EUR                               ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    SMS ABLE TO SENT [ USA ]     ┃{Msg_can_sent}                                    ┃
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
            cod = "+"

            reseee = Style.RESET_ALL
            list = input(f"          \033[0;37;45mYour Number List:~#{reseee} ")
            number = sum(1 for line in open(list))
            openit = open(list, 'r')
            client = nexmo.Client(key=Api_key, secret=secret_key)
            sms = Sms(client)
            for i in range(0, number):
                recipent = cod + str(openit.readline())
                url = 'https://rest.nexmo.com/sms/json'
                data = {
                    "from": Sender_id,
                    "text": MSG,
                    "to": recipent,
                    "api_key": Api_key,
                    "api_secret": secret_key,
                }
                rq = requests.post(url, data=data).text
                if '"status": "0"' in rq:
                    print(Fore.GREEN + '''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃   Statues                             ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}                ┃Sent                                   ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                else:
                    print('''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃    Message ID                         ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}           ┃Failed ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                    print(rq)
        elif Choice == '3':
            print('''
            {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
            {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
            {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
            {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
            {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
            {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
            {2} ┃                          {0}▀           ▐                            {2}┃
            {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {2} ┃         {0}Send99 Bulk SENDER        {2}┃         {0}CODED BY xMarvel      {2}┃
            {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

            '''.format(fg[0], fg[1], fg[5], fg[4]))

            read_config = configparser.ConfigParser()
            read_config.read("Senders-configs/Send99_Config.ini")

            Api_Id = read_config.get("Section1", "Api_Id")
            Api_Password = read_config.get("Section1", "Api_Password")
            Sender_id = read_config.get("Section1", "Sender_Id")
            MSG = read_config.get("Section1", "Message")
            Bal_endpoint = f'http://api2.send99.com/api/CheckBalance?api_id={Api_Id}&api_password={Api_Password}'
            bal_req = requests.get(Bal_endpoint).json()
            final_bal = bal_req['BalanceAmount']
            sms_able_to_sent = round(final_bal / 0.015)
            print('''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃                          [+] Send99 CONFIG [+]                          ┃
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                        ''')
            print(f'''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃    Api Id                       ┃  {Api_Id}                      ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Api Password                 ┃  {Api_Password}                             ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Sender ID                    ┃  {Sender_id}                              ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    API Balance                  ┃ {final_bal}  EUR                            ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    SMS ABLE TO SENT [ USA ]     ┃ {sms_able_to_sent}                                   ┃
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
            cod = "+"
            list = input("          Your Number List:~# ")
            number = sum(1 for line in open(list))
            openit = open(list, 'r')
            for i in range(0, number):
                recipent = cod + str(openit.readline())
                url = 'http://api2.send99.com/api/SendSMS?api_id='+Api_Id+'&api_password='+Api_Password+'&sms_type=P&encoding=T&sender_id=INFO&phonenumber='+recipent+'&textmessage='+MSG
                rq = requests.get(url)
                job = rq.text
                search = re.search('"status":"S"', job)
                if search:
                    print(Fore.GREEN + '''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃   Statues                             ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}                ┃Sent                                   ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                else:
                    print('''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃    Message ID                         ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}           ┃Failed ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                    print(rq.text)
        elif Choice == '4':
            print(' Not Subscribed !+!+!+!')
        elif Choice == '5':
            print('''
            {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
            {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
            {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
            {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
            {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
            {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
            {2} ┃                          {0}▀           ▐                            {2}┃
            {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {2} ┃         {0}SMSALA Bulk SENDER        {2}┃         {0}CODED BY xMarvel      {2}┃
            {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

            '''.format(fg[0], fg[1], fg[5], fg[4]))

            read_config = configparser.ConfigParser()
            read_config.read("Senders-configs/SMSALA.ini")

            Api_Id = read_config.get("Section1", "Api_Id")
            Api_Password = read_config.get("Section1", "Api_Password")
            Sender_id = read_config.get("Section1", "Sender_Id")
            MSG = read_config.get("Section1", "Message")
            Bal_endpoint = f'http://api.smsala.com/api/CheckBalance?api_id={Api_Id}&api_password={Api_Password}'
            bal_req = requests.get(Bal_endpoint).json()
            final_bal = bal_req['BalanceAmount']
            sms_able_to_sent = round(final_bal / 0.0074)
            print('''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃                          [+] SMSALA CONFIG [+]                          ┃
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                        ''')
            print(f'''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃    Api Id                       ┃  {Api_Id}                      ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Api Password                 ┃  {Api_Password}                             ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Sender ID                    ┃  {Sender_id}                              ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    API Balance                  ┃ {final_bal}  EUR                            
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    SMS ABLE TO SENT [ USA ]     ┃ {sms_able_to_sent}                                   
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
            cod = "+"
            list = input("          Your Number List:~# ")
            number = sum(1 for line in open(list))
            openit = open(list, 'r')
            for i in range(0, number):
                recipent = cod + str(openit.readline())
                url = 'http://api.smsala.com/api/SendSMS?api_id='+Api_Id+'&api_password='+Api_Password+'&sms_type=P&encoding=T&sender_id=TSTALA&phonenumber='+recipent+'&textmessage='+MSG
            
                rq = requests.get(url)
                job = rq.text
                search = re.search('"status":"S"', job)
                if search:
                    print(Fore.GREEN + '''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃   Statues                             ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}                           ┃Sent                                   ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                    recipent))
                else:
                    print('''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃    Message ID                         ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}           ┃Failed ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                    recipent))
                    print(rq.text)
        elif Choice == '19':
            bl = Fore.BLACK
            wh = Fore.WHITE
            yl = Fore.YELLOW
            red = Fore.RED
            res = Style.RESET_ALL
            gr = Fore.GREEN
            ble = Fore.BLUE

            def screen_clear():
                _ = os.system('cls')
            def logo():
                screen_clear()
                clear = "\x1b[0m"
                colors = [36, 32, 34, 35, 31, 37]
                x = """ 

                                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                    ┃                ▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               ┃
                                    ┃            ▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               ┃
                                    ┃              █ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               ┃   
                                    ┃             ▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            ┃
                                    ┃            █   ▀▄    █     █   █    █  █  ▀███▀       ▀           ┃
                                    ┃             ▀       ▀     █   ▀      █▐                           ┃
                                    ┃                          ▀           ▐                            ┃
                                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
                                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            		              ┃	                    [+] Twilio MASS CHECKER ...	                  ┃
                        	      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                                                                                             
                                       """
                for N, line in enumerate(x.split("\n")):
                    sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
            logo()
            link = input(f'root@xMarvel:/{currnet_dir}/# Enter List -- >  ')
            with open(link) as fp:
                for star in fp:
                    check = star.rstrip()
                    ch = check.split('\n')[0].split('|')
                    account_sid = ch[0]
                    auth_token = ch[1]
                    auth = (account_sid, auth_token)
                    try:
                        curler_balance = requests.get(
                            "https://api.twilio.com/2010-04-01/Accounts/" + account_sid + "/Balance.json",
                            auth=auth).text
                        curler_msg = requests.get(
                            "https://api.twilio.com/2010-04-01/Accounts/" + account_sid + "/Messages.json",
                            auth=auth).text
                        info_balance = json.loads(curler_balance)
                        info_msg = json.loads(curler_msg)
                        for msg in info_msg["messages"]:
                            if msg["direction"] == "outbound-api":
                                nope = msg["from"]
                                break
                            elif msg["direction"] == "inbound-api":
                                nope = msg["to"]
                                break
                        print(f"# {account_sid}'|'{auth_token} Work => .")
                        build = "Account_SID: " + account_sid + '|' + "Token: " + auth_token + '\n' + "Currency: " + \
                                info_balance["currency"] + '\n' + "Balance :" + info_balance[
                                    "balance"] + '\n' + "Phone number: " + nope + '\n'
                        usd_balss = info_balance["balance"]
                        remover = build.replace('\r', '')
                        save = open('Crackers/twilio/Work.txt', 'a')
                        save.write(remover + '\n')
                        save.close()
                    except:
                        print(f"FAILED: Invalid credentials.")
                        build = "Account_SID: " + account_sid + '|' + "Token: " + auth_token + '\n'
                        remover = build.replace('\r', '')
                        save = open('Crackers/twilio/Bad.txt', 'a')
                        save.write(remover + '\n')
                        save.close()
                        pass
        elif Choice == '21':
            os.system('cls')
            def logo():

                now = strftime("%Y-%m-%d %H:%M:%S")
                clear = "\x1b[0m"
                colors = [36, 32, 34, 35, 31, 37]
                x = """ 

                                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                    ┃                ▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               ┃
                                    ┃            ▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               ┃
                                    ┃              █ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               ┃   
                                    ┃             ▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            ┃
                                    ┃            █   ▀▄    █     █   █    █  █  ▀███▀       ▀           ┃
                                    ┃             ▀       ▀     █   ▀      █▐                           ┃
                                    ┃                          ▀           ▐                            ┃
                                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
                                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            		              ┃	                    [+] NEXMO MASS CHECKER ...	                  ┃
                        	      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                                                                                             
                                       """
                for N, line in enumerate(x.split("\n")):
                    sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
            logo()
            bl = Fore.BLACK
            wh = Fore.WHITE
            yl = Fore.YELLOW
            red = Fore.RED
            res = Style.RESET_ALL
            gr = Fore.GREEN
            ble = Fore.BLUE

            link = input(f'root@xMarvel:/{currnet_dir}/# Enter List -- >  ')
            with open(link) as fp:
                for star in fp:
                    try:
                        check = star.rstrip()
                        ch = check.split('\n')[0].split('|')
                        Key = ch[0]
                        Sec = ch[1]
                        client = vonage.Client(key=Key, secret=Sec)
                        result = client.get_balance()
                        usd_bals = (f"{result['value']:0.2f}")
                        print(f" {Key}|{Sec}  Working API! Balance : {result['value']:0.2f} EUR{res}")
                        open("Crackers/Nexmo/Live.txt", "a").write(f"{Key}|{Sec} Balance: {result['value']:0.2f} EUR\n")


                    except:
                        print(f" {Key}|{Sec}  {red}DEAD API!{res}\n")
                        pass
        elif Choice == '25':
            os.system('cls')
            print('''
                                {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
                                {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
                                {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
                                {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
                                {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
                                {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
                                {2} ┃                          {0}▀           ▐                            {2}┃
                                {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                                {2} ┃         {0}Number Checker v1.0       {2}┃         {0}CODED BY xMarvel      {2}┃
                                {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

                                '''.format(fg[0], fg[1], fg[5], fg[4]))
            print('=' * 30)
            print(Fore.RED + 'Setting Up Numverify...')
            print('=' * 30)
            API = input('[+] Your API Key Here: ')
            print('=' * 30)
            list = input('[+] Your Phone Numbers List: ')
            base_url = 'http://apilayer.net/api/validate'
            params = {
                'access_key': API,
                'number': '',
            }
            phone = open(list, 'r')
            for i in phone:
                i = i.strip()
                if i:
                    line = i.split(':')
                    params['number'] = line[0]
                    response = requests.get(base_url, params=params)

                try:

                    resp = response.json()
                    final = resp['carrier']
                    valid = re.search('"valid":true', response.text)
                    carrier = 'Checker/Number-check'
                    if not os.path.isdir(carrier):
                        os.makedirs(carrier)
                    mok = open(os.path.join(carrier, resp['carrier'] + '.txt'), 'a+')
                    if (carrier + '\\' + resp['carrier'] + '.txt') == mok.name and valid:
                        print(Fore.GREEN + f'''
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃    Number                       ┃    Carrier                            ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃    {i}                 ┃{final}                                
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
                        mok.write(i + '\n')
                    else:
                        dead = open('Checker/Number-check/Invalid.txt', 'a')
                        dead.write(i + '\n')
                except OSError:
                    print('skipping')

                except FileNotFoundError:
                    if resp['carrier'] == '':
                        print('skipping')


                except KeyError:
                    print(Fore.RED + 'Api Limit Exceeded Consider Changing Api Key')
                    break;
        elif Choice == '24':
            class Numbercheck():
                live = '"valid":true,'.encode()
                die = '"valid":false,'.encode()
                inputQueue = queue.Queue()

                def __init__(self):
                    def slowprint(s):
                        for c in s + '\n':
                            sys.stdout.write(c)
                            sys.stdout.flush()
                            time.sleep(1. / 10)
                            # backdoors removed by @f4c3r100
                    def logo():
                        from random import choice
                        os.system('cls')
                        print('''
                        {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                        {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
                        {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
                        {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
                        {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
                        {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
                        {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
                        {2} ┃                          {0}▀           ▐                            {2}┃
                        {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                        {2} ┃         {0}Number Checker v1.0       {2}┃         {0}Very Fast             {2}┃
                        {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

                        '''.format(fg[0], fg[1], fg[5], fg[4]))

                    logo()
                    bl = Fore.BLACK
                    wh = Fore.WHITE
                    yl = Fore.YELLOW
                    red = Fore.RED
                    gr = Fore.GREEN
                    ble = Fore.BLUE
                    res = Style.RESET_ALL
                    self.mailist = input(f'{gr}  Give Me Your List{wh}/{red}@xMarvel> {gr}${res} ')
                    self.token = input(f'{gr}  Give Me Your Token {wh}/{red}@xMarvel > {gr} ${res}  ')
                    self.thread = '8'
                    self.clean = 'n'
                    if self.clean == 'y':
                        self.clean_rezult()
                    print('')

                def save_to_file(self, nameFile, x):
                    kl = open(nameFile, 'a+')
                    kl.write(x)
                    kl.close()

                def clean_rezult(self):
                    open('live.txt', 'w').close()
                    open('die.txt', 'w').close()
                    open('unknown.txt', 'w').close()

                def post_email(self, eml):
                    try:
                        r = requests.get(
                            'https://apilayer.net/api/validate?access_key=' + self.token + '&number=' + eml)
                        if self.live in r.content:
                            return 'live'
                        else:
                            return 'die'
                    except:
                        return 'unknown'

                def chk(self):
                    while 1:
                        eml = self.inputQueue.get()
                        rez = self.post_email(eml)
                        if rez == 'die':
                            red = Fore.RED
                            resetall = Style.RESET_ALL
                            print(f'''
                                        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                        ┃      {eml}                 ┃         {red}DIE{resetall}                   ┃
                                        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
                            self.save_to_file('Checker\Fast-Num-Check\die.txt', eml + '\n')
                        elif rez == 'live':
                            Green = Fore.GREEN
                            resetall = Style.RESET_ALL
                            print(f'''
                                        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                        ┃      {eml}                 ┃         {Green}Live{resetall}                  ┃
                                        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
                            self.save_to_file('Checker\Fast-Num-Check\live.txt', eml + '\n')
                        elif rez == 'unknown':
                            print(
                                Fore.CYAN + '[Number Checker v1.0 ]' + Fore.WHITE + ' | ' +Fore.YELLOW + f" | {eml} | UNKOWN !!! ")
                        else:
                            print('contact @xMarval_support')
                        self.inputQueue.task_done()

                def run_thread(self):
                    for x in range(int(self.thread)):
                        t = threading.Thread(target=self.chk)
                        t.setDaemon(True)
                        t.start()
                    for y in open(self.mailist, 'r').readlines():
                        self.inputQueue.put(y.strip())
                    self.inputQueue.join()
            heh = Numbercheck()
            heh.run_thread()
        elif Choice == '26':
            os.system('cls')
            clear = "\x1b[0m"
            colors = [36, 32, 34, 35, 31, 37]
            x = """ 
 
                ██╗  ██╗███╗   ███╗ █████╗ ██████╗ ██╗   ██╗███████╗██╗ 
                ╚██╗██╔╝████╗ ████║██╔══██╗██╔══██╗██║   ██║██╔════╝██║ 
                 ╚███╔╝ ██╔████╔██║███████║██████╔╝██║   ██║█████╗  ██║ 
                 ██╔██╗ ██║╚██╔╝██║██╔══██║██╔══██╗╚██╗ ██╔╝██╔══╝  ██║ 
                ██╔╝ ██╗██║ ╚═╝ ██║██║  ██║██║  ██║ ╚████╔╝ ███████╗███████╗
                    ╚═╝  ╚═╝╚═╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚══════╝ 
                                 CODED BY XEON :")
                        
                       Bulk Phone Number Generator V1.0   |  Coded by xMarvel ( xeon )                          
                                         Greetinz to : Mad-Hacker    
                      
                                [+] My Telegram: @xe0on      [+]
                                [+]Author: XEON              [+]
                                [+]Support: @xMarvel_support [+]
                                [+]Channel: @xMarvel_OfficIal[+]
                                          
                              +-------- With Great Power Comes Great Toolz! --------+

			                  """
            for N, line in enumerate( x.split( "\n" ) ):
                sys.stdout.write( " \x1b[1;%dm%s%s\n " % (random.choice( colors ), line, clear) )
            print('-'*33)
            cc = input(str('Enter the Country Code { EX +1 For USA } : '))
            print('-'*33)
            sc = input(str('Enter the Area Code { EX 910 } : '))
            print('-'*33)
            n = int(input("Enter Amount of numbers: "))
            print('-'*33)
            lent = int(input('Length Remaining Digits [ 7 FOR USA ] : '))
            print('-'*33)
            mow = str('9'*lent)
            print('-'*33)
            def random_phone_num_generator():
                first = str(random.randint(0,int(mow))).zfill(lent)
                return (first)
            save = open('Phone.txt','a+')
            for i in range(0,n):
                rez = cc+sc+random_phone_num_generator()
                save.write(rez + '\n')
            print('Phone Numbers Saved In Phone.txt')
            input('Enter any Key')
        elif Choice == '99':
            rs = requests.get('https://pastebin.com/raw/YKKc4Yky').text
            forgr = Fore.GREEN
            reseee = Style.RESET_ALL
            print(f'''
                         ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                         ┃{forgr}                       [+] {rs} [+]                           {reseee}┃
                         ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                                    ''')
        elif Choice == '23':
            class AMZCHK():
                live = '"status":"live"'.encode()
                die = '"status":"invalid"'.encode()
                inputQueue = queue.Queue()

                def __init__(self):
                    def slowprint(s):
                        for c in s + '\n':
                            sys.stdout.write(c)
                            sys.stdout.flush()
                            time.sleep(1. / 10)

                    def logo():
                        from random import choice
                        os.system('cls')
                        print('''
                        {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                        {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
                        {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
                        {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
                        {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
                        {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
                        {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
                        {2} ┃                          {0}▀           ▐                            {2}┃
                        {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                        {2} ┃         {0}Amazon Checker v1.0       {2}┃         {0}Very Fast             {2}┃
                        {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

                        '''.format(fg[0], fg[1], fg[5], fg[4]))

                    logo()
                    bl = Fore.BLACK
                    wh = Fore.WHITE
                    yl = Fore.YELLOW
                    red = Fore.RED
                    gr = Fore.GREEN
                    ble = Fore.BLUE
                    res = Style.RESET_ALL
                    self.mailist = input(f'{gr}  Give Me Your List{wh}/{red}@xMarvel> {gr}${res} ')
                    self.thread = '15'
                    self.clean = 'n'
                    if self.clean == 'y':
                        self.clean_rezult()
                    print('')

                def save_to_file(self, nameFile, x):
                    kl = open(nameFile, 'a+')
                    kl.write(x)
                    kl.close()

                def clean_rezult(self):
                    open('live.txt', 'w').close()
                    open('die.txt', 'w').close()
                    open('unknown.txt', 'w').close()

                def post_email(self, eml):
                    print('This feature is currently not working.')
                    return False
                    #try:
                    #    r = requests.get(
                    #        'https://x-hell.shop/g3.php?phnum=' + eml)
                    #    if self.live in r.content:
                    #        return 'live'
                    #    else:
                    #        return 'die'
                    #except:
                    #    return 'unknown'

                def chk(self):
                    while 1:
                        eml = self.inputQueue.get()
                        rez = self.post_email(eml)
                        if rez == 'die':
                            red = Fore.RED
                            resetall = Style.RESET_ALL
                            print(f'''
                                        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                        ┃      {eml}                 ┃         {red}DIE{resetall}                   ┃
                                        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
                            self.save_to_file('Checker/Amz-check/Die.txt', eml + '\n')
                        elif rez == 'live':
                            Green = Fore.GREEN
                            resetall = Style.RESET_ALL
                            print(f'''
                                        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                        ┃      {eml}                 ┃         {Green}Live{resetall}                  ┃
                                        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
                            self.save_to_file('Checker/Amz-check/live.txt', eml + '\n')
                        elif rez == 'unknown':
                            print(
                                Fore.CYAN + '[AMZ-NUM v1.0 ]' + Fore.WHITE + ' | ' +Fore.YELLOW + f" | {eml} | UNKOWN !!! ")
                            self.save_to_file('Checker/Amz-check/Die.txt', eml + '\n')
                        else:
                            print('contact @xMarval_support')
                        self.inputQueue.task_done()

                def run_thread(self):
                    for x in range(int(self.thread)):
                        t = threading.Thread(target=self.chk)
                        t.setDaemon(True)
                        t.start()
                    for y in open(self.mailist, 'r').readlines():
                        self.inputQueue.put(y.strip())
                    self.inputQueue.join()
            heh = AMZCHK()
            heh.run_thread()
        elif Choice == '6':
            os.system('cls')
            print('''
                        {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                        {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
                        {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
                        {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
                        {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
                        {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
                        {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
                        {2} ┃                          {0}▀           ▐                            {2}┃
                        {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                        {2} ┃         {0}BULKSMS.TOP v1.0          {2}┃         {0}BULK                  {2}┃
                        {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

                        '''.format(fg[0], fg[1], fg[5], fg[4]))
            def main_sender():
                read_config = configparser.ConfigParser()
                read_config.read("Senders-configs/BULKSMS-config.ini")
                username = read_config.get("Section1", "username")
                password = read_config.get("Section1", "password")
                type = read_config.get("Section1", "msgtype")
                source = read_config.get("Section1", "senderid")
                message = read_config.get("Section1", "message")
                cod = "+"
                list = input("          Your Number List:~# ")
                number = sum(1 for line in open(list))
                openit = open(list, 'r')
                for i in range(0, number):
                    recipent = cod + str(openit.readline())
                    api_url = f'https://bulksms.top/sendsms?username={username}&password={password}&type={type}&source={source}&destinations={recipent}&message={message}'
                    send_sms = requests.get(api_url).text
                    if '"status":"success",' in send_sms:
                        print(Fore.GREEN + '''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃   Statues                             ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}                 ┃Sent                                   ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                    else:
                        print('''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃    Message ID                         ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}           ┃Failed ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                        print(rq.text)
            main_sender()
        elif Choice == '7':
            os.system('cls')
            print('''
                        {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                        {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
                        {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
                        {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
                        {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
                        {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
                        {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
                        {2} ┃                          {0}▀           ▐                            {2}┃
                        {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                        {2} ┃        {0}BulkGate     v1.0          {2}┃         {0}BULK                  {2}┃
                        {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

                        '''.format(fg[0], fg[1], fg[5], fg[4]))
            def main_sender():
                read_config = configparser.ConfigParser()
                read_config.read("Senders-configs/BulkGate-config.ini")
                application_id  = read_config.get("Section1", "application_id")
                application_token  = read_config.get("Section1", "application_token")
                senderr_id  = read_config.get("Section1", "sendername")
                message = read_config.get("Section1", "message")
                balanceurl = f'https://portal.bulkgate.com/api/1.0/simple/info?application_id={application_id}&application_token={application_token}'
                try:
                    getbaln = requests.get(balanceurl).json()
                    balanceurldataload = getbaln['data']
                    usdbalance = balanceurldataload['credit']
                    print(Fore.GREEN + '''
                                 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                 ┃                         [+] BULKGATE CONFIG [+]                         ┃
                                 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                    ''')
                    print(f'''
                                 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                 ┃    Application Id               ┃{application_id}     
                                 ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                                 ┃    Secret Key                   ┃{application_token}       
                                 ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                                 ┃    Number Or Sender ID          ┃{senderr_id}                           
                                 ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                                 ┃    API Balance                  ┃{usdbalance}                                 
                                 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
                except:
                    print(' wrong api ')
                cod = "+"
                list = input("          Your Number List:~# ")
                number = sum(1 for line in open(list))
                openit = open(list, 'r')
                for i in range(0, number):
                    recipent = cod + str(openit.readline())
                    sende_url = 'https://portal.bulkgate.com//api/1.0/simple/transactional'
                    data = {
                        "application_id": application_id, 
                        "application_token": application_token, 
                        "number": recipent, 
                        "text": message,
                    }
                    sendit = requests.post(sende_url, data=data).text
                    if """accepted""" in sendit:
                        print('sent')
                    else:
                        print(sendit)
            main_sender()
        elif Choice == '8':
            class PlivoSend:
                def __init__(self):
                    self.banner()
                    self.setup()
                    self.initialize()
                    self.startup()
                def setup(self):
                    if not os.path.isfile('Senders-configs/Plivo-config.json'):
                        self.config = {
                        'threads': 10,
                        'auth_id': 'plivo_auth_id',
                        'auth_token': 'plivo_token',
                        'sender_num': 'plivo_registered_num'
                        }
                        with open('Senders-configs/Plivo-config.json', 'w+') as json_file:
                            json.dump(self.config, json_file, indent=2)
                        print(f'             {fg[0]}[!] - Edit The {fg[6]}config{fg[0]} File And Try Again - [!]')
                        sys.exit()
                    else:
                        with open('Senders-configs/Plivo-config.json') as json_file:
                            self.config = json.load(json_file)

                def banner(self):
                    fg = [
    '\033[91;1m', #RED     0
    '\033[92;1m', #GREEN   1
    '\033[93;1m', #YELLOW  2
    '\033[94;1m', #BLUE    3
    '\033[95;1m', #MAGENTA 4
    '\033[96;1m', #CYAN    5
    '\033[97;1m'  #WHITE   6
                            ]
                    print('''
{2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{2} ┃  {0}          ██   ██ ███    ███  █████  ██████  ██    ██ ███████ ██       {2}┃    
{2} ┃  {0}           ██ ██  ████  ████ ██   ██ ██   ██ ██    ██ ██      ██       {2}┃     
{2} ┃  {0}            ███   ██ ████ ██ ███████ ██████  ██    ██ █████   ██       {2}┃     
{2} ┃  {0}           ██ ██  ██  ██  ██ ██   ██ ██   ██  ██  ██  ██      ██       {2}┃   
{2} ┃  {0}          ██   ██ ██      ██ ██   ██ ██   ██   ████   ███████ ███████  {2}┃
{2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫                                                            
{2} ┃         {0}PLIVIO SMS SENDER         {2}┃         {0}RENEWED TOOL                {2}┃
{2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ '''.format(fg[0], fg[1], fg[5], fg[4]))                                         


                def startup(self):
                    self.numlist = open(input("\t{0} Your Number List:~# {1}".format(fg[0], fg[1])), 'r').read().splitlines()
                    self.messege = open(input("\t{0} Your Messege File:~# {1}".format(fg[0], fg[1])), 'r').read()
                    self.max = len(self.numlist)
                    self.current = 1
                    if self.config['threads'] > 10:
                        self.config['threads'] = 10
                    self.banner()
                    with ThreadPoolExecutor(max_workers=self.config['threads']) as executor:
                        executor.map(self.sender, self.numlist)

                def log(self, status, number):
                    date = datetime.now().strftime("%B%d")
                    now = datetime.now().strftime("%H:%M:%S")
                    current = (self.current if len(str(self.max)) == len(str(self.current)) else f'{"0"*(len(str(self.max))-len(str(self.current)))}{self.current}')
                    if status == 'error':
                        print('\t{0}[{1}{4}{0}] [{2}{5}/{6}{0}] {0}[{3}FAIL{0}] - {3}{7}'.format(fg[5], fg[6], fg[2], fg[0], now, current, self.max, number))
                    elif status == 'sent':
                        print('\t{0}[{1}{4}{0}] [{2}{5}/{6}{0}] {0}[{3}SENT{0}] - {3}{7}'.format(fg[5], fg[6], fg[2], fg[1], now, current, self.max, number))
                    elif status == "wait":
                        print('\t{0}[{1}{4}{0}] [{2}{5}/{6}{0}] {0}[{3}OHHOLD{0}] - {3}{7}'.format(fg[5], fg[6], fg[2], fg[1], now, current, self.max, number))
                    self.current += 1
                def initialize(self):
                    if self.config['auth_id'] == 'plivo_auth_id' or self.config['auth_token'] == 'plivo_token' or self.config['sender_num'] == 'plivo_registered_num':
                        print(f'             {fg[0]}[!] - Edit The {fg[6]}config{fg[0]} File And Try Again - [!]')
                        sys.exit()
                    else:
                        self.auth_id = self.config['auth_id']
                        self.auth_token = self.config['auth_token']
                        self.sender_num = self.config['sender_num']
                def sender(self, num):
                    self.headers = {'Content-Type': 'application/json'}
                    self.url = "https://api.plivo.com/v1/Account/"+self.auth_id+"/Message/"
                    self.data = '{"src": "'+self.sender_num+'","dst": "'+num+'", "text": "'+self.messege+'"}'
                    self.send = requests.post(self.url, data=self.data, headers=self.headers, auth=(self.auth_id, self.auth_token))
                    if "verify" in str(self.send.text) or "login" in str(self.send.text) or "credentials" in str(self.send.text):
                        print(f'               {fg[0]}[!] - Invalid Auth Token Or Auth ID - [!]')
                        sys.exit()
                    else:
                        self.send_json = self.send.json()
                        self.uuid = self.send_json['message_uuid']
                        self.msg_u = self.uuid[0]
                        self.surl = self.url+self.msg_u
                        self.status = requests.get(self.surl, headers=self.headers, auth=(self.auth_id, self.auth_token))
                        self.final = self.status.json()
                        self.state = self.final["message_state"]
                        if self.state == "sent" or self.state == "delivered":
                            self.log("sent", num)
                        elif self.state == "undelivered" or self.state == "queued":
                            self.log("wait", num)
                        else:
                            self.log("fail", num)

            if __name__ == "__main__":
                PlivoSend()
        elif Choice == '9':
            os.system('cls')
            print('''
                        {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                        {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
                        {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
                        {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
                        {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
                        {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
                        {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
                        {2} ┃                          {0}▀           ▐                            {2}┃
                        {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                        {2} ┃        {0}MSGBIRD     v1.0           {2}┃         {0}BULK                  {2}┃
                        {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

                        '''.format(fg[0], fg[1], fg[5], fg[4]))
            def main_sender():
                read_config = configparser.ConfigParser()
                read_config.read("Senders-configs/MsgBird-config.ini")
                AccessKey  = read_config.get("Section1", "AccessKey")
                sender_id  = read_config.get("Section1", "Sender_id")
                message = read_config.get("Section1", "message")
                try:
                    apiend = f'https://rest.messagebird.com/balance?access_key={AccessKey}'
                    lkf = requests.get(apiend).json()
                    final_balance = lkf['amount']
                    print(Fore.GREEN + '''
                                 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                 ┃                       [+] MESSAGE BIRD CONFIG [+]                       ┃
                                 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                    ''')
                    print(f'''
                            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                            ┃    Access Key                   ┃ {AccessKey}     
                            ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                            ┃    Number Or Sender ID          ┃ {sender_id}                           
                            ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                            ┃    API Balance                  ┃ {final_balance} USD                                 
                            ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')                  
                except:
                    print(' WRONG API !!')
                    sys.exit()
            main_sender()
        elif Choice == '10':
            print( ' coming soon ..')
        elif Choice == '20':
            os.system('cls')
            def logo():

                now = strftime("%Y-%m-%d %H:%M:%S")
                clear = "\x1b[0m"
                colors = [36, 32, 34, 35, 31, 37]
                x = """ 

                                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                    ┃                ▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               ┃
                                    ┃            ▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               ┃
                                    ┃              █ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               ┃   
                                    ┃             ▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            ┃
                                    ┃            █   ▀▄    █     █   █    █  █  ▀███▀       ▀           ┃
                                    ┃             ▀       ▀     █   ▀      █▐                           ┃
                                    ┃                          ▀           ▐                            ┃
                                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
                                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            		              ┃	                    [+] SEND99 MASS CHECKER ...	                  ┃
                        	      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                                                                                             
                                       """
                for N, line in enumerate(x.split("\n")):
                    sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
            logo()
            bl = Fore.BLACK
            wh = Fore.WHITE
            yl = Fore.YELLOW
            red = Fore.RED
            res = Style.RESET_ALL
            gr = Fore.GREEN
            ble = Fore.BLUE

            link = input(f'root@xMarvel:/{currnet_dir}/# Enter List -- >  ')
            with open(link) as fp:
                for star in fp:
                    try:
                        check = star.rstrip()
                        ch = check.split('\n')[0].split('|')
                        Key = ch[0]
                        Sec = ch[1]
                        Bal_endpoint = f'http://api2.send99.com/api/CheckBalance?api_id={Key}&api_password={Sec}'
                        bal_req = requests.get(Bal_endpoint).json()
                        final_bal = bal_req['BalanceAmount']
                        print(f" {Key}|{Sec}  Working API! Balance : {final_bal} EUR{res}")
                        open("Cracker/Send99/Live.txt", "a").write(f"{Key}|{Sec} Balance: {final_bal} EUR\n")
                    except:
                        pass
        elif Choice == '22':
            os.system('cls')
            def logo():

                now = strftime("%Y-%m-%d %H:%M:%S")
                clear = "\x1b[0m"
                colors = [36, 32, 34, 35, 31, 37]
                x = """ 

                                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                    ┃                ▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               ┃
                                    ┃            ▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               ┃
                                    ┃              █ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               ┃   
                                    ┃             ▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            ┃
                                    ┃            █   ▀▄    █     █   █    █  █  ▀███▀       ▀           ┃
                                    ┃             ▀       ▀     █   ▀      █▐                           ┃
                                    ┃                          ▀           ▐                            ┃
                                    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛   
                                    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            		              ┃	                    [+] SMSALA MASS CHECKER ...	                  ┃
                        	      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛                                                                                             
                                       """
                for N, line in enumerate(x.split("\n")):
                    sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
            logo()
            bl = Fore.BLACK
            wh = Fore.WHITE
            yl = Fore.YELLOW
            red = Fore.RED
            res = Style.RESET_ALL
            gr = Fore.GREEN
            ble = Fore.BLUE

            link = input(f'root@xMarvel:/{currnet_dir}/# Enter List -- >  ')
            with open(link) as fp:
                for star in fp:
                    try:
                        check = star.rstrip()
                        ch = check.split('\n')[0].split('|')
                        Key = ch[0]
                        Sec = ch[1]
                        Bal_endpoint = f'http://api.smsala.com/api/CheckBalance?api_id={Key}&api_password={Sec}'
                        bal_req = requests.get(Bal_endpoint).json()
                        final_bal = bal_req['BalanceAmount']
                        print(f" {Key}|{Sec}  Working API! Balance : {final_bal} EUR{res}")
                        open("Cracker/smsala/Live.txt", "a").write(f"{Key}|{Sec} Balance: {final_bal} EUR\n")
                    except:
                        pass
        elif Choice == '27':
            class AMZCHK():
                live = '"status":"live"'.encode()
                die = '"status":"invalid"'.encode()
                inputQueue = queue.Queue()

                def __init__(self):
                    def slowprint(s):
                        for c in s + '\n':
                            sys.stdout.write(c)
                            sys.stdout.flush()
                            time.sleep(1. / 10)

                    def logo():
                        from random import choice
                        os.system('cls')
                        print('''
                        {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                        {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
                        {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
                        {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
                        {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
                        {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
                        {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
                        {2} ┃                          {0}▀           ▐                            {2}┃
                        {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                        {2} ┃         {0}PayPal Checker v1.0       {2}┃         {0}Very Fast             {2}┃
                        {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

                        '''.format(fg[0], fg[1], fg[5], fg[4]))

                    logo()
                    bl = Fore.BLACK
                    wh = Fore.WHITE
                    yl = Fore.YELLOW
                    red = Fore.RED
                    gr = Fore.GREEN
                    ble = Fore.BLUE
                    res = Style.RESET_ALL
                    self.mailist = input(f'{gr}  Give Me Your List{wh}/{red}@xMarvel> {gr}${res} ')
                    self.thread = '15'
                    self.clean = 'n'
                    if self.clean == 'y':
                        self.clean_rezult()
                    print('')

                def save_to_file(self, nameFile, x):
                    kl = open(nameFile, 'a+')
                    kl.write(x)
                    kl.close()

                def clean_rezult(self):
                    open('live.txt', 'w').close()
                    open('die.txt', 'w').close()
                    open('unknown.txt', 'w').close()

                def post_email(self, eml):
                    #try:
                    #    r = requests.get(
                    #        'https://x-hell.shop/g3.php?phnum=' + eml)
                    #    if self.live in r.content:
                    #        return 'live'
                    #    else:
                    #        return 'die'
                    #except:
                    #    return 'unknown'
                    return False
                def chk(self):
                    while 1:
                        eml = self.inputQueue.get()
                        rez = self.post_email(eml)
                        if rez == 'die':
                            red = Fore.RED
                            resetall = Style.RESET_ALL
                            print(f'''
                                        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                        ┃      {eml}                 ┃         {red}DIE{resetall}                   ┃
                                        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
                            self.save_to_file('Checker/PayPal-check/die.txt', eml + '\n')
                        elif rez == 'live':
                            Green = Fore.GREEN
                            resetall = Style.RESET_ALL
                            print(f'''
                                        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                        ┃      {eml}                 ┃         {Green}Live{resetall}                  ┃
                                        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
                            self.save_to_file('Checker/PayPal-check/live.txt', eml + '\n')
                        elif rez == 'unknown':
                            print(
                                Fore.CYAN + '[PPL-NUM v1.0 ]' + Fore.WHITE + ' | ' +Fore.YELLOW + f" | {eml} | UNKOWN !!! ")
                            self.save_to_file('Checker/PayPal-check/die.txt', eml + '\n')
                        else:
                            print('contact @xMarval_support')
                        self.inputQueue.task_done()

                def run_thread(self):
                    for x in range(int(self.thread)):
                        t = threading.Thread(target=self.chk)
                        t.setDaemon(True)
                        t.start()
                    for y in open(self.mailist, 'r').readlines():
                        self.inputQueue.put(y.strip())
                    self.inputQueue.join()
            heh = AMZCHK()
            heh.run_thread()
        elif Choice == '11':
            print('soon')
        elif Choice == '12':

            print('''
            {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
            {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
            {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
            {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
            {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
            {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
            {2} ┃                          {0}▀           ▐                            {2}┃
            {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {2} ┃         {0}Karix Bulk SENDER         {2}┃         {0}CODED BY xMarvel      {2}┃
            {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

            '''.format(fg[0], fg[1], fg[5], fg[4]))

            read_config = configparser.ConfigParser()
            read_config.read("Senders-configs/Karix_Config.ini")

            acc_id = read_config.get("Section1", "acc_id")
            acc_tok = read_config.get("Section1", "acc_tok")
            sender_id = read_config.get("Section1", "sender_id")
            MSG = read_config.get("Section1", "Message")
            print('''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃                          [+] Karix CONFIG [+]                           ┃
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                        ''')
            print(f'''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃    Account id                       ┃  {acc_id}   ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Account Token                    ┃  {acc_tok}   ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Sender ID                        ┃  {sender_id}                                ┃                               
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
            reseee = Style.RESET_ALL
            list = input(f"          \033[0;37;45mYour Number List:~#{reseee} ")
            numberass = sum(1 for line in open(list))
            openit = open(list, 'r')
            for i in range(0, numberass):
                recipent =  str(openit.readline())
                ses = requests.session()
                inf = (str(acc_id),str(acc_tok))
                intel = {
                "channel": "sms",
                "source": str(sender_id),
                "destination": [str(recipent)],
                "content": {
                "text": str(MSG)
                    }
                }
                message = ses.post('https://api.karix.io/message/',json=intel , auth = inf)
                try:
                    search = re.search('"status":"queued"', message.text)
                    search1 = re.search('"status":"sent"', message.text)
                    search2 = re.search('"status":"delivered"', message.text)
                    bal = message.json()
                    balance = str(bal['meta']['available_credits'])
                    if  search1 or search or search2 :
                       print(Fore.GREEN + '''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃   Statues                             ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}                ┃Sent                                   ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                    else:
                        print('''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃    Message ID                         ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}           ┃Failed ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                except Exception as e:
                    pass
        elif Choice == '13':

            print('''
            {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
            {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
            {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
            {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
            {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
            {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
            {2} ┃                          {0}▀           ▐                            {2}┃
            {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {2} ┃         {0}telesign Bulk SENDER      {2}┃         {0}CODED BY xMarvel      {2}┃
            {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

            '''.format(fg[0], fg[1], fg[5], fg[4]))

            read_config = configparser.ConfigParser()
            read_config.read("Senders-configs/telesign_Config.ini")

            acc_id = read_config.get("Section1", "customer_id")
            acc_tok = read_config.get("Section1", "api_key")
            sender_id = read_config.get("Section1", "sender_id")
            MSG = read_config.get("Section1", "Message")
            print('''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃                          [+] telesign CONFIG [+]                        ┃
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                        ''')
            print(f'''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃    Account id                       ┃  {acc_id}   ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Account Token                    ┃  {acc_tok}   ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Sender ID                        ┃  {sender_id}                                ┃                               
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
            reseee = Style.RESET_ALL
            list = input(f"          \033[0;37;45mYour Number List:~#{reseee} ")
            numberass = sum(1 for line in open(list))
            openit = open(list, 'r')
            for i in range(0, numberass):
                recipent =  str(openit.readline())
                ses = requests.session()
                inf = (str(acc_id),str(acc_tok))
                intel = {
                    "message": str(MSG),
                    "from": str(sender_id),
                    "message_type": 'ARN',
                    "phone_number": str(recipent),
                        }
                message = ses.post('https://rest-api.telesign.com/v1/messaging',data=intel , auth = inf)
                try:
                    search = re.search('"status": {"code": 290', message.text)
                    if  search :
                       print(Fore.GREEN + '''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃   Statues                             ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}                ┃Sent                                   ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                    else:
                        print('''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃    Message ID                         ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}           ┃Failed ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                except Exception as e:
                    pass
        elif Choice == '14':

            print('''
            {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
            {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
            {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
            {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
            {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
            {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
            {2} ┃                          {0}▀           ▐                            {2}┃
            {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {2} ┃         {0}Textbelt Bulk SENDER      {2}┃         {0}CODED BY xMarvel      {2}┃
            {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

            '''.format(fg[0], fg[1], fg[5], fg[4]))

            read_config = configparser.ConfigParser()
            read_config.read("Senders-configs/textbelt_Config.ini")

            acc_tok = read_config.get("Section1", "api_key")
            MSG = read_config.get("Section1", "Message")
            print('''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃                          [+] Textbelt CONFIG [+]                        ┃
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                        ''')
            print(f'''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃    API KEY                          ┃  {acc_tok}   ┃                             
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
            reseee = Style.RESET_ALL
            list = input(f"          \033[0;37;45mYour Number List:~#{reseee} ")
            numberass = sum(1 for line in open(list))
            openit = open(list, 'r')
            for i in range(0, numberass):
                recipent =  str(openit.readline())
                ses = requests.session()
                intel = {
                    "phone": str(recipent),
                    "message": str(MSG),
                    "key": str(acc_tok)
                    }
                message = ses.post('https://textbelt.com/text',json=intel)
                bal = message.json()
                balance = str(bal['quotaRemaining'])
                try:
                    if str(bal['success']).lower() == 'true' :
                       print(Fore.GREEN + '''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃   Statues                             ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}                ┃Sent                                   ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                    else:
                        print('''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃    Message ID                         ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}           ┃Failed ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                except Exception as e:
                    pass
        elif Choice == '15':

            print('''
            {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
            {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
            {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
            {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
            {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
            {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
            {2} ┃                          {0}▀           ▐                            {2}┃
            {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {2} ┃         {0}SMS77 Bulk SENDER         {2}┃         {0}CODED BY xMarvel      {2}┃
            {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

            '''.format(fg[0], fg[1], fg[5], fg[4]))

            read_config = configparser.ConfigParser()
            read_config.read("Senders-configs/SMS77_Config.ini")

            api_key = read_config.get("Section1", "api_key")
            sender_id = read_config.get("Section1", "sender_id")
            MSG = read_config.get("Section1", "Message")
            print('''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃                          [+] SMS77 CONFIG [+]                           ┃
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                        ''')
            print(f'''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃    API KEY                       ┃  {api_key}   ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Sender ID                        ┃  {sender_id}                                ┃                               
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
            reseee = Style.RESET_ALL
            list = input(f"          \033[0;37;45mYour Number List:~#{reseee} ")
            numberass = sum(1 for line in open(list))
            openit = open(list, 'r')
            for i in range(0, numberass):
                recipent =  str(openit.readline())
                ses = requests.session()
                inf = (str(api_key),str())
                intel = {
                    "p": str(api_key),
                    "to": str(recipent),
                    "text": str(MSG),
                    "from": str(sender_id)
          
                    }
                message = ses.post('https://gateway.sms77.io/api/sms',params=intel)
                bal = ses.get(f'https://gateway.sms77.io/api/balance?p={str(api_key)}')
                balance = bal.text
                try:
                    search = re.search('100', message.text)
                    if search:
                       print(Fore.GREEN + '''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃   Statues                             ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}                ┃Sent                                   ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                    else:
                        print('''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃    Message ID                         ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}           ┃Failed ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                except Exception as e:
                    pass
        elif Choice == '16':

            print('''
            {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
            {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
            {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
            {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
            {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
            {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
            {2} ┃                          {0}▀           ▐                            {2}┃
            {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {2} ┃         {0}SMSBEEP Bulk SENDER       {2}┃         {0}CODED BY xMarvel      {2}┃
            {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

            '''.format(fg[0], fg[1], fg[5], fg[4]))

            read_config = configparser.ConfigParser()
            read_config.read("Senders-configs/SMSBEEP_Config.ini")
            user_name = read_config.get("Section1", "user_name")
            api_key = read_config.get("Section1", "api_key")
            sender_id = read_config.get("Section1", "sender_id")
            MSG = read_config.get("Section1", "Message")
            print('''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃                          [+] SMSBEEP CONFIG [+]                         ┃
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                        ''')
            print(f'''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃    API KEY                       ┃  {api_key}  ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Sender ID                        ┃  {sender_id}                                ┃                               
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
            reseee = Style.RESET_ALL
            list = input(f"          \033[0;37;45mYour Number List:~#{reseee} ")
            numberass = sum(1 for line in open(list))
            openit = open(list, 'r')
            for i in range(0, numberass):
                recipent =  str(openit.readline())
                ses = requests.session()
                inf = (str(api_key),str())
                intel = {
                    "username":str(user_name),
                    "apikey": str(api_key),
                    "sender": str(sender_id),
                    "messagetext": str(MSG),
                    "flash": "0",  
                    "recipients": str(recipent)
                        }
                message = ses.get('http://api.smsbeep.com/sendsms',params=intel)
                bal = ses.get(f'http://api.smsbeep.com/balance/{str(user_name)}/{str(api_key)}')
                balance = bal.text
                search = re.search('SUCCESS', message.text)
                try:
                    if search:
                       print(Fore.GREEN + '''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃   Statues                             ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}                ┃Sent                                   ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                    else:
                        print('''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃    Message ID                         ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}           ┃Failed ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                except Exception as e:
                    pass

        elif Choice == '17':

            print('''
            {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
            {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
            {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
            {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
            {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
            {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
            {2} ┃                          {0}▀           ▐                            {2}┃
            {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {2} ┃         {0}PROOVL Bulk SENDER        {2}┃         {0}CODED BY xMarvel      {2}┃
            {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

            '''.format(fg[0], fg[1], fg[5], fg[4]))

            read_config = configparser.ConfigParser()
            read_config.read("Senders-configs/PROOVL_Config.ini")
            user = read_config.get("Section1", "user_name")
            token = read_config.get("Section1", "token")
            sender_id = read_config.get("Section1", "sender_id")
            MSG = read_config.get("Section1", "Message")
            print('''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃                          [+] PROOVL CONFIG [+]                          ┃
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                        ''')
            print(f'''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃    API KEY                       ┃  {token}  ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Sender ID                        ┃  {sender_id}                                ┃                               
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
            reseee = Style.RESET_ALL
            list = input(f"          \033[0;37;45mYour Number List:~#{reseee} ")
            numberass = sum(1 for line in open(list))
            openit = open(list, 'r')
            for i in range(0, numberass):
                recipent =  str(openit.readline())
                hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
                ses = requests.session()
                inf = (str(token),str())
                intel = {
                    "user": str(user),
                    "token": str(token),
                    "from": str(sender_id),
                    "to": str(recipent),
                    "text": str(MSG)
                    }
                message = ses.post('https://www.proovl.com/api/send.php',params=intel,headers=hdr)
                bal = ses.get(f'https://www.proovl.com/api/balance.php?user={str(user)}&token={str(token)}')
                balance = bal.text
                me = message.text.split(';')
                g = me[1].replace("\"","").strip()
                balance = bal.text
                search = re.search('SUCCESS', message.text)
                try:
                    if me[1] != 'Authorization error':
                        print('''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃    Message ID                         ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}           ┃Failed ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))                        
                       
                    else:
                        print(Fore.GREEN + '''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃   Statues                             ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}                ┃Sent                                   ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))
                except Exception as e:
                    pass
        elif Choice == '18':

            print('''
            {2} ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
            {2} ┃                {0}▄  █▀▄▀█ ██   █▄▄▄▄    ▄   ▄███▄   █               {2}┃
            {2} ┃            {0}▀▄   █ █ █ █ █ █  █  ▄▀     █  █▀   ▀  █               {2}┃
            {2} ┃              {0}█ ▀  █ ▄ █ █▄▄█ █▀▀▌ █     █ ██▄▄    █               {2}┃  
            {2} ┃             {0}▄ █   █   █ █  █ █  █  █    █ █▄   ▄▀ ███▄            {2}┃
            {2} ┃            {0}█   ▀▄    █     █   █    █  █  ▀███▀       ▀           {2}┃
            {2} ┃             {0}▀       ▀     █   ▀      █▐                           {2}┃
            {2} ┃                          {0}▀           ▐                            {2}┃
            {2} ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
            {2} ┃         {0}phcomm Bulk SENDER        {2}┃         {0}CODED BY xMarvel      {2}┃
            {2} ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛ 

            '''.format(fg[0], fg[1], fg[5], fg[4]))

            read_config = configparser.ConfigParser()
            read_config.read("Senders-configs/phcomm_Config.ini")
            acc_tok = read_config.get("Section1", "Accsses_Token")
            sender_id = read_config.get("Section1", "sender_id")
            MSG = read_config.get("Section1", "Message")
            print('''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃                          [+] phcomm CONFIG [+]                          ┃
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                        ''')
            print(f'''
             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
             ┃    API KEY                       ┃  {acc_tok}  ┃
             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
             ┃    Sender ID                        ┃  {sender_id}                                ┃                               
             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛''')
            reseee = Style.RESET_ALL
            list = input(f"          \033[0;37;45mYour Number List:~#{reseee} ")
            numberass = sum(1 for line in open(list))
            openit = open(list, 'r')
            for i in range(0, numberass):
                recipent =  str(openit.readline())
                hdr = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' }
                ses = requests.session()
                inf = (str(acc_tok),str())
                intel = {
                    "sender": str(sender_id),
                    "content": str(MSG),
                    "phone": str(recipent),
                    }
                headers = {
               'Authorization': 'Bearer ' +str(acc_tok)
                    }
                message = ses.post('https://sms.phcomm.biz/api/v1/messages/send',data=intel,headers=headers)
                search = re.search('"message":"Queued Succesfully"', message.text)
                search = re.search('SUCCESS', message.text)
                try:
                    if search:
                        print(Fore.GREEN + '''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃   Statues                             ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}                ┃Sent                                   ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))                        
                        
                       
                    else:
                        print('''
                             ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                             ┃    Number                       ┃    Message ID                         ┃
                             ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                             ┃    {}           ┃Failed ┃
                             ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛'''.format(
                        recipent))                        
                except Exception as e:
                    pass
        elif Choice == '28' or '29' or '30' or '31':
            print('\033[31mFeature currently not available!')
        else:
            print(' lol ')
    choose_service()
Auth_check()
