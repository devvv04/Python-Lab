# check wether a number is negative , positive or zero
num = int(input("Enter your number: "))
if(num >0):
    print("Number is positive")
elif(num < 0):
    print("Number is negative")
elif(num ==0):
    print("Number is zero")
else:
    print("Number is invalid")