#----------------------- Task 4 -----------------------------
print("\n----------------------- Task 4 -----------------------------\n")

#   Q_1
print("\t1. Methods of sets.....")

print("\n---Symmetric Difference Update-----")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Sets before applying symetrric difference update :- ")
print("Set 1 ="+str(set1))
print("Set 2 ="+str(set2))
set1.symmetric_difference_update(set2)
# set1 now contains {1, 2, 4, 5}
print("Set 1 after applying symmetric difference update is :- "+str(set1))

print("\n---Is Subset-----")
# Define two sets
set_1 = {1, 2, 3, 4, 5}
set_2 = {2, 3, 4}
print("Set 1.1 ="+str(set_1))
print("Set 2.1 ="+str(set_2))
# Check if set2 is a subset of set1
is_subset = set_2.issubset(set_1)
# Output
print("Is Set 2.1 a subset of Set 1.1 ? "+str(is_subset))  # True, because set2 is a subset of set1

print("\n---Is Superset-----")
# Define two sets
set11 = {1, 2, 3, 4, 5}
set22 = {2, 3, 4}
print("Set 1.1 ="+str(set11))
print("Set 2.1 ="+str(set22))
# Check if set1 is a superset of set2
is_superset = set11.issuperset(set22)
# Output
print("Is Set 1.1 a superset of Set 2.1 ? "+str(is_superset))  # True, because set1 is a superset of set2

#   Q_2
print("\n\t2. Methods of Dictonary.....")

print("\n-----fromkeys(keys, value)-------")
keys = ["a", "b", "c"]
print("keys:- "+str(keys))
default_value = 99
print("default Values = "+str(default_value))
new_dict = dict.fromkeys(keys, default_value)
print("Dictonary Consists :- "+str(new_dict))
# Resulting dictionary: {"a": 99, "b": 99, "c": 99}

print("\n-----setdefault(key, default)--------")
my_dict = {"a": 1, "b": 2}
print("Dictonary Consists :- "+str(my_dict))
value = my_dict.setdefault("c", 3)
print("value = "+str(value))
print("Updated Dictonary Consists :- "+str(my_dict))
# Resulting dictionary: {"a": 1, "b": 2, "c": 3}

#   Q_3
print("\n\t3. Voting Age Calc.....")

print("\n-----MultiLine Code-------")
age = int(input("Enter your age: "))
#   Multiline code
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
#   Single Line Code
print("\n-----SingleLine Code-------")
print("You are eligible to vote.") if int(input("Enter your age: ")) >= 18 else print("You are not eligible to vote.")

#   Q_4
print("\n\t4. Fruit is in list ?")
# Create a list of fruit names
fruits = ["apple", "banana", "cherry", "date", "litchi", "papaya", "grape"]

# Take user input for a fruit name
user_input = input("Enter a fruit name: ")

# Check if the user input is in the list of fruit names
if user_input in fruits:
    print("It is in the list of fruits.")
else:
    print("It is not in the list of fruits.")


