emails = ['rafi@gmail.com','karim@gmail.com','sharif@gamil.com']

emailInput=input('Enter an email:')

# if iema==emailInput:
#     print('this email is already exist.')
#     # break
#     else:
#         print('congrates, your email is unique.')

if emailInput not in emails:
    print('This is a new email.')
else:
    print('This input is alredy exist.')