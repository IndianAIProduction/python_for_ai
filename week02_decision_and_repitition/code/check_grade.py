print("====================Check Grade Program====================")
print("Enter valid input number from [0 - 100] or enter character only 'A' ")

marks = input("Enter your marks to get Grade : ")

if marks == "A": 
    print("Student was absent")
elif marks >= str(90): 
    print("Grade A")
elif (marks >= str(70)) and (marks< str(90)): 
    print("Grade B")
elif (marks >= str(50)) and (marks< str(70)): 
    print("Grade C")
elif marks < str(50):
    print("Grade D")
    print("Failed")


print("============Thank you for using Check Grade Program============")