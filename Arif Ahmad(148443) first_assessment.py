#1.Write function to take input from user in days and print
#it in years,month and days

number_of_days = int(input("Enter number of days: "))
years = number_of_days // 365
months = (number_of_days - years *365) // 30
days = (number_of_days - years * 365 - months*30)
print(years,"years,",months,"months,",days,"days")

#2.Generate- fibnoacci series from 1 to 20.

num = 20
n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")
while count < num:
           print(n1)
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1

#3.Create a program to play rps game.
import random

player1 = input("Select Rock, Paper, or Scissor :")
player2 = random.choice(["Rock", "Paper", "Scissor"])
print("Player 2 selected: ", player2)

if player1 == "rock" and player2 == "paper":
    print("Player 2 Won")
elif player1 == "paper" and player2 == "scissor":
    print("Player 2 Won")
elif player1 == "scissor" and player2 == "rock":
    print("Player 2 Won")
elif player1 == player2:
    print("Tie")
else:
    print("Player 1 Won")
    
#4.Write function to calculate and display grosssalary and netsalary of an employee after getting
#input as basicsalary write separate function for allowance and deduction to calculate them respectivly.

gvn_basc_sal = int(input("Please Enter Basic salary"))
gvn_da = (float)(18 * gvn_basc_sal) / 100.0
gvn_hra = (float)(22 * gvn_basc_sal) / 100.0
gvn_ta = (float)(10 * gvn_basc_sal) / 100.0

gvn_pf=(float)(12 * gvn_basc_sal) / 100.0
gvn_insurance=(float)(8 * gvn_basc_sal) / 100.0
if gvn_basc_sal >8000:
    gvn_proftax=200
else:
    gvn_proftax=150  
allowances=gvn_da + gvn_hra + gvn_ta
deduction=gvn_pf+gvn_insurance+gvn_proftax
gros_sal = gvn_basc_sal + allowances
net_sal=gros_sal-deduction
print("The Employee's Net salary from the given basic salary ", net_sal)

#5.calculate the number of vowel individually and calculate the number of consonants without considering
#punctuation character
ip_str = '''python is widely used general purpose, high level programming language it was created by guido van rossum in 1991 and further
developed by python software foundation'''
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvexz'
ip_str = ip_str.casefold()
count = {}.fromkeys(vowels,0)
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)

vowels=0
consonants=0
for i in ip_str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1;
    else:
        consonants=consonants+1;

print("\nThe number of consonant:",consonants);

#6.Ask user a input string and check if the entered string is palindrome

def isPalindrome(s):
	return s == s[::-1]

s = input("enter the string to check whether string is palindrome or not")
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")


#7.Ask user a input email and check if the email is valid form or not

import re

def solve(s):
   pat = "^[a-z]+@[a-z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False

s = input("please enter the email address")
print(solve(s))
#9.create a shopping cart for the below bakery items.
#bakery_items={"bread":40,"butter":120,"jam":200,"cheese":220,"crossiant":60)

bakery_items={"bread":40,"butter":120,"jam":200,"cheese":220,"crossiant":60}
cart_items = []
price_items = []

print("Welcome to the Shopping Cart Program!")
print()

def menu():

        print("1. View the bakery items")
        print("2. add the item into the cart")
        print("3. view the cart")
        print("4. update item in cart")
        #print("5. remove item from cart")
        #print("6. checkout and generate bill")

def display_content():
    print(cart_items[0], price_items[0])
for i in range(0, len(cart_items)):
        print(f"{cart_items[i]} - {price_items[i]}")

menu()
option = int(input("Please, enter an action: "))

while option != 7:
    if option == 1:
        print("View available item in Bakery.",bakery_items.keys())
    elif option == 2:   
        new_item = input("What item would you like to add? ")
        price_item = float(input(f"What is the price of the {new_item}? "))
        print(f"{new_item} has been added to the cart.")
        cart_items.append(new_item)
        price_items.append(price_item)
    elif option == 3:
        print("View the cart.",cart_items)
    elif option == 4:
        new_item=input("What item would you like to update ")
        price_item = float(input(f"What is the price of the {new_item}? "))
        print("updated item in the cart.")
    '''elif option == 5:
        
        cart_items.remove()
    elif option == 6:
        for i in range(len(cart_items)):
            items = cart_items
            print("")
            
    '''
else:
        print("Invalid option, please, try again.")

print()
menu()
option = int(input("Please, enter an action: "))

print("Thank you!")



