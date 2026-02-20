from random import randint #This line imports the randint function from the random module. The randint function generates a random integer between two specified values


ranNums = [] #name your list and make sure it is empty!

# Generates a list of 5 or 10 random integers between 1 and 50 inclusive.
length = int(input("How long do you want the list to be? "))
for i in range(length): #for loop appends "length" numbers to your list, but make sure you name your variable
    ranNums.append(randint(1,50)) #this adds a random number between 1-50 to the list
ranSearch = int(input("What number do you want to search for?"))
print("You are searching for", ranSearch)

searches = 0
comparisons = 0  # Initialize the counter for comparisons
found = True  # Variable to track if the number was found

while found:
    print(ranNums)
    if len(ranNums) == 1:
        if ranNums[0] == ranSearch:
            found = False
        else:
            break
    else:
        if ranSearch == ranNums[len(ranNums)//2]:
            found = False
        elif ranSearch > ranNums[len(ranNums)//2]:
            ranNums = ranNums[len(ranNums)//2 : len(ranNums)]
        elif ranSearch < ranNums[len(ranNums)//2]:
            ranNums = ranNums[0 : len(ranNums)//2]
    comparisons +=1


print(f"The number of comparisons is {comparisons}")
if found == True:
    print("The number is not in the list")
else:
    print("The number is in the list")