# 2 classes, lender and book
# csv file storing both, separately
# new function for every action 
# 3 more functions at end 


# should we add something so make sure that when
# you're adding books / lenders to the csv, the id is unique
# as the project rubric specifically mentions that it must be unique 

# in return_book, what should we do if the book does not exist
# in the books.csv file

# in all functions except add / return, is it okay if we use the parameters
# to be the unique id's and not something of type Lender / Book


import random 
import csv 
from datetime import date

class Lender():
    def __init__(self, unique_id, name, book_id, date, penalty):

        self.unique_id = unique_id
        self.name = name
        self.book_id = book_id
        self.date = date
        self.penalty = penalty 


    def print_(self):
        print("The parameters of the lender are: ")
        print(f"Unique ID: {self.unique_id}")
        print(f"Name: {self.name}")
        print(f"Book ID: {self.book_id}")
        print(f"Date: {self.date}")
        print(f"Penalty: {self.penalty}")
        print("============")

class Book():
    def __init__(self, unique_id, title, author, copies, times_borrowed):

        self.unique_id = unique_id
        self.title = title
        self.author = author
        self.copies = copies
        self.times_borrowed = times_borrowed


    def print_(self):
        print("The parameters of the book are: ")
        print(f"Unique ID: {self.unique_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Copies: {self.copies}")
        print(f"times_borrowed: {self.times_borrowed}")
        print("============")

def get_lenders():
    lender_list = []
    lender_listofdicts = []
    name_list = ['Rishika', 'Nichole', 'Alejandro', 'Doyin', 'Ron', 'Ananya', 'Chris', 'Selma', 'Jordan', 'Joy']

    csv_fd = open("lenders.csv", 'w')

    csv_writer = csv.DictWriter(csv_fd, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty'])
    csv_writer.writeheader()

    for i in range(10):
        lender_dict = {} 
        name = name_list[i]
        unique_id = i + 1 
        # book_id = random.randint(1000,2000)
        book_id = None
        # date = datetime.date(random.randint(1990,2021), random.randint(1,12), random.randint(1,28))
        date = None
        penalty = 0 
        
        lender_dict["name"] = name
        lender_dict["unique_id"] = unique_id
        lender_dict["book_id"] = book_id
        lender_dict["date"] = date
        lender_dict["penalty"] = penalty 

        lender_listofdicts.append(lender_dict)

        lender_1 = Lender(unique_id, name, book_id, date, penalty) 
        
        lender_list.append(lender_1)

    csv_writer.writerows(lender_listofdicts)

    return lender_list


def get_books():
    book_list = []
    book_listofdicts = []
    title_list = ['Beloved', 'Great Gatsby', 'Catcher in the Rye', 'To Kill a Mockingbird', 
    'Lord of the Rings', 'Untamed', 'Hatchet', 'Gone With The Wind', 'Goodnight Moon', 'Little Women']
    author_list = ['Jones', 'Robins', 'Noel', 'Obama', 'Smith', 'Zha', 'Stillman', 'Marchuck', 'Seewald', 'Pomahac']

    csv_fd = open("books.csv", 'w')

    csv_writer = csv.DictWriter(csv_fd, fieldnames = ['unique_id', 'title', 'author', 'copies', 'times_borrowed'])
    csv_writer.writeheader()

    for i in range(10):
        book_dict = {} 
        # unique_id = i + 1
        unique_id = random.randint(1000, 2000) 
        title = title_list[i]
        author = author_list[i]
        copies = random.randint(1,15)
        # times_borrowed = random.randint(0,3)
        times_borrowed = 0
        
        book_dict["unique_id"] = unique_id
        book_dict["title"] = title
        book_dict["author"] = author
        book_dict["copies"] = copies
        book_dict["times_borrowed"] = times_borrowed

        book_listofdicts.append(book_dict)

        book_1 = Lender(unique_id, title, author, copies, times_borrowed) 
        
        book_list.append(book_1)

    csv_writer.writerows(book_listofdicts)

    return book_list

def add_lender(lender):
    csv_fd = open("lenders.csv", 'a')
    csv_writer = csv.DictWriter(csv_fd, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty'])

    lender_dict = {}

    lender_dict["name"] = lender.name
    lender_dict["unique_id"] = lender.unique_id
    lender_dict["book_id"] = lender.book_id
    lender_dict["date"] = lender.date
    lender_dict["penalty"] = lender.penalty 

    csv_writer.writerow(lender_dict)

def remove_lender(remove_id):
    lines = list() 
    with open('lenders.csv', 'r') as read_file:
        reader = csv.DictReader(read_file)

        for row in reader:
            if row['unique_id'] != remove_id:
                lines.append(row) 
                

    with open('lenders.csv', 'w') as write_file:
        writer = csv.DictWriter(write_file, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty'])
        writer.writeheader()
        writer.writerows(lines)

def add_book(book):
    csv_fd = open("books.csv", 'a')
    csv_writer = csv.DictWriter(csv_fd, fieldnames = ['unique_id', 'title', 'author', 'copies', 'times_borrowed'])

    book_dict = {}

    book_dict["unique_id"] = book.unique_id
    book_dict["title"] = book.title
    book_dict["author"] = book.author
    book_dict["copies"] = book.copies
    book_dict["times_borrowed"] = book.times_borrowed 

    csv_writer.writerow(book_dict)

def remove_book(remove_id):
    lines = list() 
    with open('books.csv', 'r') as read_file:
        reader = csv.DictReader(read_file)

        for row in reader:
            if row['unique_id'] != remove_id:
                lines.append(row) 
                

    with open('books.csv', 'w') as write_file:
        writer = csv.DictWriter(write_file, fieldnames = ['unique_id', 'title', 'author', 'copies', 'times_borrowed'])
        writer.writeheader()
        writer.writerows(lines)


def borrow_book(lender_id, book_id):

    # Reading both csv files:
    csv_fd_book = open('books.csv', 'r')
    book_list = list(csv.DictReader(csv_fd_book))

    csv_fd_lender = open('lenders.csv', 'r')
    lender_list = list(csv.DictReader(csv_fd_lender))

    for book in book_list:

        # Finding the correct book:
        if book['unique_id'] == book_id:

            # Making sure there are enough copies:
            if (int)(book['copies']) > 0:

                for lender in lender_list:

                    # Finding the correct lender:
                    if lender['unique_id'] == lender_id:

                        # Making sure they don't owe more than $10
                        if (int)(lender['penalty']) <= 10:

                            lender['book_id'] = book_id
                            lender['date'] = date.today()
                            book['copies'] = (int)(book['copies']) - 1
                            book['times_borrowed'] = (int)(book['times_borrowed']) + 1
                        
                        else:
                            print("The lender has more than $10 penalty pending")
            
            else:
                print("There aren't enough copies of the book")

    csv_fd_book.close()
    csv_fd_lender.close()

    csv_fd_book = open('books.csv', 'w')
    writer = csv.DictWriter(csv_fd_book, fieldnames = ['unique_id', 'title', 'author', 'copies', 'times_borrowed'])
    writer.writeheader()
    writer.writerows(book_list)

    csv_fd_lender = open('lenders.csv', 'w')
    writer = csv.DictWriter(csv_fd_lender, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty'])
    writer.writeheader()
    writer.writerows(lender_list)



def modify_book_count(book_id, number, increase):

    csv_fd_book = open('books.csv', 'r')
    book_list = list(csv.DictReader(csv_fd_book))

    for book in book_list:
        if book['unique_id'] == book_id:
            if increase:
                book['copies'] = (int)(book['copies']) + number
            else:
                book['copies'] = (int)(book['copies']) - number

    csv_fd_book.close()
    csv_fd_book = open('books.csv', 'w')
    writer = csv.DictWriter(csv_fd_book, fieldnames = ['unique_id', 'title', 'author', 'copies', 'times_borrowed'])
    writer.writeheader()
    writer.writerows(book_list)

def return_book(lender_id):

    # Reading both csv files:
    csv_fd_book = open('books.csv', 'r')
    book_list = list(csv.DictReader(csv_fd_book))

    csv_fd_lender = open('lenders.csv', 'r')
    lender_list = list(csv.DictReader(csv_fd_lender))

    for lender in lender_list:

        # Finding the correct lender:
        if lender['unique_id'] == lender_id:
            
            book_id = lender['book_id']
            borrowed_date_list = lender['date'].split('-')
            borrowed_date = date(int(borrowed_date_list[0]), int(borrowed_date_list[1]), int(borrowed_date_list[2]))
            
            for book in book_list:

                # Finding the correct book:
                if book['unique_id'] == book_id:

                    book['copies'] = (int)(book['copies']) + 1
                    today = date.today()
                    days_passed = (today - borrowed_date).days
                    if days_passed > 7:
                        lender['penalty'] = (int)(lender['penalty']) + (days_passed - 7)

            lender['book_id'] = None
            lender['date'] = None

    csv_fd_book.close()
    csv_fd_lender.close()

    csv_fd_book = open('books.csv', 'w')
    writer = csv.DictWriter(csv_fd_book, fieldnames = ['unique_id', 'title', 'author', 'copies', 'times_borrowed'])
    writer.writeheader()
    writer.writerows(book_list)

    csv_fd_lender = open('lenders.csv', 'w')
    writer = csv.DictWriter(csv_fd_lender, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty'])
    writer.writeheader()
    writer.writerows(lender_list)
    

def pay_penalty(lender_id):
    csv_fd_lender = open('lenders.csv', 'r')
    lender_list = list(csv.DictReader(csv_fd_lender))

    for lender in lender_list:
        if lender['unique_id'] == lender_id:
            print(f"You currently owe ${lender['penalty']}. Please pay this amount now.")
            # Assume they pay it:
            lender['penalty'] = 0

    csv_fd_lender.close()

    csv_fd_lender = open('lenders.csv', 'w')
    writer = csv.DictWriter(csv_fd_lender, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty'])
    writer.writeheader()
    writer.writerows(lender_list)


if __name__ == "__main__":
    pass

    # get_lenders()
    # get_books()
    # borrow_book('6', '1553')
    # modify_book_count('1553', 3, True)
    # return_book('6')
    # pay_penalty('6')


    # lender_1 = Lender(1, 'Bob', '43', datetime.date(2020, 4, 2), 0)
    # book_1 = Book(7,'Hatchet','Stillman',4,1)
    # # lender_1.print_()
    # lenders = get_lenders()
    # for i in lenders:
    #     i.print_() # all this works 


    # book = get_books()
    # for i in book:
    #     i.print_() # works 
    # add_book(book_1)
    # remove_book(str(7))
    # # add_lender(lender_1) #works
    # # remove_lender(str(3)) #works 



