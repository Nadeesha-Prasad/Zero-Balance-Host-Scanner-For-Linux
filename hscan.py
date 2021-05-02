import os, requests, colorama
from colorama import Fore
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
reset = Fore.RESET

#banner
banner = """ 
   __  __           __                  
   / / / /___  _____/ /_                 
  / /_/ / __ \/ ___/ __/                 
 / __  / /_/ (__  ) /_                   
/_/_/_/\____/____/\__/_  ____  ___  _____
  / ___/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
 (__  ) /__/ /_/ / / / / / / /  __/ /    
/____/\___/\__,_/_/ /_/_/ /_/\___/_/    v.1.0                                    
"""
os.system("clear")
print(green + banner + reset)

print(green + "[1]" + reset + "Dialog")
print(green + "[2]" + reset + "Mobitel")
print(green + "[3]" + reset + "Airtel")
while True:
    try:
        isp = int(input(yellow + "Please select your ISP " + green + ">>>" + reset))
        if 0 < isp <= 3:
            break
        else:
            print(red+"Invalid value, please try agein!!"+reset)
            continue
    except:
        print(red+"Invalid value, please try agein!!"+reset)
        continue
isp_selfcare = ""
if isp == 1:
    isp_selfcare = "www.dialog.lk"
elif isp == 2:
    isp_selfcare = "202.129.235.210"
elif isp == 3:
    isp_selfcare = "staysafe.gov.lk"
else:
    isp_selfcare = "none"
pms = False
host_list = []
try :
    requests.post(f"http://{isp_selfcare}", timeout=2)
    pms = True
except:
    pms = False
    print(red + "OOPs...Your internet connection is not stable, Please Try agein!" + reset)
if pms == True:
    while True:
        try:
            ask_host_list = input(yellow + "Enter host list " + green + ">>>" + reset)
            h_list = open(str(ask_host_list), "r")
            new_file = input(yellow + "Enter name of output file " + green + ">>>" + reset)
            break
        except:
            print(red + "Please check your host list and try agein!" + reset)
            continue
    for x in h_list:
        try:
            requests.post(f"http://{x.strip()}", timeout=5)
            host_list.append(x)
        except:
            pass
    with open(f"{new_file}.txt", "w+") as file1:
        for x in host_list:
            file1.writelines(x)
    print(green + "done" + reset)
else:
    print("Fuck")
