try:
    age = int(input('age: '))
    print(age)
# valueerror is for conversion
except ValueError:
    print('Invalid Value')


try:
    devision = 100/0
    print(devision)
# valueerror is for conversion
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print('Trying to devide number by 0')
