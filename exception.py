    
# # else:
# #     ...
# # finally:
# #     ...

# # try:
# #     file=open('demo1.txt','r')
# #     print(file.read())
    
# # except Exception as e:
# #     print(repr(e))

# # # ZeroDivisionError  
# # try:
# #     x = 10 / 0
# # except ZeroDivisionError:
# #     print("You can't divide by zero.")

# # # ValueError
# while True:
#     try:
#         num=int(input('Enter a number:'))
#         result=10/num
#     except ValueError:
#         print('please enter a valid number.')
#     except ZeroDivisionError:
#         print('You can\'t divide by zero')
#     else:
#         print(result)
#         print('this is a correct number.')
#         break

# try:
#     num=int(input('Enter a number:'))
#     result=10/num
# except (ValueError, ZeroDivisionError) as e:
#     print("Error occurred:", e)
# else:
#     print('this is a correct number.')

# # rase valueError

# age = -5
# if age < 0:
#     raise ValueError("Age cannot be negative.")
# try:
#     file = open("demo1.txt", "r")
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found.")
# finally:
#     try:
#         file.close()
#     except:
#         pass


# def multiply(x, y):
#     return x * y

# print(multiply("Hi", 3))
# # print(multiply("Hi", "3"))


# TypeError
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
# IndexError
try:
    item=['apple']
    print(item[5])
except IndexError:
    print('In this list there is no index 5')

# # FileNotFoundError

try:
    file=open('demo1.txt','r')
    print(file.read())
    
except FileNotFoundError:
    print('file not found')

# # PermissionError
try:
    file=open("demo1.txt", "r")
    print(file.read())
except FileNotFoundError:
    print('this file is not found in this directory')
except PermissionError:
    print("there has no permission to read this file.")

# # NameError
name2='hah'
try:
    print(name)
except NameError:
    print('name is not defined.')

# # AssertionError
def sqr(x):
    return x*x
try:
    assert sqr(4)==16
    assert sqr(5)==25
    print('this is a valid square number.')
except AssertionError:
    print('this is not a valid square number.')