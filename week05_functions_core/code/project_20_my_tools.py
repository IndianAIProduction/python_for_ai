"""
Project 20 — Build Your First Tools Library (capstone)
EN: Create a file my_tools.py with 4 reusable functions, each returning a value: celsius_to_f(c), bmi(weight, height), is_prime(n), and word_count(text). Test all four and print the results. This is the seed of your own "AI tools" library!
हिंदी: एक file my_tools.py बनाओ जिसमें 4 reusable functions हों, हर एक value return करे: celsius_to_f(c), bmi(weight, height), is_prime(n), और word_count(text)। चारों को test करके results print करो। यह आपकी अपनी "AI tools" library की शुरुआत है!
Concepts: multiple functions, return, loops/flags inside functions, .split()
Hint: For is_prime, use a flag: assume prime, loop 2..n-1, if any divides evenly set flag False. For word_count, return len(text.split()).
"""


def celsius_to_f(c):
    return (c * 1.8) + 32

def bmi(weight_kg, height_m):
    return weight_kg/(height_m**2)

def is_prime(n):
    if n < 2:
        return False

    prime = True
    for i in range(2, n-1):
        if n%i == 0:
            prime=False
            break
    return prime

def word_count(text):
    return len(text.split())


print("The temperature in Fahrenheit is: ", celsius_to_f(36.9))

print("The BMI is: ", bmi(70, 1.75))

print("Is 17 a prime number? ", is_prime(17))

print("The word count is: ", word_count("Hello, how are you?"))