informtion={'name':('mehedi',1,2,3),'age':22,'height':'5.9','education':'HSC','current':'dhaka'}
# print(informtion['name'])
# for i in informtion.values():
#     print(i)
for i,j in informtion.items():
    print(i)
b=informtion.setdefault('name')
print(informtion,b,sep='\n')
#change
informtion['height']=('5.10',2)
print(informtion)
print(informtion.clear())
informtion={'name':('mehedi',1,2,3),'age':'22','height':'5.9','education':'HSC','current':'dhaka'}
hello={'year':2330}
print(informtion[hello])

print(informtion)
#del informtion["education"]
informtion.popitem()
print(informtion)
#copy
b=informtion.copy()
print(sorted(b))
print(b)
informtion={'name':('mehedi',1,2,3),'age':'22','height':'5.9','education':'HSC','current':'dhaka'}
for i in informtion:
    print(i)
for i in informtion.values():
   print(i)
for i,j in informtion.items():
    print(i,":",j)
print(informtion.keys())
print(informtion.values())
print(informtion.items())
# this is one kind of add
# b={'email':'mehedimozumder',
# 'age':'21'}
informtion.update({'email':'mehedimozumder',
'age':'21'})
print(informtion)
details=('name','age','location')
# c=dict.fromkeys(details)
# for i in c:
#     if i=='name':
#         c['name']='mehedi'
#     elif i=='age':
#         c['age']='22'
#     elif i=='location':
#         c['location']='cumilla'
# print(c)

student={

}
print(type(student))
student={
    'id':24,
    'name':'mehedi',
    'age':22
}
print(student)
student={
    'id':24,
    'name':'mehedi',
    'age':22,
    'id':241014023
}
student['department']='cse'
student.update({'section':3})
print(student) 
print(student.get('age'))
student['name']='mozumder'
print(student)
print(student.get('id'))
print(student.get('name'))
for x in student.values(): 
    print(x)
for x in student.keys():   # here he print keys without comadding, like he bydefault print keys       
    print(x)
for x,y in student.items(): 
    print(x,':',y)
student=[
    {'id':24,'name':'mehedi','age':22},
    {'id':24,'name':'mehedi','age':22},
    {'id':24,'name':'mehedi','age':22},
    {'id':241,'name':'mehedi','age':22}
]
# print(student)
for i in student:
    # print(i)
    if i['id']==241:
        i.update({'year':2025,'passing_time':2030})
    print(i)
h=0
hell=[]
for x in student:
    hello=x.get('id')
    hell.append(hello)
    h+=hello
print(hell)
print(max(hell))
print(h)
for x in student:
    for j,i in x.items():
        print(j,':',i)

for x in student:
    x.pop('name')
    print(x)

for c in student:
    c['va']=32
    print(c)
student={
    'id':24,
    'name':'mehedi',
    'age':22,
    'year':2024
}
student.update({'id':43,'fname':'hasan'})
print(student)
# student.clear()
# print(student)
# del student
# print(student)
student.pop('id')
print(student)
x=student.popitem()
print(x)    # here it will return an items in tuple ,which one he removed
print(len(student))
student={}
x=student.fromkeys(['name','position','salary','id'],57)
print(x)

# before providing value ,you can set this kind of dictionary

student={
    'id':24,
    'name':'mehedi',
    'age':22,
    'year':2024,
    'marks':{'bangla':44,'english':66,'math':67,}
}
h=student.get('marks')
print(type(h))
print(sum(h.values()))
for x in h.values(): 
    print(x)
    value=h.values()
    print(sum(value))
print(value)


student.setdefault('position','faculty')
print(student)
print(student['marks']['math'])
del student['id']
print(student)

student = {'position': 'student','value':5687}
student.setdefault('position', 'faculty')
print(student)



student={}
id = int(input('Enter your student ID: '))
name=input('Enter your name:')
item=input('Enter your item:')
value=int(input('Enter your value:'))
student[id]={'name':name,'item':item,'value':value}
print(student.values())

STUDENTS=[]
i=0
while(i<2):
    
    i+=1
    id = int(input('Enter your student ID: '))
    name=input('Enter your name:')
    item=input('Enter your item:')
    value=int(input('Enter your value:'))
    student[id]={'name':name,'item':item,'value':value}
    
for st ,l in student.items():
    student_data ={'id': st, 'name': l['name'], 'item': l['item'],'value': l['value']}
    STUDENTS.append(student_data)
      


for j in STUDENTS:
        print(f'ID:{j['id']} Name:{j['name']},Item:{j['item']},Value:{j['value']}') 