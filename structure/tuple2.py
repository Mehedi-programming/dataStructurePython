name=("md", "mehedi", "hasan",("shajal","rafi"), "mozumder",2,4,5,1)
print(len(name))
name2=("Md", "Mehedi", "Masan","shajal","rafi", "mozumder")
print(sorted(name2))
var='name','name2','name3','name4'
print(name+name2)
print(type(var))
var1=('name',)
print(type(var1))
var2=2,3,1,2,3,3
print(type(var2))
var2=tuple()
print(type(var2))
print(max(name2))
num=(1,2,3,4,5)
print(num.count(2))
print(sum(num))
print(num.index(4))
name=("md", "mehedi", "hasan",("shajal","rafi"), "mozumder",2,4,5,1)
name1=name[2]='uryr'
print(name1)
print(name[3])
print(name[0:3])
print(name[2:])
for x in name:
    print(x)
name=("md", "mehedi", "hasan",("shajal","rafi"), "mozumder",2,4,5,1)
# for x in name:
#     if x=='mehedi':
#         # name[x]='hasan'
#         name[name.index(x)]='hasan'
print(name)
d=str(name)
print(d)
b=list(name)
b.append('russel')
print(b)
c=tuple(b)
print(c)
print(name)
print(name[2])
print(type(name))
name=("mehedi")
print(type(name))
name1=("mehedi",)
print(type(name1))
nam=("md", "mehedi", "hasan",["shajal","haji"], "mozumder",2,4,5,1)
#nam[3][0]="kamrul","rafi"
print(nam)
print(nam[3][1])
for i in nam:
    if type(i) is list:
        for j in i:
            print(j)   
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thistuple1 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)
print(len(thistuple))
print(max(thistuple))
print(sum(thistuple))
print(sorted(thistuple))

print(x)

# del thistuple
# print(thistuple)

print(1 in thistuple)
print(4*thistuple)
print(thistuple+thistuple1)
