def find_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

numbers = [12, 45, 7, 23, 56, 89, 34]
print("Minimum number is:", find_min(numbers))
