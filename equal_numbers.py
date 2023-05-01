def get_count_equal_numbers(number_1, number_2, number_3):
    if number_1 == number_2 == number_3:
        return 3
    elif number_1 == number_2 or number_1 == number_3 or number_2 == number_3:
        return 2
    else:
        return 0


num_1 = int(input('Please enter the first number: '))
num_2 = int(input('Please enter the second number: '))
num_3 = int(input('Please enter the third number: '))

print(get_count_equal_numbers(num_1, num_2, num_3))
