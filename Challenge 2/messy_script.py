def calculate_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

numbers = [1, 2, 3, 4, 5]
print("Sum:", calculate_sum(numbers))
