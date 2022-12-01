fN = int(input("Enter Your first number:- "))
Function = str(input("Enter the sum (+,-,/,*):- "))
sN = int(input("Enter the second number:- "))

if Function == "+":
    output = fN + sN
if Function == "-":
    output = fN - sN
if Function == "*":
    output = fN * sN
if Function == "/":
    output = fN / sN

print("Answer is :",output)

