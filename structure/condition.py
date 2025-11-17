a = 2
b = 330
print("A") if a > b else print("B")
a = 330
b = 330

# print("A") if a > b else print("=") if a == b else print("B1")
print('A') if a> b else print('both are equal') if a==b else print('B1')
x = 41

if x > 10:  
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
else:
    print("but not above 20.")

a = 33
b = 200

if b > a:
  pass

x='2312'
y=231
print(x+str(y))
x = [1, 2, 3]
y = x
y.append(4)
print(x)
x=10
y=3
print(x/y)
x = "Hello"
y = 'World'
print(x + " " + y)
p, q, r = 10, 20 ,30
print(p, q, r)
for i in range(1, 5):
    print(i)
else:
    print("this is else block statement" )
var= "James Bond"
print(var[2::-2])
salary = 8000

def printSalary():
  salary = 12000
  print(f"Salary:{salary}")
  
printSalary()
print("Salary:", salary)
sampleSet = {"Jodi", "Eric", "Garry"}
sampleSet.add(1,"Vicki")
print(sampleSet)
def calculate (num1, num2=4):
  res = num1 * num2
  print(res)

calculate(5, 6)
var1 = 1
var2 = 2
var3 = "3"

print(var1 + var2 + var3)
sampleList = ["Jon", "Kelly", "Jessa"]
sampleList.append(2, "Scott")
print(sampleList)
str = "pynative"
print (str[1:3])
x = 36 / 4 * (3 +  2) * 4 + 2
print(x)
var = "James" * 2  * 3
print(var)