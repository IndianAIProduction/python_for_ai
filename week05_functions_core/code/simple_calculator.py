## Step 1 >> restate : create simple calculator for +, -, *, /
## Step 2 >> example : 7+9 >> 16
## step 3 >> Pseudocode :
            # Take 2 number input fromuser
            # take any one operator as input ( +, -, *, /)
            # call respective function according to user input oprator
            # give final result to the user
## step 4 >> Traslate to python code
## step 5 >> Trace (dry run)
#

def add(num1, num2): ## num1 = 9, num2 = 4
    return num1 + num2 ##  9 + 4 >> 13

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

print("========== Welcome to simple calculator ==========")

while True:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    if operator == "+": ## "+"" == "+" >> True
        print("Addition of 2 numbers is: ", add(number1, number2)) ## add(9,4) >> 13

    elif operator == "-":
        print("Subtraction of 2 numbers is: ", sub(number1, number2))

    elif operator == "*":
        print("Multiplication of 2 numbers is: ", mul(number1, number2))

    elif operator == "/":
        print("Division of 2 numbers is: ", div(number1, number2))

    else:
        print("Invalid operator")
    
    print("------------------------------------------------")
    want_to_continue = input("Do you want to continue? (y/n): ")
    if want_to_continue == "n":
        break
    print("================================================")


#========== Welcome to simple calculator ==========
#Enter the first number: 9
#Enter the second number: 4
#Enter the operator (+, -, *, /): +
#Addition of 2 numbers is: 13
