import os
#using import os for clearing screen on mac and linux

#this will be our main file for story and logic

print "THE QUEST FOR THE SACRED WATER"


print " "
print "For generations, your clan, the Sentries of the Southern Village have safeguarded the Great Tree."
print "People from all over the kingdom came to receive healing from the tree's sap."
print "Tragedy has struck; raiders attacked the village, hoping to use the tree for themselves, and it was scorched and deformed from flaming projectiles, and many brave sentries lost their lives."
print "Since then, the Great Tree's healing properties have waned, the sap turned bitter; all over the kingdom people grow sick with a new disease brought by the barbarians; medics and priests are unable to heal it."
print "All attempts to heal the tree were in vain. The greatest mystics and most talented alchemists were powerless to remedy damage."
print "Legend tells of a healing water, hidden away in a forgotten temple in the northernmost portion of the kingdom that can restore the tree to its former glory."
print "You are a young prodigy, who has the respect and admiration of the village for your bravery, and status as a Sentry."
print "The task has fallen to you; the sentries have also fallen victim to this great plague, and so you must make the trek north, and save your home!"


print " "
go_on = raw_input("Continue to page 2?")
print "Enter 'y' for yes, 'n' to end story"
if (go_on == "y"):

    os.system('clear')  # on linux / os x

    print "Welcome to Your Quest!"

    print " "
    print " "

    print "You are sitting in your room, "

    print "MOTHER:For centuries, our clan has safeguarded the tree of life. We have ensured that pilgrims from across the realm may benefit from its healing properties."
    print "But, I, and all the sentries, have failed this day, my child."
    print "Your training is complete. Now, you must choose your weapon."
    print "The wilds are fraught with dangers. Go over to the chest, at the end of my bed."
    print "Now, choose, my child. What shall safegaurd you, on your mission?"

    choice=raw_input ("You have three choices: sword and shield, bow and dagger, or staff and tome. Choose wisely...")
    if choice=="sword and shield" or choice=="sword":
        print "So, the blade. You always excelled in combat training. May it serve you well."
    elif choice=="bow and dagger" or choice=="bow":
        print "The stealth approach, eh? Take care not to let those sticky fingers get you into trouble!"
    elif choice=="staff and tome" or choice=="staff":
        print "Yes, of course. Your mind has always been your strongest asset. Take care not to shout. A mage's voice is their greatest weapon."
    else:
        print "My child, you must choose your weapon. Time is of the essence!"

    print " "

    print "You must venture to the northern wastes, and find the lost temple our ancestors once safeguarded."

    print "It is there you will find the sacred life-giving water, which can restore the tree we hold so dear."

    print "You will brave dangers and conquer challenges our people have not faced for a generation."

    print ""
