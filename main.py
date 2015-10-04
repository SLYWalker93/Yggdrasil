import os
from path1 import *


 #importing path_1 function from path1.py
#import path2
#import path3
#using import os for clearing screen on mac and linux

#this will be our main file for story and logic
os.system('clear')

print "T H E  Q U E S T  F O R  T H E  S A C R E D  W A T E R"
path_prime()
print " "
go_on = raw_input("Enter 'y' to continue story.")
if (go_on=="n"):
    print "Thanks for playing!"
elif (go_on == "y"):

    os.system('clear')  # on linux / os x

    print "Welcome to Your Quest!"
    path_prime_2()

    choiceweapon=raw_input ("You have three choices: 'sword and shield,' 'bow and dagger,' 'or staff and tome.' Choose wisely...")
    if choiceweapon=="sword and shield":
        path_1_a() #prints out path 1's stories
    else:
        if choiceweapon=="bow and dagger":
            path_1_1()
        else:
            if choiceweapon=="staff and tome":
                path_1_2()
            else:
                path_1_3()
    #elif choiceweapon=="bow and dagger" or "bow":

    #elif choiceweapon=="staff and tome" or "staff":
    #    path_1_2()
    #else:
    #    path_1_3()
    path_prime_3()

    choice=raw_input ("You look on your mother one last time. Do you embrace her? Or do you turn and go? Enter 'turn and go' or 'embrace.'")
    if choice=="embrace":
        print " "
        print "You embrace your sick mother, kissing her on the cheek, then rise to face the challenges ahead of you."
        print " "
        print " "
    elif choice=="turn and go":
        print " "
        print "You know your mother is ill, and it's too risky to endanger your own life. You turn to face the challenges ahead."

        print " "
        print " "

    path_prime_4()

    go_on_2= raw_input("Enter 'y' to continue story.")
    if (go_on_2 == "n"):
        print "Thanks for playing!"

    elif (go_on_2=="y"):

        os.system('clear')

        path_prime_5()

    answer=raw_input("What will you do? Enter 'go into the light' or 'continue.'")
    if (answer=="continue"):
        print "You ignore the light, heeding your mother's warning about the dangers of the forest."

    elif answer=="go into the light":
        path_f_1()
        path_f_1_1()

        if choiceweapon=="sword and shield":
            path_f_1_2()
        elif choiceweapon=="staff and tome":
            path_f_1_3()
        elif choiceweapon=="bow and dagger":
            path_f_1_4()

    print " "
    print " "

go_on_3= raw_input("Enter 'y' to continue.")
if (go_on_3 =="n"):
    print "Thanks for playing!"

elif (go_on_3=="y"):

    os.system('clear')

    print "THE FOREST-PART II"
    print " "
    print " "
if answer=="continue":
    path_f_1_5()
elif answer=="go into the light":
    path_f_1_6()

fightorflight=raw_input("What shall you do? 'stay and fight,' or 'flee?'Choose one...")

os.system('clear')
print " "
print " "
if fightorflight=="flee":
    print "You flee the scene, leaving some of your gear behind in your excitement,"
    print "back into the forest's maw."
elif fightorflight=="stay and fight":
    print "You prepare yourself, readying your weapon once again; you shall fear no creature!"
if choiceweapon=="sword and shield":
    path_f_2_1()
if choiceweapon=="staff and tome":
    path_f_2_2()
if choiceweapon=="bow and dagger":
    path_f_2_3()
    print " "
    print " "
if choiceweapon=="sword and shield" or choiceweapon=="staff and tome":
    path_f_2_4()
elif choiceweapon=="bow and dagger":
    path_f_2_5()
    stealthchoice=raw_input("What will you do? 'flee,' or 'face the wolf?''")
if choiceweapon=="bow and dagger" and stealthchoice==("flee"):
    print "You flee back into the woods, the wolf none the wiser, though you left your"
    print "bag behind."
elif choiceweapon=="bow and dagger" and stealthchoice==('face the wolf'):
    path_f_2_6()
