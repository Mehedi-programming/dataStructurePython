def display():
    print('Hello world.')
display()

def display_name(name):
    print(f'Hello {name} ,how are you?')
display_name('Mehedi')

# default argument

def display_age(name,age=18):
    print(f'hello {name}, I am {age} years old?')

display_age('Mehedi',39)

def keyword(*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)

keyword(212,323,22,11,2,3,45,33)

# keyworded argument

student=[]
def keyworded(**kwargs):
    student.append(kwargs)
    for i ,j in kwargs.items():
        print(i,':',j)
    print(student)
 
id=int(input('Enter your id:'))
name=input('Enter your name:')
age=int(input('Enter your age:'))

keyworded(id=id,name=name,age=age)
