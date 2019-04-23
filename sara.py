# -*- coding: utf-8 -*-
import random
playerhand=[]
cpuhand = []
cpuhandview = []
listofmonopoly = ['Baltic Avenue', '2M', 'Medtierranean Avenue', 'States Avenue', '5M', 'St. Charles Place', 'Virginia Avenue', '1M', 'Indiana Avenue', '4M', 'illionis Avenue', '1M', 'Kentucky Avenue', '3M', 'St. James Place', 'New York Avenue', '4M', 'Tennesssee Avenue', 'Ventor Avenue', '10M', 'Marvin Gardens','2M', 'Atlantic Avenue', '1M', 'Pennsylvania Avenue', '3M', 'Pacific Avenue', '1M', 'North Carolina Avenue', 'Water Works', 'Electric Company', '4M', 'Connecticut Avenue', '3M', 'Vermont Avenue', 'Oriental Avenue', '1M', 'Boardwalk', 'Park Place', 'Reading Railroad', 'Short Line', '2M', 'Pennsylvania Railroad', '1M', 'B. & O. Railroad', 'Sly Deal', '2M', 'Forced Deal', '5M', 'Debt Collector']
print (listofmonopoly)

random.shuffle(listofmonopoly)
print (listofmonopoly)
for i in range (5):
  playerhandview = random.choice(listofmonopoly)
  playerhand.append (playerhandview)
  listofmonopoly.remove (playerhandview)
print (".............Player hand is......")
print(playerhand)
print(listofmonopoly) 
#cpuhand = random.shuffle
for i in range (5):
   playercpuhand = random.choice(listofmonopoly)
   cpuhand.append(playercpuhand)
   listofmonopoly.remove(playercpuhand) 
print ("..........cpu hand is.....")
print(cpuhand)
print(listofmonopoly)
cpuhandview = random.choice(listofmonopoly)
listofmonopoly.remove(cpuhandview)
