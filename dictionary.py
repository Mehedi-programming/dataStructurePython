def display_all_students():
    print('Welcome to Student Management System:')
    print('1. Add student')
    print('2. Display all students')
    print('3. Delete student')
    print('4. Find student')
    print('5. Count student')
    print('6. Exit')

def added(STUDENT):
    Student_Id = int(input('Enter your ID: '))
    for student in STUDENT:
        if student['Student_Id'] == Student_Id:
            print('This student is already added.')
            return
    student_name = input('Enter your name: ')
    student_age = int(input('Enter your age: '))
    student_CGPA = input('Enter your result: ')
    new_student = {
        'Student_Id': Student_Id,
        'student_name': student_name,
        'student_age': student_age,
        'student_CGPA': student_CGPA
    }
    STUDENT.append(new_student)


def delete(STUDENT):
    student_Id = int(input('Enter your student ID: '))
    for student in STUDENT:
        if student['Student_Id'] == student_Id:
            STUDENT.remove(student)
            print('Student has been deleted.')
            return
    print('Student ID not found.')

def find(STUDENT):
    Student_Id = int(input('Enter your student ID: '))
    for student in STUDENT:
        if student['Student_Id'] == Student_Id:
            print(f"ID: {student['Student_Id']}\nName: {student['student_name']}\nAge: {student['student_age']}\nCGPA: {student['student_CGPA']}")
            return
    print('Student ID not found.')

def display_all_student(STUDENT):
    if STUDENT!=0:
        print('The student list is empty:')
        for student in STUDENT:
            print(f"ID: {student['Student_Id']}\nName: {student['student_name']}\nAge: {student['student_age']}\nCGPA: {student['student_CGPA']}")
    else:
        print('There are no students.')


def count(STUDENT):
    if len(STUDENT)!=0:
        print(f"Total students: {len(STUDENT)}")
    else:
        print(0)
        

STUDENT = []
new_student={}
def my():
    while True:
        display_all_students()
        selection = input('Enter your selection (1 to 6): ')
        if selection == '1':
            added(STUDENT)
        elif selection == '2': 
            display_all_student(STUDENT)
        elif selection == '3':
            delete(STUDENT)
        elif selection == '4':
            find(STUDENT)
        elif selection=='5':
            count(STUDENT)
        elif selection == '6':
            print('Exit')
            break
        else:
            print('Please enter a valid number (1 to 6).')

my()
