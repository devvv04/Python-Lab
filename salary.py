# male got 5% bonus , female got 10% bonus, if salary less then 10000, extra 2%.
gender = input("Enter your gender (Male/Female): ")
salary = int(input("Enter your salary: "))

if(gender == "Male"):
    final = salary + (salary * 0.05)
elif(gender == "Female"):
    final = salary + (salary * 0.1)
# else:
#     print("Invalid input")
#     exit()

if(salary < 10000):
    final = final + (salary * 0.02)
   
print("Final salary after bonus is",final)