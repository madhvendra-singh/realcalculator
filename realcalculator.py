import time
print("Write Your First Number")
cal1 = input()
print("Write Your Second Number")
cal2 = input()
print("Write add,sub,multi,div")
cal3 = input()
if cal3 == "add":
    print(int(cal1) + int(cal2))
elif cal3 == "sub":
    print(int(cal1) - int(cal2))
elif cal3 == "multi":
    print(int(cal1) * int(cal2))
else:
    print(int(cal1) / int(cal2))
time.sleep(5)