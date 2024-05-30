fruits = ["apple", "banana", "orange"]

#accessing by indexing
#print(fruits[0])

#slicing
#print(fruits[0:3])

#Modifying Lists
fruits.append("Guava") #add an item at the end of the list similar to js push

fruits.insert(2,"Apple") #Inserts an item at a specific index.

fruits.pop(0) #Removes and returns the element at a given index (default is the last).
fruits.clear() #clears the entire content of the list from the memory

#since i cleared the list i think something must be done
second_fruitList =  ["Apple", "Banana", "Orange", "Mango", "Grape",
          "Strawberry", "Blueberry", "Pineapple", "Watermelon",
          "Kiwi", "Peach", "Pear", "Coconut", "Dragonfruit", "Avocado"]


fruits.extend(second_fruitList) #adds the contents of the new list to the parent one
thirdList = fruits.copy() #copying the content of another list to a  new list
fruits.remove("Kiwi") #removes a specific item
#print(thirdList)

#List operations
length = len(fruits) #gives the length of a given array
check = "Peach" in fruits #Checking if the item is available in the list
#print(check)

#playground

numberedList = []

nums = 0
while nums <= 13:
    numberedList.append(nums)
    nums = nums + 1

numberedList.reverse() #reverses the items of the list
numberedList.sort()
#print(numberedList)

userChoiceOfFoods = []
numOfTurns = 12
loopValue = 0
while loopValue <= numOfTurns:
    userAction = input("Enter the names of foods you have eaten before: ")
    userChoiceOfFoods.append(userAction)
    loopValue = loopValue + 1

#print(userChoiceOfFoods)