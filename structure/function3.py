students = [
    {'id': 1,
    'name': 'Alice Johnson',
    'email': 'alice.johnson@college.edu',
    'department': 'Computer Science',
    'gpa': 3.8
    },
    {'id':34,
    'name': 'Bob Smith',
    'email': 'bob.smith@college.edu',
    'department': 'Mechanical Engineering',
    'gpa': 3.2
    },
    {'id': 34,
    'name': 'Charlie Lee',
    'email': 'charlie.lee@college.edu',
    'department': 'Electrical Engineering',
    'gpa': 3.5
    },
    {'id':34,
    'name': 'Diana Gomez',
    'email': 'diana.gomez@college.edu',
    'department': 'Business Administration',
    'gpa': 3.9
    },
    {'id': 5, 
    'name': 'Ethan Brown',
    'email': 'ethan.brown@college.edu',
    'department': 'Mathematics',
    'gpa': 3.6
    }
]

# read opearation
def student_fetch(student):
    for i in student:
        i['gpa']=3.9
        print(i)
    print('='*30)
# student_fetch(students)
# delete opearation
def student_delete(ID,student):
    for i in student:
        if i['id']==ID:
            student.remove(i)
    print(f'reaming student: {student}')
    print('='*30)

# student_delete(34,students)
# student_delete(3,students)

# create opearation
def student_create(**kwargs):
    for i,j in kwargs.items():
        print(i,':',j)
    print('='*30)
    students.append(kwargs)
    print(students)


# student_create(student={'id':6,'name':'Ayaan', 'age':20, 'department':'Computer Science', 'email':'ayaan@example.com','gpa':232})
# student_create(id=7,name='Ayaan', age=20, department='Computer Science', email='ayaan@example.com',CGPA=3.66)
# student={'id':6,'name':'Ayaan', 'age':20, 'department':'Computer Science', 'email':'ayaan@example.com','gpa':232}
# student_create(**student)

# update operation
def student_update(ID,student):
    for i in student:
        if i['id']==ID:
            i.update({'name':'mehedi','email':'mehedihasan@gmail.com'})
    print(students)
    print('='*30)

# student_update(34,students)

# update operation
def student_update(ID,**kwargs):
    for i in students:
        if i['id']==ID:
            i['name']=kwargs['name']
            i['department']=kwargs['department']
    print(students)
    # print('='*30)

student_update(2,**{'name':'hasan','department':'Blockchain'})
def student_list_input():
    print('Enter 1 for fetch.')
    print('Enter 2 for add.')
    print('Enter 3 for delete.')
    print('Enter 4   for update.')
    print('Enter 5 for update.')
while True:
    student_list_input()
    print("Enter your choose:(1 to 4....)")
    value=int(input('Enter your choise:'))
    if value==1:
        student_fetch(students)
    elif value==2:
        student={'id':6,'name':'Ayaan', 'age':20, 'department':'Computer Science', 'email':'ayaan@example.com','gpa':232}
        student_create(**student)
    elif value==3:
        student_delete(3,students)
    elif value==4:
        student_update(2,**{'name':'hasan','department':'Blockchain'})
    elif value == 5:
            print('Exit')
            break
    else:
        print('Enter a valid number:')














