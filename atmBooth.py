def displayAll():
    print('Which one do you want:')
    print('click 1 for withdraw:')
    print('click 2 for deposite amount:')
    print('click 3 for display your account:')
    print('click 4 for break from here:')

def moneyAdd(customer):
    Name=input('Enter your name')
    for i in customer:
        if i['name']==Name:
            while True:
                try:
                    Fname=input('')

customer=[]
def displayItems():
    while True:
        displayAll()
        while True:
            try:
                selectedNumber=int(input('Enter your chooice in integer:'))
            except ValueError:
                print('This in not a number.')
            else:
                break
        if selectedNumber==1:
            moneyAdd(customer)


