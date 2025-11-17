# Student={}
Students=[]

i=0
while(i<3):
    student={
    'name':input('Enter your name:'),
    'cname':input('Enter your class name:'),
    'marks':int(input('Enter your marks:'))
    }
    i+=1
    Students.append(student)


for i in Students:
    for j ,x in i.items():
        print(j,':',x)
    print('-' * 20)
     
Name=input('Enter your choicess name:')
for i in Students:
    if i['name']==Name:
        for j,x in i.items():
            print(j,':',x)
            

