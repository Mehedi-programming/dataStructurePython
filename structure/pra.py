def add(a,b):
    result=(a+b)
    print(result)
    # return a + b
def hello():
    while True:
        try:
            hello=int(input('enter two number:'))
            hello1=int(input('enter two number:'))
            add(hello,hello1)
        except ValueError:
            print("string and integer cannot be added.")
        else:
            print('your number are correct value.')
            break
hello()

print('hekeld\n')
print('heke323423ld')