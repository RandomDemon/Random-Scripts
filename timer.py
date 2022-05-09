import time

n = int(input("How long would you like to wait?"))
n-=1
while n > 0:
    print(n)
    n-=1
    time.sleep(1)
