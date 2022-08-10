import pandas as pd
import numpy as np
import time


class Library:
    def __init__(self):
        self.list_of_books = pd.read_csv('books.csv', on_bad_lines='skip')
        self.borrower = pd.read_csv('borrower.csv', on_bad_lines='skip')

    def addBook(self):
        title = input('Enter title: ')
        author = input('Enter author: ')
        isbn = int(input('Enter ISBN: '))

        #Check ISBN if it is already exist. 
        #ISBN Nnumber is an Unique Number for books.
        check_isbn = self.list_of_books[self.list_of_books['isbn'] == isbn]
        if check_isbn.empty:
            genre = int(input('Enter genre: '))
            add = Book(title, author, isbn, genre)
            dic = {
                'title' : add.title,
                'author' : add.author,
                'isbn' : add.isbn,
                'genre' : add.genre
            }
            df = pd.DataFrame([dic])
            df.to_csv('books.csv', mode='a', index=False, header=False)
            self.list_of_books = pd.read_csv('books.csv', on_bad_lines='skip')
        else:
            print('ISBN Number Already Exist.')

    def borrowBooks(self):
        while True:
            title = input('Enter title of the book to borrow: ')
            if title == 'show':
                print(self.list_of_books)
            else:
                #Check whether the title exist in the library.
                check_title = self.list_of_books[self.list_of_books['title'] == title]
                if check_title.empty:
                    print('There is no ', title, 'in the library')
                else:
                    print(check_title)
                    isbn = int(input('Enter ISBN: '))
                    check_isbn = self.list_of_books[self.list_of_books['isbn'] == isbn].iloc[0]
                    if check_isbn.empty:
                        print('Book with an ISBN number of', isbn, 'is not available in the library')
                    else:
                        name = input('Enter Full Name: ')
                        grade = input('Enter Year and Section: ')
                        borrow = {
                            'name of borrower': name,
                            'yr_section': grade,
                            'date borrowed': time.ctime(),
                            'title': check_isbn['title'],
                            'author': check_isbn['author'],
                            'isbn': check_isbn['isbn'],
                            'genre': check_isbn['genre']
                        }
                        df = pd.DataFrame([borrow])
                        df.to_csv('borrower.csv', mode='a', index=False, header=False)
                        self.borrower = pd.read_csv('borrower.csv', on_bad_lines='skip')

                        array = self.list_of_books[['title', 'author', 'isbn', 'genre']].values
                        count = 0
                        for i in array:
                            if i[2] == isbn:
                                array = np.delete(array, count, axis=0)
                                break
                            count += 1
                        df = pd.DataFrame(array, columns=['title', 'author', 'isbn', 'genre'])
                        df.to_csv('books.csv', index=False)
                        self.list_of_books = pd.read_csv('books.csv')
                        print(check_isbn['title'], 'has successfully borrowed to', name)
                        time.sleep(2)
                        break

    def returnBook(self):
        while True:
            title = input('Enter title of the book to be returned: ')
            if title == 'show':
                print(self.borrower)
            else:
                name = input('Enter Full Name of the Borrower: ')
                check_name = self.borrower[(self.borrower['name of borrower'] == name) & (self.borrower['title'] == title)]
                if check_name.empty:
                    print('No book found.')
                else:
                    print(self.borrower[(self.borrower['title'] == title) & (self.borrower['name of borrower'] == name)])
                    isbn = int(input('Enter ISBN Number: '))
                    check_isbn = self.borrower[self.borrower['isbn'] == isbn].iloc[0]
                    if check_isbn.empty:
                        print('No ISBN Found')
                    else:
                        dic = {
                            'title': check_isbn['title'],
                            'author': check_isbn['author'],
                            'isbn': check_isbn['isbn'],
                            'genre': check_isbn['genre']
                        }
                        df = pd.DataFrame([dic])
                        df.to_csv('books.csv', mode='a', index=False, header=False)
                        self.list_of_books = pd.read_csv('books.csv', on_bad_lines='skip')

                        array = self.borrower[['name of borrower','yr_section','date_borrowed','title','author','isbn','genre']].values
                        count = 0
                        for i in array:
                            if i[5] == isbn:
                                array = np.delete(array, count, axis=0)
                                break
                            count += 1
                        df = pd.DataFrame(array, columns=['name of borrower','yr_section','date_borrowed','title','author','isbn','genre'])
                        df.to_csv('borrower.csv', index=False)
                        self.borrower = pd.read_csv('borrower.csv')
                    print('Returned Book Successfully!')
                    time.sleep(3)
                    break

    def searchBorrower(self):
        name = input('Search Name: ')
        check_name = self.borrower[self.borrower['name of borrower'] == name]
        if check_name.empty:
            print('There is no', name,'list.')
        else:
            print(check_name)
        time.sleep(2)


    def displayBooks(self, choice):
        if choice == 1:
            print(self.list_of_books)
            print('There are', self.list_of_books.shape[0],'books available.')
        elif choice == 2:
            if self.borrower.empty:
                print('There no borrowed books')
            else:
                print(self.borrower)
                print('There are', self.borrower.shape[0],'books lent out')
        time.sleep(2)
        
class Book:

    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.isbn = isbn
        self.author = author
        if genre == 1:
            self.genre = 'Philosophy'
        elif genre == 2:
            self.genre = 'History'
        elif genre == 3:
            self.genre = 'Computer Science'
        elif genre == 4:
            self.genre = 'Art and Recreation'
        elif genre == 5:
            self.genre = 'Pure Science'
    
    def displayBook(self):
        print('Title: ', self.title)
        print('Author: ', self.author)
        print('ISBN ', self.isbn)
        print('Genre ', self.genre)

class Borrower:
    def __init__(self, name, year):
        self.name = name
        self.year = year