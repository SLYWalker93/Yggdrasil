import os
from path1 import path_1
from path1 import path_1_1
from path1 import path_1_2
from path1 import path_1_3
from path1 import path_f_1
from path1 import path_f_2
 #importing path_1 function from path1.py
#import path2
#import path3
#using import os for clearing screen on mac and linux

#this will be our main file for story and logic
os.system('clear')

print "THE QUEST FOR THE SACRED WATER"

print " "
print "For generations, your clan, the Sentries of the Southern Village have safeguarded the Great Tree."
print "People from all over the kingdom came to receive healing from the tree's sap."
print "Tragedy has struck; raiders attacked the village, hoping to use the tree for themselves, and it was scorched and deformed from flaming projectiles and torches."
print "Many brave sentries lost their lives, many your loved ones."
print "Since then, the Great Tree's healing properties have waned, the sap turned bitter."
print "All over the kingdom people grow sick with a new disease brought by the barbarians; medics and priests are unable to heal it."
print "All attempts to heal the tree were in vain. The greatest mystics and most talented alchemists were powerless to remedy damage."
print "Legend tells of a healing water, hidden away in a forgotten temple in the northernmost portion of the kingdom."
print "Only it can restore the tree to its former glory."
print "You are a young prodigy, who has the respect and admiration of the village for your bravery, and status as a Sentry."
print "The task has fallen to you; the sentries have also fallen victim to this great plague, and so you must make the trek north, and save your home!"


print " "
go_on = raw_input("Continue to page 2? Enter 'y' for yes, 'n' to end story.")
print "Enter 'y' for yes, 'n' to end story"
if (go_on == "y"):

    os.system('clear')  # on linux / os x

    print "Welcome to Your Quest!"

    print " "
    print " "

    print "You are sitting in your room. Recent events have left you unsettled."
    print "Raider attacks, recent diseases, and now even your own mother lies ill."
    print "She calls to you, and you heed her call. You find her lying in bed, the sickness present in her face."

    print " "

    print "MOTHER:For centuries, our clan has safeguarded the tree of life."
    print "We have ensured that pilgrims from across the realm may benefit from its healing properties."
    print "But, I, and all the sentries, have failed this day, my child."
    print "Your training is complete. Now, you must choose your weapon."
    print "The wilds are fraught with dangers. Go over to the chest, at the end of my bed."
    print "Now, choose, my child. What shall safegaurd you, on your mission?"
    print " "
    print " "

    choice=raw_input ("You have three choices: sword and shield, bow and dagger, or staff and tome. Choose wisely...")
    if choice=="sword and shield" or choice=="sword":
        path_1() #prints out path 1's stories
    elif choice=="bow and dagger" or choice=="bow":
        path_1_1()
    elif choice=="staff and tome" or choice=="staff":
        path_1_2()
    else:
        path_1_3()
    print "Now, go my child. Fly fast and true, to the north."
    print "Your first challenge will be passing through the forest. Take care not to wander off the path."
    print "Dangerous creatures reside there. Some of them savage things. Others command the languge of men, and can bewitch you."
    print "I love you."
    print " "
    choice=raw_input ("You look on your mother one last time. Do you embrace her? Or do you turn and go, too proud to consider you may not see her again? Enter 'turn and go' or 'embrace.'")
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

    print "You are on the road now, a few miles away from your village."
    print "The forest stretches before you like an ocean of green, ready to engulf the weak."
    print "You take one last look at home before you carry on, your weapon clutched tightly."
    print " "
    print " "

    go_on = raw_input("Continue to page 3? Enter 'y' for yes, 'n' to end story.")
    if (go_on == "y"):

        os.system('clear')

print "THE FOREST"
print " "
print " "
print " "
print "The light grows dim as you venture deeper into the dense forest."
print "You hurdle over dead logs, pass over streams, and sneak past slumbering bears."
print "As the darkness grows, you notice a clearing in the distance, bathed in light."
print "However, it is off the beaten path your family has shown you before."
answer=raw_input("What will you do? Enter 'go into the light' or 'continue.'")
if answer=="go into the light":
    path_f_1()
elif answer== "continue":
    path_f_2()
