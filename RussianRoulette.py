import random
import time

bullet = float(random.randint(1,6))

while True:
    shot = float(input("Enter a number from 1-6"))
    print("You are...")
    time.sleep(1)
    if bullet == shot:
     print("Dead!")
     time.sleep(1)
     break
    else:
      print("Alive!")
