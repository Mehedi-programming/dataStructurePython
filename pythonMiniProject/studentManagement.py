def displayStudent():
    print('student add for 1:')
    print('student CGPA for 2:')
    print('student highest CGPA for 3:')
    print('student lowest CGPA for 4:')
    print('student overall cgpa for 5:')
    print('Break from there 6:')
STUDENT=[]
def added(STUDENT):
    while True:
        try:
            StudentId=int(input('Enter your ID:'))
        except ValueError:
            print('please enter the ID in integer number:')
        else:
            break
    for student in STUDENT:
        if student['studentId']==StudentId: 
            print('Sorry,This student already added.')
            return

    name=input('Enter your name:')
    deparment=input('Enter your deparment name:')
    while True:
        try:
            bangla=int(input('Enter your marks in bangla:'))
            math=int(input('Enter your marks in math:'))
            English=int(input('Enter your marks in English:'))
        except ValueError:
            print('please enter your marks in integer:')
        else:
            break

    marks={'bangla':bangla,'math':math,'english':English}
    if bangla >= 85:
        banglaGpa= 4.00
    elif bangla >= 80:
        banglaGpa= 3.80
    elif bangla >= 70:
        banglaGpa= 3.30
    elif bangla >= 60:
        banglaGpa= 3.00
    else:
        banglaGpa= 0.00
    if math >= 85:
        mathGpa= 4.00
    elif math >= 80:
        mathGpa= 3.80
    elif math >= 70:
        mathGpa= 3.30
    elif math >= 60:
        mathGpa= 3.00
    else:
        mathGpa=00
    if English >= 85:
        EnglishGpa= 4.00
    elif English >= 80:
        EnglishGpa= 3.80
    elif English >= 70:
        EnglishGpa= 3.30
    elif English >= 60:
        EnglishGpa= 3.00
    else:
        EnglishGpa=00
    total_gpa=[banglaGpa,mathGpa,EnglishGpa]
    summation=sum(total_gpa)
    CGPA=summation/(len(marks))
    student={'studentId':StudentId,'Name':name,
            'department':deparment,
            'marks':marks,'CGPA':CGPA}
    STUDENT.append(student)


def cgpa_count(STUDENT):
    for i in STUDENT:
        while True:
            try:
                StudentId=int(input('Enter your ID:'))
            except ValueError:
                print('please enter the ID in integer number:')
            else:
                break
        if i['studentId']==StudentId: 
            result=i.get('CGPA')
            roundResult=result
            print(f'your cgpa is:{round(roundResult,3)}')
            return

def highestCGPA(STUDENT):
    CGPA=[]
    for i in STUDENT:
        cg=i.get('CGPA')
        CGPA.append(round(cg,3))
    print(max(CGPA))

def lowestCGPA(STUDENT):
    CGPA=[]
    for i in STUDENT:
        cg=i.get('CGPA')
        CGPA.append(round(cg,3))
    print(min(CGPA))

def average(STUDENT):
    CGPA=[]
    for i in STUDENT:
        cg=i.get('CGPA')
        CGPA.append(round(cg,3))
    lenth=len(CGPA)
    summation=sum(CGPA)
    average1=(summation/lenth)
    print(round(average1,3))

def StudentInformation():
    while True:
        displayStudent()
        while True:
            try:
                selectNumber=int(input('Enter your chooice:'))
            except ValueError:
                print('please choose chooice in an integer within (1 to 5):')
            else:
                break
        if selectNumber==1:
            added(STUDENT)
        elif selectNumber==2:
            cgpa_count(STUDENT)
        elif selectNumber==3:
            highestCGPA(STUDENT)
        elif selectNumber==4:
            lowestCGPA(STUDENT)
        elif selectNumber==5:
            average(STUDENT)
        elif selectNumber==6:
            break
        else:
            print('Please enter 1 to 5.')
StudentInformation()




