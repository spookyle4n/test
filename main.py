from random import seed
from random import randint
import time
import random
import string
import requests
print('''
\033[36m 
  _____     _____
 /____/|   /____/|_______________________________
|    | |  |    |/________/___________/_________\\ \\
|    | |  |    |   ___   |     __    |    ___   \\_\\
|    | /\ |    |  |   |  |    | |\\___|   |   |  | |
|    |/  \|    |  |___|  |    | |    |   |___|  |_|
 \             /         |    | |    |          / /
\033[37m  \___________/__________|____|_|    |_________/_/
   
               tiktok jahsehrare
               insta: spookyle4n\033[37m
''')
e = input("[?] Your schoology email?: ")
d = input("[?] Your schoology password? (bruteforce attack wont work without it): ")
print("attempting to log into schoology with...\033 " + e)
time.sleep(4)
print("\033[32msuccessfully logged in as " + e + " [\u2713]")

c = input("\033[37m[?] Victims schoology email?: ")
b = int(input("[?] How many passwords would you like to try?: "))
a = input("[?] Start Attack? [y/n]: ")
if a == 'y':
    print("\033[31mStarting bruteforce on " + c)
    time.sleep(2)
    for i in range(b):
        randomnumber = chr(random.randint(ord('0'), ord('9')))
        randomnumber2 = chr(random.randint(ord('0'), ord('9')))
        randomnumber3 = chr(random.randint(ord('0'), ord('9')))
        randomnumber4 = chr(random.randint(ord('0'), ord('9')))
        randomnumber5 = chr(random.randint(ord('0'), ord('9')))
        randomnumber6 = chr(random.randint(ord('0'), ord('9')))
        randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
        randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
        if randomnumber + randomLowerLetter == '9u':
            print("\033[32m\n\tsuccess! [\u2713] ")
            time.sleep(100000000)
            
        print("\033[31m[+] attempting... " + randomnumber + randomLowerLetter, flush=True)
        time.sleep(0.0001)
