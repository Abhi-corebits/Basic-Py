import os     
import time   
import operator
from math import pi
import time

# Function to clear the screen according to OS
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
#Defined Operators using Operator module
oprs = {
 "+": operator.add,
  "-": operator.sub,
  "*": operator.mul,
  "/": operator.truediv,
  "%": operator.mod,
  "^": operator.pow,
  "×": operator.mul,
  "÷": operator.truediv
}
 
#Display the calculator layout 
def display(n1=" ", opr=" ", n2=" ", ans=" "):
	
	print(f"            {n1} {opr} {n2} = {ans}")
	print('''
	   clr  dele    %    ÷
             7    8    9    ×
             4    5    6    -
             1    2    3    +
             ^    0    π    =
	  ''')
	

#First Number 
display()
number1 = input("Enter The 1st Number: ")
if number1== "π":
	number1= round(pi, 2)
elif number1 == "clr" or number1 == "dele":
	print("These Function are not workable right now")
	exit()
else:
	number1 = round(float(number1), 2)	
clear_screen()

#Operator 
display(number1)
operat = input("Choose & Enter The Operator From Calculator: ")
clear_screen()

#Second Number
display(number1, operat )
number2 = input("Enter The 2nd Number: ")
if number2== "π":
	number2= round(pi, 2)
elif number1 == "clr" or number1 == "dele":
	print("These Function are not workable right now")
	exit()
else:
	number2 = round(float(number2), 2)	
clear_screen()

#For asthetics
display(number1, operat, number2)
print("Calculating The Answer.....")
time.sleep(1.5)

#Final Answer Display
if operat in oprs:
	answer = oprs[operat](number1,number2)
	clear_screen()
	display(number1, operat, number2, answer)
	print("Operation is Completed")
else :
	print("Invalid Operator")


