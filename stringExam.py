# question no 1

Gmail=input('Enter an email address:')
if '@' in Gmail :
    print("The email address is valid.")
else:
    print("The email address is not valid.")

# question no 2

Palindrome=input('Enter a string:')
reverse=Palindrome[::-1]
if (Palindrome==reverse):
    print('The string is a palindrome.')
else:
    ('the string is not a palindrome.')

# question no 3
# print(punctuation)
# special=any(not i.isalnum() for i in password)
from string import punctuation
special=punctuation

print('Enter your password. It must contain at least 8 characters,with including an uppercase letter, a number, and a special character.')
password=input('Enter your password:')
upper=any(i.isupper() for i in password)
number=any(i.isnumeric() for i in password)
space=any(i.isspace() for i in password)
if len(password)>=8:
    if upper:
        if number:
            if special in password:
                if space:
                    print('please remove the space.')
                else:
                    print('This is a strong password.')
            else:
                print('enter at least one special cheracters.')
        else:
            print('enter at least one a numeric.')
    else:
        print('enter at least one uppercase letters.')
else:
    print('please enter the password at least 8 charecters')

# question no 4


Text=input('Enter your text:')

print('Here total characters:',len(Text))

word=Text.split()
print('Here total words:',len(word))


# question no 5

# value='.','?','!'
# value1=any(i for i in value)

Text=input("Enter your paragraph:")
text2=Text.split('.')
text3=[i.capitalize() for i in text2]
text11=('.'.join(text3))
print(text11)
var=(4)

print(type(4))
var=(4)

print(type(4))
# question no 6

set1={1,2,3,4,5}
set1.clear()
print(set1) 
tup=(1,2,3,1,1.0,4)
print(tup.count(1))

dic={'a':1,'e':2,2:54}
type(dic.keys())

print((1,2,3)+('a','b','c'))
# question no 7

TextReverse=input('Enter a string:')
reverse=TextReverse[::-1]
print(reverse)



# question no 8
Word=input('Enter a  paragraph of text:')
WordSplit=Word.split()
print(len(WordSplit))