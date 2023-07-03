my_list = ["apple", "", "banana", "", "cherry", "  "]

my_list = [element for element in my_list if element.strip()]

print(my_list)
