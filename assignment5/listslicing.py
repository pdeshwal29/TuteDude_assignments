import re

numbers = list(range(1, 11))

numbers_str = " ".join(map(str, numbers))
first_five = re.findall(r'\b[1-5]\b', numbers_str)

first_five = list(map(int, first_five))

reversed_list = first_five[::-1]

print("Original list:", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_list)