def max_numbers(numbers):
    max =numbers[0]
    for number in numbers:
        if number > max:
            max=number
    return max
