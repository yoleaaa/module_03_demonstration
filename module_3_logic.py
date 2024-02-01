"""
Author:Yuan Olea
Description:  intro to python control structures
date: 30 jan 2024
"""


#Sequintial, Selection, Iteration

#SELCTION
#Conditionals
#if something is the case, do one thing, otherwise, do another thing
"""
age = 20
#comparision evaluation
age == 0
print("not born yet")
# Boolean ; true or false 
if age < 13: 
    #age is less than thirteen meaning
    print("Child")


    if True:
    print("its true")

#if (value that is true):
    # run code
    if False:
    """



#Dynamic Code



#Vending machine app

#change = [5,10,25,100,200]
#price = 1.25
#input = 1.75
        

"""
calculate automatically how many pieces of change must be returned 
look at change denominations available
calculate how many of each are required and return them

if difference = 100, return 100
if difference - 50, return 2 x 25
if the difference = 25, return 25
"""

#for and while loops
#for loop is used when the number of iterations is known, whereas execution is
 #   done in a while loop until the statement in the program is proved wrong.

iterator = 0 
colours = ["red","green","green", "orange"]
found_colour = colours[iterator]

while found_colour != "yellow" and iterator < len(colours):
   iterator += 1 
found_colour = colours[iterator]
print(f"colour found at index{iterator}")


"""
user_input = int(input("enter a number greater than 10"))

while user_input <= 10 :
    print("sorry, try that again")
    user_input = int(input())
    print("great job!")
    """


"""
fruits = ['banana','pineapple', 'durian','apple']


for num in range:
   print(num)


   isTrue:True
   #infinite loop

   
#numbered the loop
   while isTrue:
      print("its a true")
      """
      

"""
fruits = ['banana','pineapple', 'durian','apple']


for f in fruits: 
   print(f)
   print(fruits)
#numbered the loop
   for num in range(2) :
      print(num)
      """



"""
fruits = ['banana','pineapple', 'durian','apple']

fruitscopy = fruits.copy
for f in fruits: 
   print(f)
#copies the list
print(fruits)
"""


"""
fruits = ['banana','pineapple', 'durian','apple']

for index, element in enumerate(fruits):
    print(index)
    if element == "apple" :
       fruits.pop(index)
       # removes durian 
"""

"""
fruits = ['banana','pineapple', 'durian','apple']

for index, element in enumerate(fruits):
    if element == "durian" :
       fruits.pop(index)

print(fruits)
# prints ['banana', 'pineapple', 'apple']
"""

"""
fruits = ['banana','pineapple', 'durian','apple']
for index, element in enumerate (fruits):  
   fruits[index] = "nothing" #index copies the value 
print(fruits)
"""

"""
fruits = ['banana','pineapple', 'durian','apple']
for fruitElement in fruits:  
   fruitElement = fruits
print(fruitElement)


  fruitElement = "nothing" | 
  would print nothing,nothing,nothing,nothing
  """
    

"""

print(fruits[0]) 
print(fruits[1])
print(fruits[2])
print(fruits[3])

"""
#control statements
#iterate over number 1 to 9 

for i in range(1,10):
   if i % 3  != 0:
        continue 
else : 
   print(i)

   #stops after 4

   for i in range (1,4):
       if i == 5:
           break
       else:
           print(i)
    

# nested loops
letters = ['a','b', 'c', 'd', 'e']

for i in range (10):
    print(i)

    for j in letters: 
        print(j)


first=["dog","cat","mouse"]
second = ["squirrel", "mouse", "pigeon"]

for a in first: 
    for b in second:
        if (a==b):
            print("matching")