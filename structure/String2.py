'''Number1=int(input("Enter a number:"))
Number2=int(input("Enter a number:"))
Sum=' Number1+Number2
print("The sum is:",Sum)
print(type(Sum))+
 
print(len(Sum))'''
s='''Lorem ipsum dolor sit, amet consectetur adipisicing elit. Obcaecati, harum, quidem a ullam illo
culpadoloribus provident ut quia error eligendi labore itaque dicta necessitatibus modi non qui deserunt sunt.'''
p=s.splitlines()
print(len(p))
#string:
a="mehedi's name is hasan"
print(a)
a="mehedi hasan'mozumder'"
var='This is a mehedi\'s phone'
print(var)
print(a)
print(type(a))
b="""mehedi
hasan
mozumder"""
print(b)
b=1,2,3,4,5,6,7
print(b[-4:3])
print(b[::-1])
print(b)
print(b[0:16:3])
print(b[0:12:3])
print(b[::3])
print(b[1::3])
print(b[:7:3])
print(b[20:0:-1])
print(b[::-1])
print(b[3])
print(b[2])
print(b[-5])
b='mozumder'
print(b[-8])
b='calculus'
print(b[3:])
print(b[2:4])
print(b[:3])
#in string we cannot change any index but there has a logic like:
s='multiline'
s=s[:3]+'d'+s[4:]
print(s)
a='bashundhara'
a=a[:5]+'a'+a[5:]
print(a)
a='bashundhara'
a=a[:5]+a[6:]            
print(a)   
a='shajek'
print(len(a))
a='Eid day ' 
b='Gala day '
c='first day '
print(a+b+c+'off day')
print(a*4)
A='apple'
if 'apple'==A:
    print('matched')
else:
    print('something wrong')
#follow asci code:
a='abc'
b='ABC'
print(a>b)
a='coding line'
b=457
c=85.956389
# print(a+b+c)
#print(a.title())
d=a+"{}{:.2f}".format(b,c)
d=a+"{}{:.2f}".format(34,34.2322221)
print(d)
var4="{:<3}".format(d)
name='hasan'
name2='mehedi'
print('my name is %s and you can call me %s.' %(name,name2)) # this percentage % formating
# here s for string,f for float, d for dubble 
print('my name is {} and you can call me {}.'.format(name,name2))
print('my name is {1} and you can call me {0}.'.format(name,name2)) # print by indexing

print('my name is {var1} and you can call me {var2}.'.format(var1=name,var2=name2))
print(f'my name is {name} and you can call me {name2}.')
x=10
y=20
print(f'The value is {{x+y}} equal {x+y}.')
print('my name is \'jig\' and you can call me \"jag\".')
print(f'my name is {name.split()} and you can call me {name2.upper()}.')
# introduction=f"My name is {name}."

print(var4)
a='apple'
print('l'not in a)
#string method()
a='negative index'
print(a.split())
print(a.capitalize())
print(a.title())
print(a.upper())
b='HasIna Mojib Tarek'
b1='HasIna', 'Mojib', 'Tarek'
print()
print(b.lower())
print(b.casefold())
print('*'.join(b))
print(b.join(' .'))
print(b.join('**'))
print('/'.join(b1))
words = ['Hello', 'world']
result = ' '.join(words)
print(result)  # Output: Hello world
data = ['John', 'Doe', '30', 'Engineer']
csv_line = ','.join(data)
print(csv_line)  # Output: John,Doe,30,Engineer
name_parts = ['Mr.', 'John', 'Doe']
full_name = '/'.join(name_parts)
print(full_name)  # Output: Mr. John Doe


txt = "Hello, welcome to my world."
# na pele error dibe
x = txt.index("welcome")
x1 = txt.index("to")

print(x)
print(x1)
b='HasIna Mojib Tarek'
print(b.find('z')) # na pele -1 print korbe find,rfind,er shomoy and eta
print(b.find('s')) 
print(b.rfind('M'))
print(b.rfind('I'))
print(b.center(30))
b='2y2y2y a dh2yamaka 8282kk82y2y2y'
print(b.count('2'))
print(b.center(61,"$"))
print(b.rjust(30,'#'))
# print(b.rjust(34,'s'))
print(b.ljust(50,"#"))    
print(b.count("k"))
print(b.strip("2y")) 
b='  2y2y2y a dhamaka 828282y2y2y  '# eta shudu prthomer and last er value remove korte pare
print(b.strip())
# print(b.removeprefix('a'))
s='f567657 fan dad father,dad father 77357'
# print(s.strip())
# print(s.strip('f'))
# print(s.rstrip('567')) 
# print(s.rstrip('567'))
b=s.split() 
# c=b.strip()
# print(c)
print(b[2])
#print(b[0])
txt = "50"
x = txt.zfill(10)
print(x)
print(b)
print(type(b))
print(s.split(',')) 
print(s.split("father",2))
print(s.split('father',1))
print(s.rsplit('father',1))
s='''565657 father shans777 father'
helsa'''
p=s.splitlines()
print(p)
print(len(p))
print(s)
print(s.splitlines())
print(s.splitlines(True))
print(s.splitlines('  '))
print(s.splitlines(False)) # default false thake
s='565657 father 777 father Goru'
print(s.replace('father','mom'))
print(s.partition('father'))
print(type(s))
print(s.partition('777'))
print(s.partition('father'))
f=s.partition('u')
print(type(f))
print(s.partition('father'))
print(s.swapcase())
print(s.endswith('u'))
print(s.endswith('goru'))
print(s.startswith('565657'))
print(s.zfill(50))
print(s.replace('father','mom'))  
print(s.islower())
print(s.istitle())  
s='565657 Father 777 father Gor'
print(s.isupper())
print(s.islower())
s='5/7 bjhb'
print(s.isnumeric())
print(s.isdigit())
print(s.isdecimal())
print(s.isalpha())
a='apple eat' 
print('e'in a)
a='1 2 3 4 5 6 7'
print(a[::-1])
b=('1 2 3 4 5 6 7').split()
print(b)
sum=0
for i in b:
    num=int(i)
    sum=sum+num
print(sum)
 


# Creates a list of tuples representing all combinations of (x, y)
# where both x and y range from 0 to 2.
coordinates = [(x, y) for x in range(3) for y in range(3)]

print(coordinates)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

res = [val for row in mat for val in row]

print(res)

a = [1, 2, 3, 4, 5]

# Create a new list where each element in the 
#first 3 elements of 'a' is multiplied by 2
result = [x * 2 for x in a[:3]]

print(result)

a = [1, 2, 3, 4, 5, 6]

# Filter even numbers from the last three elements
evens = [x for x in a[-3:] if x % 2 == 0]

print(evens)

s = "hello"

for i, char in enumerate(s):
    print(f"Index {i}: {char}")
# Strings are immutable, that is we cannot change or delete any character of the string. If we try doing so, we get an error.However, we can delete the entire string but we get a NameError if we try accessing the string after deleting.

String = "Python"
print("Left,centre and right alignment by formatting:")

print("|{:<15}|{:^15}|{:>15}|".format(String, 'is', 'fun'))


num=34.561235

print("The value with %3.2f formatting is:")
print(" %.2f " %num)

print("The value with %3.5f formatting is:")
print(" %3.5f " %num)

print("PythonGeek\'s")
print("Python\nGeek")
print("\tPythonGeek")
print("\tPythonGeek".expandtabs(tabsize=10))
print('hello\bPythonGeek')
print('hello\b\bPythonGeek')
print("\\PythonGeek\\\\")
print("\"PythonGeek\"")
print("\fPythonGeek")
print("32465324\rPython")
n=1
print(n+n)

