name='haj'
age=29
print(f"My name is {name}")
print("My name is", name)
print("{name} has age {age}") # here python will think that here name and also age is a plain text

print(f'{name} has age {age}') 

def interest(p,n,q):
    si=(p*q*n)/100
    return si

s1= interest(20,33,32)
print (s1)

print("-"*50)

def interest(p,n,q):
    si=(p*q*n)/100
    Si=(p-q*n)/100
    return si,Si # it will be a tuple
    return Si # here it won't return the value of Si 
    


 
# s2= interest(20,33)
print (interest(20,33,32))
# print (s2)

def interest(p,n,q): # this interest is global identifire
    si=(p*q*n)/100 # si is a ocal vaiable
    return si
    def interest2(b): # this interest is local identifire
        pass


s1= interest(20,33,32)
print (s1)
print('-'*20)
num=10
def display():
    num=20
    # return num
    print(f'inside {num}')

display()
print(f'outside {num}')

print('-'*20)
num=10
def display():
    num=num+35  # local variable
    num=20
    # return num

    print(f'inside {num}')

display()
print(f'outside {num}')


print('-'*20)
num=10
def display():
    global num
    num=num+35  # local variable
    # num=20
    # return num

    print(f'inside {num}')

display()
print(f'outside {num}')

def simple_interest(p,q,r):
    si=(p*q*r)/100
    print(f'simple interest {si}')
    return si
    # print('hello world')

si=simple_interest(1000,12,332)
total=si+10000
print(total)

def display():
    # return 'hasina'
    # return 102
    return [10,23,12.23,'jfdj']

print(display())

def cal(p,q):
    add=p+q
    sub=p-q
    return add,sub  # here it will return a tuple

n1,n2=cal(20,40)
print(f'addition: {n1}')
print(f'subtraction: {n2}')
s1=cal(20,40)
print(s1)


def cal(p,q):
    if p<0:
        return 0   # here if p is less than 0 then it will return and print (None)
    add=p+q
    sub=p-q
    return add,sub  # here it will return a tuple

print(cal(-10,20))

def display():
    pass
print(type(display))
print(display)  # it will print the memory location of display function

def display():
    print("hello world")

vaiable=display
vaiable()
display()

def display():
    print("hello world 1")
    def display():
        print("hello world 2")
        def display():
            print("hello world 3")
            def display():
                 print("hello world 4")
            display()
        display()
    display()
                
display() 

# def display(name=None,Name):
#     print(f"name is {name} Name is {Name}")

# display('hasan','abdul')
# it will print an error because in function there first parameter can't be None

def display(Name, name=None):
    print(f"name is {name} Name is {Name}")

display('hasan', 'abdul')





