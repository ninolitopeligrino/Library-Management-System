import library

lib = library.Library()

while True:
    print('Welcome to E-Library')
    print('1. Add Books')
    print('2. Borrow Books')
    print('3. Return Book')
    print('4. Search Name')
    print('5. Display')
    choice = int(input('Enter Option: '))
    if choice == 0:
        break
    elif choice == 1:
        lib.addBook()
    elif choice == 2:
        lib.borrowBooks()
    elif choice == 3:
        lib.returnBook()
    elif choice == 4:
        lib.searchBorrower()
    elif choice == 5:
        print('1. Display all the Books available')
        print('2. Display all the borrowered books')
        select = int(input()) #Selecting option either display all the books available in the library or display all the borrowers.
        lib.displayBooks(select) #Display Function
    