# for i in range(100,0,-1)

a = 330
b = 330

print("A") if a > b else print("=") if a == b else print("B")

marks = 85
grade = "A+" if marks >= 80 else "A" if marks >= 70 else "B" if marks >= 60 else "F"
print("your grade is:", grade)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

i = 1
while i < 10:
  print(i)
  if (i == 3):
    break
  i += 1


# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

i = 0
while i < 10:
  i += 1
  if i == 3:
    continue
  print(i)

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("List of numbers:", numbers)


def multivalu():
    while True:
      try:
        numbers = list(map(int, input("Enter numbers separated by space: ").split()))
        print("List of numbers:", numbers)
      except ValueError:
        print("please enter only number.")
      else:
         break
      
multivalu()

