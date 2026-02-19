from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values


ranNums = [] #name your list and make sure it is empty!


# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
for i in range(10): #for loop appends 5 numbers to your list, but make sure you name your variable
    ranNums.append(randint(1,50)) #this adds a random number between 1-50 to the list
print(ranNums)

ranSearch = randint(1,50)
print(ranSearch)

if ranSearch in ranNums:
    print("Number",ranSearch,"found in the list!")
else:
    print("Number",ranSearch,"not found in the list.")
