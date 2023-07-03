numbers = input("Enter a list of numbers separated by spaces: ").split()

index = int(input("Enter an index to add the value at: "))

value = input("Enter a value to add: ")

numbers.insert(index, value)

print("Updated list of numbers:", numbers)
