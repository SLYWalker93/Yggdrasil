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
from path1 import path_f_2_1
from path1 import path_f_2_2
from path1 import path_f_2_3

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
    print " "
    print "Your MOTHER takes a moment to take in the sight of you: a tear comes to her eye."
    print "Though she may not admit it, she fears she may not see you again."
    print " "
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
if (go_on_3 =="n"):
    print "Thanks for playing!"

elif (go_on_3=="y"):

    os.system('clear')

    print "THE FOREST-PART II"
    print " "
    print " "
if answer=="continue":
    print "You continue on the path ahead, ever wary of danger."
    print "You venture further into the forest as the shadows grow, and eventually"
    print "consume the woods. You begin to hear the calls of savage bests,"
    print " the howls of wolves, and screeches of nocturnal birds on the hunt."
    print "Fear begins to set in; though you are brave, the tales you heard in youth torture your imagination."
    print "You begin to panic, and clamor through the dark, searching for shelter."
    print "You finally find it; a small cave, elevated from the forest floor, atop a cliff."
    print "You hoist your baggage and begin the climb, desperate to escape the cacophany of the forest."
    print "You finally reach the top, breathe a sigh of relief, and set up camp, just outside the cave, safe."
    print "Or so you think..."
    print " "
    print " "
    print "Your fire grows dim, and the night winds cut through your blankets,"
    print "But you endure, and finally fall asleep. Though it does not last."
    print "Soon after you have slipped into the grasp of Morpheus, you feel a soft rumble on the ground."
    print "It is coming from the cave, and grows ever larger."
    print " "
elif answer=="go into the light":
    print " "
    print "After your encounter with the fairies, your mother's message hits home."
    print "You must be on guard at all times in the forest."
    print " "
    print " "
    print "You venture further into the forest as the shadows grow, and eventually"
    print "consume the woods. You begin to hear the calls of savage bests,"
    print " the howls of wolves, and screeches of nocturnal birds on the hunt."
    print "Fear begins to set in; though you are brave, the tales you heard in youth torture your imagination."
    print "You begin to panic, and clamor through the dark, searching for shelter."
    print "You finally find it; a small cave, elevated from the forest floor, atop a cliff."
    print "You hoist your baggage and begin the climb, desperate to escape the cacophany of the forest."
    print "You finally reach the top, breathe a sigh of relief, and set up camp, just outside the cave, safe."
    print "Or so you think..."
    print " "
    print " "
    print "Your fire grows dim, and the night winds cut through your blankets,"
    print "But you endure, and finally fall asleep. Though it does not last."
    print "Soon after you have slipped into the grasp of Morpheus, you feel a soft rumble on the ground."
    print "It is coming from the cave, and grows ever larger."
    print " "

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
    print "Terror fills your body as you stare into the eyes of the creature."
    print "It licks its chops and stares through to your soul."
    print "To your surprise, despite having your weapon raised,"
    print "it sits, looking at you with as much curiosity as rabid hunger."
    print " "
elif choiceweapon=="bow and dagger":
    print "You draw your bow back and aim for the creature's head."
    print "Sweat covers your hands, and you slip, a rare mistake."
    print "You hit the creature in its shoulder, but it bounces right off."
    print " "
    print "WOLF: Oh, come now. You're better than sneaking about in the dark,"
    print "my human friend. Your species' weaponry is as useless as it's always been."
    print "Come out, and we can have, a friendly discussion."
    print " "
if choiceweapon=="bow and dagger":
    stealthchoice=raw_input("What will you do? 'flee,' or 'face the wolf?''")
if choiceweapon=="bow and dagger" and stealthchoice==("flee"):
    print "You flee back into the woods, the wolf none the wiser, though you left your"
    print "bag behind."
elif choiceweapon=="bow and dagger" and stealthchoice==('face the wolf'):
    print " "
    print "You decide to face the creature, and jump down."
    print "Terror fills your body as you stare into the eyes of the creature."
    print "It licks its chops and stares through to your soul."
    print "To your surprise, despite having your weapon raised,"
    print "it sits, looking at you with as much curiosity as rabid hunger. "
    print " "
    print " "
    
