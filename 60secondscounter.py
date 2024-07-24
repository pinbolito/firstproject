import time
x = 60
y = input()
if y == "start":
    while x > 0:
        x = x - 1
        print(x)
        time.sleep(1)
    else:
        print("end")
