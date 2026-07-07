print("===========Password  Limit  Attempts Program===========")

password = "Python@123=aai"
attemps = 0

while attemps < 3: ### 0 < 3, 1 < 3, 2 < 3, 3 < 3
    user_password = input("Enter your password: ")

    if user_password == password: ## "fsdf" == "Python@123=aai"
        print("Logged in successfully")
        break
    else:
        print("Please enter correct password.")
    attemps += 1 ### 1, 2, 3

if attemps == 3: ## 3 == 3 >>>> True
    print("Account locked")