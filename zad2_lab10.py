import time

i = 0
x = 1

while i < 30:
    print(i)
    i = i + 1
    x = x - 0.03
    time.sleep(x)
