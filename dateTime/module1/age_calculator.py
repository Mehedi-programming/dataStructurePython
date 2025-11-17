import datetime
value=datetime.datetime.now()

while True:
    try:
        ageInput=int(input('Please enter your birthyear:'))
    except ValueError:
        print('Invalid date. Please enter a valid numeric date:')
    else:
        break

Age=value.year-ageInput
print(f'your current age is {Age}')

