print('\t\t\t LIBRARY MANAGEMENT SYSTEM\t\t\t')

class Library:
    def __init__(self):
        pass
        

    def check_Details(self):
        with open('Lib_data.txt', 'r') as f:
            check= f.read()
            return check


    def add_book(self): 
        bookName= input('Please enter the book name\n')   
        with open ('Lib_data.txt', 'a') as f:
            book=f.write(bookName+'\n')
            print('Book is added')
            return book
                

    def remove_book(self):
        removeBook= input('Please enter the book name you want to remove\n')
        with open('Lib_data.txt', 'r') as f:
            lines = f.readlines()
            with open('Lib_data.txt', 'w') as f:
                for line in lines:
                    if line.strip() != removeBook:
                        remove= f.write(line)
                        print('Book removed')
                        return remove
                    

    def assign_book(self):  
        MyList=[]

        with open('Lib_data.txt','r') as f:
            for line in f:
                MyList.append(line.strip())

        name= input('Enter your full name: \n')
        assignBook= input('Please enter the book name, you want to assign: ')

        if assignBook in MyList:
            already_assigned = False
            with open("book_assign.txt", "r") as f:
                checking= f.readlines()
                for line in checking:
                    if assignBook in line:
                        already_assigned = True
                        break

            
            if already_assigned:
                print(f"Sorry! the requested book {assignBook} is already assigned to another reader!")

            else:
                with open('book_assign.txt','a') as user:
                    user.write(assignBook +'\t'+ name +'\n')
                    print(f'Book "{assignBook}" has been assigned to {name}')
        else:
            print(f'Sorry the {assignBook} is not in library!')



library= Library()

while True:
    print("\n1. Check book details \n2. Add a Book\n3. Remove Book\n4. Assign a Book\n 5. Exit")
    choice=input("Enter your choice: ") 

    if choice == "1":
        print(library.check_Details())
    
    elif choice== "2":
        library.add_book()
    
    elif choice == "3":
        library.remove_book()

    elif choice == "4":
        library.assign_book()
    
    elif choice == "5":
        break

    else:
        print("Invalid choice, please try again!")
    




















# cont= input('Do you want to continue?: Y/N\n')

# if cont=='N':
#     print('Thank you')
# else:
#     print({'1': 'add book', '2':'Remove book', '3':'Check book details'})
#     user= input('What do you want to do please choose:\n')
#     if user=='1':
#         with open ('Lib_data.txt', 'a') as f:
#                 new_book=(input('Please enter the book name\n'))
#                 wish= input('Do you want to add this book?: Y/N\n')
#                 if wish=='Y':
#                     f.write(new_book+'\n')
#                     print('Book is added')
#                 else:
#                     print('Book is not added')

#     elif user=='2':
#         with open('Lib_data.txt', 'r') as f:
#             lines = f.readlines()

#         remove_book = input('Please enter the book name you want to remove\n')
#         wish1 = input('Please confirm do you want to remove the book?: Y/N\n')

#         if wish1 == 'Y':
#             with open('Lib_data.txt', 'w') as f:
#                 for line in lines:
#                     if line.strip() != remove_book:
#                         f.write(line)
#             print('Book removed')
#         else:
#             print('Book not removed')



# MyList=[]
# with open('Lib_data.txt','r')as f:
#     for line in f:
#         MyList.append(line.strip())
# name= input('Enter your full name\n')
# assignBook= input('Please enter the book name, you want to assign: ')
# if assignBook in 'Lib_data.txt':
#     with open('book_assign.txt','a') as user:
#         user.write(assignBook+'\t'+ name+'\n')
#         print('Book assigned')
# else:
#     print('Book is not in library')

