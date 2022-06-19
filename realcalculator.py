import time
print("Write Your First Number")
cal1 = int(input())
print("Write Your Second Number")
cal2 = int(input())
print("Enter +,-,*,/ : ")
cal3 = input()
if cal3 == "+":
    print(cal1+cal2)
elif cal3 == "-":
    print(cal1-cal2)
elif cal3 == "*":
    print(cal1*cal2)
elif cal3 == "/":
    print(cal1/cal2)
else:
    print("You have not entered any recognizable input")
time.sleep(5)
