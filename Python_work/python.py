# from lib2to3.pgen2.token import EQUAL
# import random as r

# print(r.random())
# print(r.uniform(1,10))
# print(r.randint(1,10))

# print(1+2)
# print(1-2)
# print(2*3)
# print(3**3)
# print(15/3)
# print(15%3)

# balance = 100
# amount = 50

# print(balance-amount)

# == EQUAL
# != not EQUAL
# >= greater then or equal to.  > Greater then.
# <= less then or equal to.   < less then.

# music = "classical"

# if music == "classical":
#     print("oh no it's classical")
# elif music == "pop":
#     print("turn it up")
# else:
#     print("yay")

# def add_up(num1, num2):
#     num1+num2

# add_up(5, 2) 

# def add_up(num1, num2):
#     return num1+num2

# print (add_up(5, 2)) 

# coffee_order = [
#     "alex - cortado. "
#     "ben - latte. "
#     "sam - black. "
# ]
# print(coffee_order)

# coffee_order.append("fred - anything")
# print(coffee_order)

# coffee_order.pop(1)
# print(coffee_order)

# for i in range(10):
#     print(i, "yum that's great coffee")

# for i in range(1, 10, 1):
#     print(i, "yum that's great coffee")


# Welcome = "Welcome to Code Nation"

# print(len(Welcome))


# alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# for i in alphabet:
#     print (i)

# numhere = input("Put number here! ")
# numhere = int(numhere)
# numhere -=1
# print(f"the letter to your number is,") 
# print(alphabet[numhere]) 


first_move = input("What space? 1-9 ")

if first_move == "1":
    space1 = input("X or O  ").upper()
elif first_move == "2":
    space2 = input("X or O  ").upper()
elif first_move == "3":
    space3 = input("X or O  ").upper()
elif first_move == "4":
    space4 = input("X or O  ").upper()
elif first_move == "5":
    space5 = input("X or O  ").upper()
elif first_move == "6":
    space6 = input("X or O  ").upper()
elif first_move == "7":
    space7 = input("X or O  ").upper()
elif first_move == "8":
    space8 = input("X or O  ").upper()
elif first_move == "9":
    space9 = input("X or O  ").upper()
else:
    pass


print(f"""---------------------
   {space1}   |   {space2}   |   {space3}  
---------------------
   {space4}   |   {space5}   |   {space6}  
---------------------
   {space7}   |   {space8}   |   {space9}  
---------------------
""")



# space1 = "1"
# space2 = "2"
# space3 = "3"
# space4 = "4"
# space5 = "5"
# space6 = "6"
# space7 = "7"
# space8 = "8"
# space9 = "9"