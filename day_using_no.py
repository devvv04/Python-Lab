# wap to take input 1-7 and print the corresponding week name
n = int(input("Enter number between 1-7: "))
match n:
    case 1: 
        print("Monday")
    case 2:
        print("Tuesday")
    case 3: 
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5: 
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
