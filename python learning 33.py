import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["A", "K", "Q", "J", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

#number = random.randint(low, high) #output - choose any random number between low to high
#number = random.random() #output - floating number
#number = random.choice(options)  #output - guess rock/paper/scissors

random.shuffle(cards)

print(cards)