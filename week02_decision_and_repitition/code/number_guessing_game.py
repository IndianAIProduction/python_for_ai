
# ### 55

# 45
# 70
# 60
# 50
# 55

# attempt 5


import random

print("============== Welcome to the Number Guessing Game ==============")

while True:
    secret_numner = random.randint(0, 100)

    for i in range(0, 5): ## 0,1,2,3,4,,

        print(f"Attempt {i+1} of 5")
        user_guess_num = int(input("Enter the guess number [0-9]: "))
        if user_guess_num == secret_numner:
            print(f"Congratulations! You have guessed the number in {i+1} attempts")
            break

        if user_guess_num > secret_numner:
            print("Too high! Try again.")
        elif user_guess_num < secret_numner:
            print("Too low! Try again.")

        print("--------------------------------")
    
    print("The secret number was: ", secret_numner)

    print("="*50)
    user_input = input("Do you want to play again? (yes/no): ")
    if user_input == "no":
        break
