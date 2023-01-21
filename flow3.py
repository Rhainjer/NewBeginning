number=-999999
numb=int(input("Enter your number: "))
while numb!=-1:
    if numb>number:
        number=numb
    numb=int(input("Enter number"))
if number==-1:
    print("You have not entered any number")
else:
    print(number)