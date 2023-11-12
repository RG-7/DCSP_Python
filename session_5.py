#----------------------- Task 5 -----------------------------
print("\n----------------------- Task 5 -----------------------------\n")

# Q_1
#   1
#   2 2
#   3 3 3
#   4 4 4 4
#   5 5 5 5 5
print("\t--- Q_1 Pattern Printing ---")
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()

#   Q_2
#   Fibonacci Series using python loop
print("\n\t--- Q_2 Fibonacci Series ---")
n=int(input("Enter the range of series : "))
fibonacci_series = []
a,b=0,1
for _ in range(n):
    fibonacci_series.append(a)
    a,b=b,a+b
print("Fibonacci Series for "+str(n)+" is ")
for i in fibonacci_series:
    print(i,end=" ")

#   Q_3
print("\n\t--- Q_3 Fruit available in shop? ---")
fruit_shop = {
    "apple": 120.0,
    "banana": 50.5,
    "orange": 123.2,
    "grape": 235.5,
    "mango": 250.0
}
fruit_name = input("Enter the name of the fruit: ").lower() 
if fruit_name in fruit_shop:
    price = fruit_shop[fruit_name]
    print(fruit_name," costs Rs. "+str(price))
else:
    print(fruit_name," is not available in the shop.")
