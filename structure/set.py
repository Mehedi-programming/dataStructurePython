set1={'name','age','location',(1,2,'hasan')}
# print(type(set1))
# print(set1)
print(set1)
# print(set1[0])  # it will return type error

# for i in set1:
#     print(i)

for i in set1:
    if type(i) is tuple:
        print(i)

for i in set1:
    if type(i) is tuple:
        for j in i:
            print(j)
set1={'name','age','location','hasan'}
set1.add('mehedi')
print(set1)

set1.update([2,65,1,'gazi'])
print(set1)

set1.remove('location')
print(set1)

set1.pop()
print(set1)

set1.discard('mehedi')
print(set1)

# set1.clear()
# print(set1)
set1={'name','age','location',(1,2,'hasan')}
set2={3,44,22,34}
# set1.update(set2)
# print(set1)

set3=set1.union(set2)
print(set3)

print(set2 | set3)

d={2,132,2,12,3}
er={3,22,11,2,12}
print(d-er)
print(d&er)
hello = set([1,2,3,4,5,6,7,8,9,1,2,3,4,5])
(hello.add(10))
print(hello)