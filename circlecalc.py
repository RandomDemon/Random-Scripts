import time
import math

def area(pi, radious):
    return pi * radious ** 2
def circumference(pi, radious):
    return 2*pi*radious

print("Select operation.")
print("1.Area")
print("2.Circumference")

while True:
    choice = input("Enter choice(1)/(2): ")

    if choice in ('1', '2'):
        pi = float(input("Enter what you would like to use for pi: "))
        radious = float(input("Enter the radious: "))

        if choice == '1':
            print(pi, "*", radious, "^", "2", "=", area(pi, radious))

        elif choice == '2':
            print(2, "*", pi, "*", radious, "=", circumference(pi, radious))
        
        next_calculation = input("Let's do another calculation? (yes/no): ")
        if next_calculation == "no":
            print("Just run me again when you want to use me!")
            print("Good bye!")
            time.sleep(3)
            break
    
    else:
        print("Invalid Input")
        