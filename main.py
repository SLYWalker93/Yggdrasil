import os
from path1 import path_1_a
from path1 import path_1_1
from path1 import path_1_2
from path1 import path_1_3
from path1 import path_f_1
from path1 import path_f_1_1
from path1 import path_f_1_2
from path1 import path_f_1_3
from path1 import path_f_1_4

 #importing path_1 function from path1.py
#import path2
#import path3
#using import os for clearing screen on mac and linux

#this will be our main file for story and logic
os.system('clear')

print "T H E  Q U E S T  F O R  T H E  S A C R E D  W A T E R"

print " "
print "For generations, your clan, the Sentries of the Southern Village have safeguarded the Great Tree."
print "People from all over the kingdom came to receive healing from the tree's sap."
print "Tragedy has struck; raiders attacked the village, hoping to use the tree for themselves."
print "The tree was scorched and deformed by flaming projectiles and torches."
print "Numerous Sentries lost their lives, many of them your friends and loved ones."
print "Since then, the Great Tree's healing properties have waned, and its sap turned bitter."
print "All over the kingdom people grow sick with a new disease brought by the barbarians."
print "The kingdom's medics and priests are unable to cure the disease, and need the Great Tree. "
print "All attempts to heal the tree were in vain."
print "The greatest mystics and most talented alchemists were powerless to remedy the damage."
print "Legend tells of a healing water, hidden away in a forgotten temple in the northernmost portion of the kingdom."
print "Only it can restore the tree to its former glory."
print "You are a young prodigy among the Sentries."
print "You have the respect and admiration of the village for your bravery, and come from a great line of warriors."
print "The task has fallen to you!"
print "the Sentries have also fallen victim to this great plague, and so you must make the trek north, and save your home!"


print " "
go_on = raw_input("Continue to page 2? Enter 'y' for yes, 'n' to end story.")
if (go_on=="n"):
    print "Thanks for playing!"

elif (go_on == "y"):

    os.system('clear')  # on linux / os x


    print "Welcome to Your Quest!"

    print " "
    print " "

    print "You are sitting in your room."
    print "It has been many months since the last raider attack."
    print "The leader of the Sentries called a meeting last week, and it was decided,"
    print "that you would undertake the great task, to seek out the lost Temple."
    print "You've donned your family Armor, said farewell to your friends, and must say goodbye to your mother."
    print "She calls to you, and you heed her call. You find her lying in bed, the sickness present in her face."

    print " "

    print "MOTHER: There you are my child. For centuries, our clan has safeguarded the Great Tree."
    print "We have ensured that pilgrims from across the realm may benefit from its healing properties."
    print "But I, and all the Sentries, have failed in our duty."
    print "Your training is complete. I see you've donned the Sentry's armor. It suits you."
    print "Now, you must choose your weapon."
    print "The wilds are fraught with dangers. Go over to the chest, at the end of my bed."
    print "Now, choose, my child. What shall safegaurd you, on your mission?"
    print " "
    print " "

    choiceweapon=raw_input ("You have three choices: sword and shield, bow and dagger, or staff and tome. Choose wisely...")
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
    print "Now, go my child. Fly fast and true, to the north."
    print "Your first challenge will be passing through the forest. Take care not to wander off the path."
    print "Dangerous creatures reside there. Some of them savage things. Others command the languge of men, and can bewitch you."
    print "I love you."
    print " "
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

    print "You are on the road now, a few miles away from your village."
    print "The forest stretches before you like an ocean of green, ready to engulf the weak."
    print "You take one last look at home before you carry on, your weapon clutched tightly."
    print " "
    print " "

    go_on_2= raw_input("Continue to page 3? Enter 'y' for yes, 'n' to end story.")
    if (go_on_2 == "n"):
        print "Thanks for playing!"

    elif (go_on_2=="y"):

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

go_on_3= raw_input("Continue to page 4? Enter 'y' for yes, 'n' to end story.")
if (go_on_3 == "n"):
    print "Thanks for playing!"

elif (go_on_3=="y"):

    os.system('clear')

    print "THE FOREST-PART II"
    print " "
    print " "
if answer=="continue":
    print "You continue on the path ahead, ever wary of danger."
elif answer=="go into the light":
    print "After your encounter with the fairies, your mother's message hits home."
    print "You must be on guard at all times in the forest."
