numbers = [10, 20, 30, 40, 50, 30]

if 30 in numbers:
    index = numbers.index(30)
    numbers[index] = 500

print(numbers)
