numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Square numbers
squared_numbers = [num*num for num in numbers]

print(squared_numbers)

# Print Even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)


# Print common numbers from file1 and file2
number_list1 = []
number_list2 = []
with open("file1.txt") as num_file1:
    numbers = num_file1.readlines()
    for num in numbers:
        number_list1.append(num.strip())

with open("file2.txt") as num_file2:
    numbers = num_file2.readlines()
    for num in numbers:
        number_list2.append(num.strip())

common_num_list = [num for num in number_list1 if num in number_list2]
print(common_num_list)