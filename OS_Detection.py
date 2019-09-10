import os
import pyfiglet
from pyfiglet import fonts
from colorama import Fore, Back, Style
from colorama import init

# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
Y = '\033[93m'
BOLD = '\033[1m'
END = '\033[0m'

def banner():

	ascii_banner = pyfiglet.figlet_format("OS Detection")
	print(BOLD+P+ascii_banner+END)
	print P+"Thanks: Nmap, NmaptoCSV Developers...\n\n"+END

def scansingle(ip):
	cmd = "nmap -sS -sV -Pn -n -p 22,445,135,21,111,139 --open -O -T4  -oA  output "+ip
	print (BOLD+O+cmd+END)
	os.system(cmd)
	nmaptocsv()

def scan(ip_list):
        cmd = "nmap -sS -sV -Pn -n -p 22,445,135,21,111,139 --open  --osscan-guess -O -T4  -oA  output -iL "+ip_list
        print (BOLD+O+cmd+END)
        os.system(cmd)
        nmaptocsv()
	

def nmaptocsv():
	cmd1 = 'nmaptocsv -i output.nmap -d ","  -f ip-os -o os_detected.csv -n'
	os.system(cmd1)
	print BOLD+G+"[*] Check os_detected.csv File.."+END

def nmaptocsv1(filepath):
        cmd1 = 'nmaptocsv -i '+filepath+' -d "," -f ip-os -o os_detected.csv -n'
        os.system(cmd1)
	print BOLD+G+"[*] Check os_detected.csv File.."+END

def main():
	init()
	banner()
	try:
		print G+"Select One Option"+END
		print O+"1. OS Detection Of Single IP Address"+END
		print O+"2. OS Detection Of Multiple IP Addresses"+END
		print O+"3. OS Detection By Nmap Output\n"+END
		option = raw_input(BOLD+R+"Please choose one option: "+END)
		if(option == "1"):
			ip = raw_input(O+"Enter the IP Address: "+END)
			scansingle(ip)
		elif(option == "2"):
			ip_list = raw_input(O+"Enter the IP Address List (Complete Path): "+END)
			scan(ip_list)
		elif(option == "3"):
			filepath = raw_input(O+"Enter the .nmap File Path (Complete Path): "+END)
			nmaptocsv1(filepath)
		else:
			print BOLD+R+"You didn't select any option..."+END

	except KeyboardInterrupt:
                print "\nKeyboard Interrupt..."
	except IOError,i:
                print "\nInput Output Error..."
                print i


if __name__ =='__main__':
        main()
