#----------------------- Task 9 -----------------------------
from typing import Any


print("\n----------------------- Task 9 -----------------------------\n")

# Q_1 "Decorators in python"

def decoratorFun(func):
    def bihar():
        print("Welcome to Bihar <3")
        func()
        print("Thanks for visiting! Visit us again........</3 </3 </3")
    return bihar

@decoratorFun
def patna():
    print("Patna is the capital of Bihar. And you are crossing Patna......!!!")

patna()

#   Q_2 More Dunder methods

class Number:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __call__(self):
        return self.x + self.y != 0
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"{self.x}, {self.y}"

print("-- Call Method --")
num2 = Number(2, 3)
num3 = Number(2,-2)
print(f"Number num2({num2}) is non-zero : {num2()}")
print(f"Number num3({num3}) is non-zero : {num3()}")

print("-- Equal Method --")
check1 = Number(1, 2)
check2 = Number(1, 2)
check3 = Number(3, 2)
print(f"Check1({check1}) and Check2({check2}) are equal : {check1==check2}")
print(f"Check1({check1}) and Check3({check3}) are equal : {check1==check3}")
