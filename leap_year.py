def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 'YES'
    else:
        return 'NO'


print(is_leap_year(int(input('Please enter the year: '))))
