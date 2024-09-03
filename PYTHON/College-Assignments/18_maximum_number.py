def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers = [12, 45, 7, 23, 56, 89, 34]
print("Maximum number is:", find_max(numbers))
