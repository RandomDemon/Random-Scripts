import random
import time

bullet = random.randint(1,6)
shot = random.randint(1,6)
ready = True

if ready == True:
    print("The bullet is in slot...")
    print(bullet)
    time.sleep(2)
    print("You are...")
    time.sleep(1)
if bullet == shot:
    print("Dead!")
    time.sleep(5)
else:
    print("Alive!")
    time.sleep(5)