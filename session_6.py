#----------------------- Task 6 -----------------------------
print("\n----------------------- Task 6 -----------------------------\n")

#   Q_1
print("\n\t--- Q_1 ---")
#   Calc using normal & Lambda Function
print("-- Normal Function --")
def sum_a_b(a,b):
    return a+b
def diff_a_b(a,b):
    return a-b
def mul_a_b(a,b):
    return a*b
def div_a_b(a,b):
    return a/b
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
#   Sum
sum_ab = sum_a_b(a,b)
print("Sum of "+str(a)+" & "+str(b)+" is "+str(sum_ab))
#   Diff
diff_ab = diff_a_b(a,b)
print("Difference of "+str(a)+" & "+str(b)+" is "+str(diff_ab))
#   Mul
mul_ab = mul_a_b(a,b)
print("Product of "+str(a)+" & "+str(b)+" is "+str(mul_ab))
#   Div
div_ab = div_a_b(a,b)
print("Divide of "+str(a)+" & "+str(b)+" is "+str(div_ab))

print("-- Lamda Function --")
add = lambda x, y: x + y
diff = lambda x,y:x-y
mul = lambda x,y:x*y
div = lambda x,y:x/y
print("Sum of "+str(a)+" & "+str(b)+" is "+str(add(a, b)))
print("Difference of "+str(a)+" & "+str(b)+" is "+str(diff(a, b)))
print("Product of "+str(a)+" & "+str(b)+" is "+str(mul(a,b)))
print("Divide of "+str(a)+" & "+str(b)+" is "+str(div(a,b)))

#   Q_2
print("\n\t--- Q_2 ---")
#   *args & **kwargs
print("-- *args --")
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)  # Prints 1, 2, 3
print_args('apple', 'banana', 'cherry') 

print("-- **kwargs --")
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name='Alice', age=30, city='New York')
