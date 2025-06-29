def LibraryMenuItems():
    print('1. Add new book:')
    print('2. Show all books:')
    print('3. Find your book by naming:')
    print('4. Book issue:')
    print('5. Return the book:')
    print('6. Break from here:')

def Added(BOOKS):
    Title=input('Enter the books name:')
    Author=input('Enter the author name:')
    Status=input('Enter your books status:')
    while True:
        try:
            Year=int(input('Enter the books published day:'))
        except ValueError:
            print('please enter the the year in integer number:')
        else:
            break
    SingleBook={'title':Title.strip(),'author':Author.strip(),'year':Year,'status':Status.strip(),'id':0}
    for book in BOOKS:
        if book['title']==Title and book['author']==Author:
            print('Sorry this book is already added.')
            return
    BOOKS.append(SingleBook)
    for index,book in enumerate(BOOKS,start=1):
        book['id']=index

BOOKS=[]

def ShowAllBooks(BOOKS):
    if BOOKS==[]:
        print('Sorry your book shell is empty.')
        return
    for book in BOOKS:
        print(f'Title:{book['title']},Author:{book['author']},published year:{book['year']},id:{book['id']},status:{book['status']}')

def FindBook(BOOKS):
    if BOOKS==[]:
        print('Sorry your book shell is empty.')
        return
    CheckTitle=input('Enter your books title name:')
    CheckAuthor=input('Enter the author name:')
    for book in BOOKS:
        if book['title']==CheckTitle.strip() and book['author']==CheckAuthor.strip():
            print(f'Title:{book['title']},Author:{book['author']},published year:{book['year']},id:{book['id']},Status:{book['status']}')
            return
        
def BookIssue(BOOKS):
    if BOOKS==[]:
        print('Sorry your book shell is empty.')
        return
    Title=input('Enter your books title:')
    Author=input('Enter your books author:')
    for book in BOOKS:
        if book['title']==Title.strip() and book['author']==Author.strip():
            book.update({'status':'issued'})
            print(f'id:{book['id']},Title:{book['title']},Author:{book['author']},published year:{book['year']},Status:{book['status']}')
            return
    BOOKS.append(book)

def BookReturn(BOOKS):
    for book in BOOKS:
        if book['status']=='issued':
            book.update({'status':'available'})
            print(f'Return book is id:{book['id']},Title:{book['title']},Author:{book['author']},published year:{book['year']},Status:{book['status']}')


def LibraryMenu():
    while True:
        LibraryMenuItems()
        while True:
            try:
                selectNumber=int(input('Enter your chooice:'))
            except ValueError:
                print('please choose chooice in an integer within (1 to 6):')
            else:
                break
        if selectNumber==1:
            Added(BOOKS)
        elif selectNumber==2:
            ShowAllBooks(BOOKS)
        elif selectNumber==3:
            FindBook(BOOKS)
        elif selectNumber==4:
            BookIssue(BOOKS)
        elif selectNumber==5:
            BookReturn(BOOKS)
        elif selectNumber==6:
            break
        else:
            print('Please enter 1 to 6.')

LibraryMenu()