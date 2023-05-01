def get_min_of_3_numbers(number_1, number_2, number_3):
    if number_1 <= number_2 <= number_3:
        return number_1
    elif number_2 <= number_1 <= number_3:
        return number_2
    else:
        return number_3


num_1 = int(input('Please enter the first number: '))
num_2 = int(input('Please enter the second number: '))
num_3 = int(input('Please enter the third number: '))

print(get_min_of_3_numbers(num_1, num_2, num_3))
