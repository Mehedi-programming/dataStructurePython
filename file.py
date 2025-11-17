# # file =open('demo.txt',mode='r')
# # file1 =open('demo.txt',mode='w')
# # file2=open('demo.txt',mode='w')
# # print(file.read())

# # file =open('set.py',mode='r')
# # print(file.read())

# # print(file.readlines())
# # print(file.readline())

with open('demo.txt','w')as f:
    c = f.write('hello hani pani o you.\n')
    d=f.write("'email':'mehedi@gmail.com\n'")
    d=f.write('hdjfdj')
    print("count : ",c)

with open("demo.txt", "r") as file:
    content = file.read()
    print(content)


# file = open("example.txt", "w")
# content = file.write('jsdjsdssd')
# # print(content) 
# # file.close() 
# file = open("example.txt", "r")
# content = file.read()
# print(content)
# # file.close()  


# # print(file.readable())
# # print(file1.readable())
# # file2.write('hello world')
# # file2.write('\nhello kader siddik')
# # file2.writelines(['\nhello world \nhello mehedi'])
# # print(file2.writable())


# # import os

# os.remove('demo.txt')
# text = '''Lorem ipsum dolor sit, amet consectetur adipisicing elit
# Obcaecati, harum, quidem a ullam illo culpa doloribus provident ut quia
# error eligendi labore itaque dicta necessitatibus modi non qui deserunt sunt'''

# lines = text.splitlines()
# print("Total lines:", len(lines))

# print(__name__)
# import practice
# def greet():
#     print("helo i'm from file")
#     print("helo gelo i'm from file")

# if __name__ == "__main__":
#     greet()
# else:
#     print('this is not a main module for practice directory.')
