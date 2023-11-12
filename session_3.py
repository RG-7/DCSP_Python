print("----------------- Session 3 -------------------\n")
    # Task 1: Assignment Operator
print("\t\tTask 1 (Assignment Operator)\n")
number = 25
print("Original number:", number)
number += 5
print("After adding 5:", number)
number //= 3
print("After floor division by 3:", number)
number %= 7
print("After modulus operation by 7:", number)
number *= 4
print("After multiplying by 4:", number)
number ^= 2
print("After bitwise XOR with 2:", number)
number **= 2
print("After exponentiation by 2:", number)


    # Task 2: Replacing using slicing
print("\t\tTask 2 (Replacing using slicing)\n")
my_list = ["apple", "mango", "guava", "cherry"]
print("Original list:", my_list)
my_list[1:2] = ["litchi"]
print("Modified list:", my_list)

    # Task 3: List Methods in Python
print("\n\t\tTask 3 (List Methods in Python)\n")
my_list.append("mango")
print("List after appending 'mango':", my_list)
my_list.reverse()
print("Reversed list:", my_list)
list_length = len(my_list)
print("Length of the list:", list_length)

    #   Task 4 Tuple Methods in Python
print("\n\t\tTask 4 (Tuple Methods in Python)\n")
my_tuple = (1, 2, 3, 2, 4, 2)
count_of_2 = my_tuple.count(2)
print("Count of 2 in the tuple:", count_of_2)
index_of_3 = my_tuple.index(3)
print("Index of 3 in the tuple:", index_of_3)
length = len(my_tuple)
print("Length of the tuple:", length)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)
repeated_tuple = (1, 2) * 3
print("Repeated tuple:", repeated_tuple)

    # Task 5: Order of Operations (PEMDAS)
print("\n\t\tTask 5: Order of Operations (PEMDAS)\n")
result = (3 + 2) * 4
print("Result after parentheses:", result)
result = 2 ** 3
print("Result after exponentiation:", result)
result = 6 * 3 / 2
print("Result after multiplication and division:", result)
result = 5 + 4 - 2
print("Result after addition and subtraction:", result)
result = (5 + 3) * (10 - 4) / 2
print("Result after combining operations with parentheses:", result)
