"""

Project 1 — Room Area Calculator
EN: Write a function room_area(length, width) that returns the area of a room. Use it to find the area of 3 different rooms and print each result.
हिंदी: एक function room_area(length, width) बनाओ जो कमरे का area return करे। इसे 3 अलग-अलग कमरों का area निकालने के लिए इस्तेमाल करो और हर result print करो।
Concepts: def, two parameters, return, function call
Hint: return length * width. Print the call: print(room_area(10, 12)).
"""

### Step1: restate> calcualte the area of room using user input length and width
### Step2: example> length = 10, width = 12 >> area = 120
### Step3: Pseudocode> Take length and width as input from user
            # call the function room_area(length, width) >> return length * width
            # print the result

### Step4 >> Translate to python code
### Step5 >> Trace (dry run)

def room_area(length, width):
    return length * width

length = int(input("Enter the length of the room: "))
width = int(input("Enter the width of the room: "))
print("The area of the room is: ", room_area(length, width))



"""
Enter the length of the room: 10
Enter the width of the room: 20
The area of the room is: 200
"""