# wap to calc income after deducting the tax basis of following conditions: c 1: 
sal = int(input("Enter your salary: "))
if(0<sal < 150000):
    tax = 0
elif(150000<sal<300000 ):
    tax = sal * 0.1
elif(300000<sal<500000):
    tax = sal * 0.2
elif(sal>500000):
    tax = sal * 0.3
else:
    print("Salary cannot be negative")
final_sal = sal - tax
print("Salary after tax deduction is: ",final_sal)