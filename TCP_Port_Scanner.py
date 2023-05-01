from socket import *
import sys
from threading import *
from datetime import datetime
import os
import art


def clear():
 
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
clear()

print(art.text2art("                                         Port  Scanner"))

try:
    host = input("\nEnter the Domain name/ ip address =  ")
    resolvedip = gethostbyname(host)
except:
    sys.exit("Check your domain , Entered domain not found")

normalPortStart = 1
normalPortEnd = 1024
allPort = 1
allPortEnd = 65535
customPortStart = 0
customPortEnd = 0

print('\n')
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Select your scan type: ")
print("[+] Select 1 for Normal Ports scaning")
print("[+] Select 2 for All Ports scaning")
print("[+] Select 3 for custom port scaning")
print("[+] Select 4 for exit \n")

mode = int(input("[+] Select any option: "))
print()

if mode == 3:
    customPortStart = int(input("[+] Enter starting port number: "))
    customPortEnd = int(input("[+] Enter ending port number: "))

print("-"*50)
print(f"Target IP: {host}")
print("Scanning started at:" + str(datetime.now()))
print("-"*50)


allports = []
def get_ports(mode):
    if mode == 1:
        print("\n[+] scaning..\n")
        for port in range(normalPortStart, normalPortEnd+1):
            allports.append(port)
    elif mode == 2:
        print("\n[+] scaning..\n")
        for port in range(allPort, allPortEnd+1):
            allports.append(port)
    elif mode == 3:
        print("\n[+] scaning..\n")
        for port in range(customPortStart, customPortEnd+1):
            allports.append(port)
    elif mode == 4:
        print("[-] Exiting...")
        sys.exit()

setdefaulttimeout(0.01)
lock = Lock()
thread_array = []
main_array = []

def conn(ipx,portx,lock,mode):
    addr = (ipx,portx)
    s = socket(AF_INET,SOCK_STREAM)
    result = s.connect_ex(addr)
    s.close()
    lock.acquire() 
    if(result == 0):
        main_array.append(portx)
        print("Port ",format(portx)," is open")
    else:
        print("Port ",format(portx)," is not open")
    lock.release()

get_ports(mode)   
for port in allports:
    t = Thread(target = conn , args = (host,port,lock,mode)) 
    thread_array.append(t)
    t.start()
    

for thread in thread_array:
    thread.join()

print("-"*50)
print("port that are open are ",main_array)
print("-"*50)

print(f"Scanning compleate in: {current_time}")
