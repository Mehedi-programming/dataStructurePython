file =open('demo.txt',mode='r')
file1 =open('demo.txt',mode='w')
file2=open('demo.txt',mode='w')
# print(file.read())

# file =open('set.py',mode='r')
# print(file.read())

# print(file.readlines())
# print(file.readline())

print(file.readable())
print(file1.readable())
file2.write('hello world')
file2.write('\nhello kader siddik')
file2.writelines(['\nhello world \nhello mehedi'])
print(file2.writable())

with open('demo.txt','w')as f:
    f.write('')

# import os

# os.remove('demo.txt')
text = '''Lorem ipsum dolor sit, amet consectetur adipisicing elit
Obcaecati, harum, quidem a ullam illo culpa doloribus provident ut quia
error eligendi labore itaque dicta necessitatibus modi non qui deserunt sunt'''

lines = text.splitlines()
print("Total lines:", len(lines))

