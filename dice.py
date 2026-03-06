import random
import time
import os

# ==VERSON - 1.0 - GPL_3.0 ==
# yes this is one of the first programs i ever made
# and yes i could have made it better, but will i?
# no.

#numbers
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6

#start
print("welcome to dice! for linux only .")
time.sleep(5)
os.system('clear && echo made by classic14.')
time.sleep(3)
os.system('clear')

#main
random1 = input("type: roll to start. or type: how for how to play: ")
if random1 == "roll":
    os.system('clear')
    print("lets see what you get!")
    time.sleep(2)
    os.system('clear')
elif random1 == "how":
    os.system('clear')
    print("type (roll) to start. in this game you roll a dice. and the higher the numbers you get. the better your score!")
    time.sleep(5)
    os.system('clear')
    exit()
else:
     print("you cant type that right now!")
     exit()
     
options = (a, b, c, d, e, f)
chosen = random.choice(options)

print("you got!", chosen)
    


              
