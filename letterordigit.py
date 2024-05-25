name=input("enter any digit or letter:::::")
if  name.isalpha():
    print("LETTER")
elif name.isdigit():
    print("DIGIT")
else :
    print("invalid choice")