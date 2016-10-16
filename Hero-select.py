#Here we go!

#First we draw the data in from the raw-data.csv

from sys import exit
import csv

reader = csv.reader(open("raw-data.csv"))
dict1={}
for row in reader:
    dict1[row[0]]=row[1:]

for key in dict1:
    dict1[key] = [x for x in dict1[key] if x]

#Next step we load the masterlist

buffer1 = dict1['masterlist']

#Here's a list of hero quality:

#Done, next part we ask the user to input what qualities they're looking for

mode = True #mode1 = search, 2 = listing, 3 = exit
#while mode == 1:
while mode == True:
    print ("Input search criteria/\'List\':")
    argument = input(">").lower() #user input, we make it into lower case...
    argument = argument.replace(' ',"")#and join them to make sure they don't get error
    if argument in dict1:
        buffer1 = set(buffer1) & set(dict1[argument])
        print ()
        print ("Choose these:")
        for i in buffer1:
            print ("\t",i)
        print ()
        print ("Need more? Y/N")
        argument2 = input(">").lower()
        if argument2 == "n":
            break
    else:
        qualityList = ['Poke','Reveal','','Selfsustain','Sustaindamage','Poison','AOE Burst','Burst Damage','Giant Killer','Pet','','Tank','Wave Clear','Split Push','Siege','Ambusher','Bruiser','Diver','Stealth','Mage','Mobility','Fast Respawn','','Crowd Control','Interrupter','Stasis','Stun','Displacement','Root','Silence','Slow','Blind','','Melee','Ranged','Long range','Global Attack','Global Presence','','Buffer','Healer','Single Heal','Multi heal','Shields','Invulnerable']
        print ('                              List of qualities:')
        for i in qualityList:
            print (i)
