# Task 1: -  Python Built in Methods :-
print("\n------------ Task 1 ------------\n")
    #   .maketrans or .translate it translate or replace we can say
trans = "This is Taj Mahal"
translation_table = str.maketrans("aeiou", "12345")
trans_string = trans.translate(translation_table)
print(trans+" --> "+trans_string)
    #   symmetric_difference() 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)  # Outputs: {1, 2, 5, 6}


# Task 2:- Python escape characters
print("\n------------ Task 2 ------------\n")
    #   \ooo it replaces decimal values to octal value
my_name = "I am R\141tn Govind\141m" # 141 is decimal value of a
print(my_name)
    #   \xhh it replaces the sequence to hexadecimal code
about = "I \x61m \x61 Student" # \x61 --> a
print(about)
    #   \b is for backspace
back_space = "Ratn \bGovindam"
print(back_space)
    #   \t used for tab of space eof 4 char
tab = "Ratn\tGovindam"
print(tab)
    #   \v used for vertical tab
v_tab = "R\vG"
print(v_tab)


# Task 3:- Examples of User Input
print("\n------------ Task 3 ------------\n")
    #   Basic Input
user_input = input("Enter something: ")
print("You entered:", user_input)

    #   Multiple Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello,", name, "! You are", age, "years old.")
