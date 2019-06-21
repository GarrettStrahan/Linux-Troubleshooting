#Written in Python,
#Code for Linux Troubleshooting. Tested with a Ubuntu 18.04

import os

os.system('touch ~/TestInformation.txt')

sudoPassword = 'REPLACE THIS yOuRpAsSwOrD HeRe!'

print("What is your version of Linux?")
os.system('echo What is your version of Linux? : > ~/TestInformation.txt')
os.system('lsb_release -a >> ~/TestInformation.txt')

print("\nIP Information:")
os.system('echo IP Information: >> ~/TestInformation.txt')
os.system('ifconfig >> ~/TestInformation.txt')

print("\nVarious Hardware information")
os.system('echo Various Hardware information >> ~/TestInformation.txt')
os.system('echo %s|sudo -S %s' % (sudoPassword, 'lshw -short >> ~/TestInformation.txt'))

print("\nCan you reach Google?")
os.system('echo "\nCan you reach Google?" >> ~/TestInformation.txt')
os.system('ping 8.8.8.8 -c 5 >> ~/TestInformation.txt')

print("\nYour route to google:")
os.system('echo "\nYour route to google:" >> ~/TestInformation.txt')
os.system('traceroute 8.8.8.8 >> ~/TestInformation.txt')

print("\nNetstat information:")
os.system('echo Netstat information: >> ~/TestInformation.txt')
os.system('netstat >> ~/TestInformation.txt')

print("\nHard drive information")
os.system('echo "\nHard drive information:" >> ~/TestInformation.txt')
os.system('lsblk >> ~/TestInformation.txt')

print("\nYour routing information")
os.system('echo "\nYour routing information:" >> ~/TestInformation.txt')
os.system("route >> ~/TestInformation.txt")

print("\nethtool information:")
os.system('echo "\nethtool information:" >> ~/TestInformation.txt')
os.system('ethtool eth0 >> ~/TestInformation.txt >> ~/TestInformation.txt')
os.system('ethtool wlp1s0 >> ~/TestInformation.txt')


print("\nChecking DNS information:")
os.system('echo "\nChecking DNS information:" >> ~/TestInformation.txt')
os.system('cat /etc/resolv.conf >> ~/TestInformation.txt >> ~/TestInformation.txt')
os.system('nslookup gw.isp.com >> ~/TestInformation.txt')


print("\nYour hostname is:")
os.system('echo "\nYour hostname is: >> ~/TestInformation.txt')
os.system('hostname >> ~/TestInformation.txt')

print("\nYour loaded modules")
os.system('echo "\nYour loaded modules:" >> ~/TestInformation.txt')
os.system('lsmod >> ~/TestInformation.txt')

print("\nYour allowed hosts")
os.system('echo "\nYour allowed hosts:" >> ~/TestInformation.txt')
os.system('cat /etc/hosts.allow >> ~/TestInformation.txt')

print("\nYour denied hosts >> ~/TestInformation.txt")
os.system('echo "Your denied hosts:" >> ~/TestInformation.txt')
os.system('cat /etc/hosts.deny >> ~/TestInformation.txt')

print("\nYour memory information:")
os.system('echo Your memory information: >> ~/TestInformation.txt')
os.system('cat /proc/meminfo >> ~/TestInformation.txt')

print("\nYour CPU information:")
os.system('echo "\nYour CPU information:" >> ~/TestInformation.txt')
os.system('cat /proc/cpuinfo >> ~/TestInformation.txt')

print("\nThis might work or not on your system: CPU temp")
os.system('echo "\nThis might work or not on your system: CPU temp" >> ~/TestInformation.txt')
os.system('cat /proc/acpi/thermal_zone/THRM/temperature >> ~/TestInformation.txt')

print("\nList PCI:")
os.system('echo "\nList PCI:" >> ~/TestInformation.txt')
os.system('lspci >> ~/TestInformation.txt')

print("\nUSB devices:")
os.system('echo "\nUSB devices:" >> ~/TestInformation.txt')
os.system('lsusb >> ~/TestInformation.txt')

print("\nFree Disk Space:")
os.system('echo "\nFree Disk Space:" >> ~/TestInformation.txt')
os.system('df -h >> ~/TestInformation.txt')

print("\nYour processes your running:")
os.system('echo "\n Your processes your running:" >> ~/TestInformation.txt')
os.system('ps >> ~/TestInformation.txt')

os.system('echo "\nSome other commands you could run: nload, top, but they will take up the whole screen and stop the progress of this program" >> ~/TestInformation.txt')
print("\nSome other commands you could run: nload, top, but they will take up the whole screen and stop the progress of this program")