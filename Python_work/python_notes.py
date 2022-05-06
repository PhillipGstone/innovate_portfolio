# Data types 
# string, 

# conditional operators

# # Casting
print (int(5.4))
print (int("54")) 
print (float(54)) 
print (str(5.4)) 
print (type(str(5.4))) 

print("what is your name?")
name = input()

if name:  # not compering it to anything so as long as you type something it true.
    print(f"Hello {name}") # put in anything it's true so prints this.
else:
    print("you did not provide a name") # if u don't type anything it's false and prints this.

# == EQUAL
# != not EQUAL
# >= greater then or equal to.  > Greater then.
# <= less then or equal to.   < less then.

print(not True) 
print(not False)

bool = False
if bool != True:
    print(False)
else:
    print(True)

bool = False
if not bool:
    print(False)
else:
    print(True)

def add_up():
    num1 = input("add up 1st number \n")
    num2 = input("add up 2nd number \n")
    print(num1 + num2)  # this adds strings to strings so you'll get 510 from 5 and 10 not 15.

add_up() 

def add_up():
    num1 = input("add up 1st number \n") # This will ask u all these first and if there an errer even with one it'll just un the except.
    num2 = input("add up 2nd number \n")
    try:   # if u want to catch the errer as soon as it happens put the inputs into the try:
        print(f"{num1} + {num2} is {int(num1) + int(num2)}")  
    except: # handles any error even keybord kill. use. except  ValueError: to fix that.
        print("Error! Please type a number")
        print("****************")
        add_up()

add_up() 

light = False

def light_switch():
    global light # make the verable global. Turn the local to a global.
    if light:
        print("Whoa! it's bright in here")
        light = False
    else:
        print("who turned out the lights?")
        light = True

light_switch()
light_switch()

balance = 100

def cash_withdraw(amount):
    global balance
    print(f"your balance is {balance}")
    print(f"you are withdrawing {amount}")
    balance -=amount
    print(f"your new balance is {balance}")

cash_withdraw(int(input("amount ")))


list1 = [1, 2, 3] # can be changed.

tuple1 = (1, 2, 3) # can't be changed.
# tuple good when u have stuff u don't want to change.
even_nums = [2, 4, 6, 8, 10]
odd_nums = (1, 3, 5, 7, 9)

even_nums.append(12)
even_nums.insert(0, 0)

for i in even_nums:
    print (i) 

odd_nums.remove(1) # won't work coz it a tuple.
odd_nums.pop()

odd_nums = odd_nums + (11, 13, 15) # add onto a tuple.

list_of_fruit = ["apples", "bananas", "oranges", "pears", "grapes", "pineapples", "star_fruit", "mango", "cherries", "black-berries"]

num = 0
while num < 10:
    print(num)
    num += 1

