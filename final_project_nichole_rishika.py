# 2 classes, lender and book
# csv file storing both, separately
# new function for every action 
# 3 more functions at end 

import random 
import csv 
from datetime import date

class Lender(): # Nichole
    def __init__(self, unique_id, name, book_id, date, penalty, age):

        self.unique_id = unique_id
        self.name = name
        self.book_id = book_id
        self.date = date
        self.penalty = penalty 
        self.age = age


    def print_lender(self):
        print("The parameters of the lender are: ")
        print(f"Unique ID: {self.unique_id}")
        print(f"Name: {self.name}")
        print(f"Book ID: {self.book_id}")
        print(f"Date: {self.date}")
        print(f"Penalty: {self.penalty}")
        print(f"Age: {self.age}")
        print("============")

class Book(): # Nichole
    def __init__(self, unique_id, title, author, copies, times_borrowed, rating):

        self.unique_id = unique_id
        self.title = title
        self.author = author
        self.copies = copies
        self.times_borrowed = times_borrowed
        self.rating = rating


    def print_book(self):
        print("The parameters of the book are: ")
        print(f"Unique ID: {self.unique_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Copies: {self.copies}")
        print(f"times_borrowed: {self.times_borrowed}")
        print(f"Rating: {self.rating}")
        print("============")

def get_lenders(): # Nichole
    lender_list = []
    lender_listofdicts = []
    name_list = ['Rishika', 'Nichole', 'Alejandro', 'Doyin', 'Ron', 'Ananya', 'Chris', 'Selma', 'Jordan', 'Joy']

    csv_fd = open("lenders.csv", 'w')

    csv_writer = csv.DictWriter(csv_fd, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty', 'age'])
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
        age = random.randint(10, 85)
        
        lender_dict["name"] = name
        lender_dict["unique_id"] = unique_id
        lender_dict["book_id"] = book_id
        lender_dict["date"] = date
        lender_dict["penalty"] = penalty 
        lender_dict["age"] = age

        lender_listofdicts.append(lender_dict)

        lender_1 = Lender(unique_id, name, book_id, date, penalty, age) 
        
        lender_list.append(lender_1)

    csv_writer.writerows(lender_listofdicts)

    return lender_list


def get_books(): # Nichole
    book_list = []
    book_listofdicts = []
    title_list = ['Beloved', 'Great Gatsby', 'Catcher in the Rye', 'To Kill a Mockingbird', 
    'Lord of the Rings', 'Untamed', 'Hatchet', 'Gone With The Wind', 'Goodnight Moon', 'Little Women']
    author_list = ['Jones', 'Robins', 'Noel', 'Obama', 'Smith', 'Zha', 'Stillman', 'Marchuck', 'Seewald', 'Pomahac']
    rating_list = ['18+', '16+', 'N/A']

    csv_fd = open("books.csv", 'w')

    csv_writer = csv.DictWriter(csv_fd, fieldnames = ['unique_id', 'title', 'author', 'copies', 'times_borrowed', 'rating'])
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
        rating = rating_list[random.randint(0,2)]
        
        book_dict["unique_id"] = unique_id
        book_dict["title"] = title
        book_dict["author"] = author
        book_dict["copies"] = copies
        book_dict["times_borrowed"] = times_borrowed
        book_dict["rating"] = rating

        book_listofdicts.append(book_dict)

        book_1 = Book(unique_id, title, author, copies, times_borrowed, rating) 
        
        book_list.append(book_1)

    csv_writer.writerows(book_listofdicts)

    return book_list

def add_lender(lender): # Nichole
    csv_fd = open("lenders.csv", 'a')
    csv_writer = csv.DictWriter(csv_fd, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty', 'age'])

    lender_dict = {}

    lender_dict["name"] = lender.name
    lender_dict["unique_id"] = lender.unique_id
    lender_dict["book_id"] = lender.book_id
    lender_dict["date"] = lender.date
    lender_dict["penalty"] = lender.penalty 
    lender_dict["age"] = lender.age 

    csv_writer.writerow(lender_dict)

def remove_lender(remove_id): # Nichole
    lines = list() 
    with open('lenders.csv', 'r') as read_file:
        reader = csv.DictReader(read_file)

        for row in reader:
            if row['unique_id'] != remove_id:
                lines.append(row) 
                

    with open('lenders.csv', 'w') as write_file:
        writer = csv.DictWriter(write_file, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty', 'age'])
        writer.writeheader()
        writer.writerows(lines)

def add_book(book): # Nichole
    csv_fd = open("books.csv", 'a')
    csv_writer = csv.DictWriter(csv_fd, fieldnames = ['unique_id', 'title', 'author', 'copies', 'times_borrowed', 'rating'])

    book_dict = {}

    book_dict["unique_id"] = book.unique_id
    book_dict["title"] = book.title
    book_dict["author"] = book.author
    book_dict["copies"] = book.copies
    book_dict["times_borrowed"] = book.times_borrowed 
    book_dict["rating"] = book.rating 

    csv_writer.writerow(book_dict)

def remove_book(remove_id): # Nichole
    lines = list() 
    with open('books.csv', 'r') as read_file:
        reader = csv.DictReader(read_file)

        for row in reader:
            if row['unique_id'] != remove_id:
                lines.append(row) 
                

    with open('books.csv', 'w') as write_file:
        writer = csv.DictWriter(write_file, fieldnames = ['unique_id', 'title', 'author', 'copies', 'times_borrowed', 'rating'])
        writer.writeheader()
        writer.writerows(lines)


def borrow_book(lender_id, book_id): # Rishika

    # Reading both csv files:
    csv_fd_book = open('books.csv', 'r')
    book_list = list(csv.DictReader(csv_fd_book))

    csv_fd_lender = open('lenders.csv', 'r')
    lender_list = list(csv.DictReader(csv_fd_lender))

    for book in book_list:

        # Finding the correct book:
        if book['unique_id'] == book_id:

            # Making sure there are enough copies:
            if int(return_copies(book_id)) > 0:

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
    writer = csv.DictWriter(csv_fd_book, fieldnames = ['unique_id', 'title', 'author', 'copies', 'times_borrowed', 'rating'])
    writer.writeheader()
    writer.writerows(book_list)

    csv_fd_lender = open('lenders.csv', 'w')
    writer = csv.DictWriter(csv_fd_lender, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty', 'age'])
    writer.writeheader()
    writer.writerows(lender_list)



def modify_book_count(book_id, number, increase): # Rishika

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
    writer = csv.DictWriter(csv_fd_book, fieldnames = ['unique_id', 'title', 'author', 'copies', 'times_borrowed', 'rating'])
    writer.writeheader()
    writer.writerows(book_list)

def return_book(lender_id): # Rishika

    # Reading both csv files:
    csv_fd_book = open('books.csv', 'r')
    book_list = list(csv.DictReader(csv_fd_book))

    csv_fd_lender = open('lenders.csv', 'r')
    lender_list = list(csv.DictReader(csv_fd_lender))

    for lender in lender_list:

        # Finding the correct lender:
        if lender['unique_id'] == lender_id:
            
            book_id = lender['book_id']
            if book_id != '':
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
    writer = csv.DictWriter(csv_fd_book, fieldnames = ['unique_id', 'title', 'author', 'copies', 'times_borrowed', 'rating'])
    writer.writeheader()
    writer.writerows(book_list)

    csv_fd_lender = open('lenders.csv', 'w')
    writer = csv.DictWriter(csv_fd_lender, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty', 'age'])
    writer.writeheader()
    writer.writerows(lender_list)
    

def pay_penalty(lender_id): # Rishika
    csv_fd_lender = open('lenders.csv', 'r')
    lender_list = list(csv.DictReader(csv_fd_lender))

    for lender in lender_list:
        if lender['unique_id'] == lender_id:
            print(f"You currently owe ${lender['penalty']}. Please pay this amount now.")
            # Assume they pay it:
            lender['penalty'] = 0

    csv_fd_lender.close()

    csv_fd_lender = open('lenders.csv', 'w')
    writer = csv.DictWriter(csv_fd_lender, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty', 'age'])
    writer.writeheader()
    writer.writerows(lender_list)

# new function #1:
# checks if a lender is allowed to borrow a book based on their age and number of copies
def check_to_borrow(lender_id, book_id): # Rishika

    # Reading both csv files:
    csv_fd_book = open('books.csv', 'r')
    book_list = list(csv.DictReader(csv_fd_book))

    csv_fd_lender = open('lenders.csv', 'r')
    lender_list = list(csv.DictReader(csv_fd_lender))
    allowed = False

    for lender in lender_list:
        if lender['unique_id'] == lender_id:
            for book in book_list:
                if book['unique_id'] == book_id:
                    age = lender['age']
                    rating = book['rating']

                    if rating == 'N/A':
                        allowed = True
                    elif rating == '18+' and int(age) > 18:
                        allowed = True
                    elif rating == '16+' and int(age) > 16:
                        allowed = True

                    if int(return_copies(book_id)) <= 0:
                        allowed = False

    if allowed:
        print("You can borrow the book!")
    else:
        print("No book for you!")

# new function #2:
# returns number of copies of a book:
def return_copies(book_id): # Rishika

    csv_fd_book = open('books.csv', 'r')
    book_list = list(csv.DictReader(csv_fd_book))

    for book in book_list:
        if book['unique_id'] == book_id:
            print(f"There are {book['copies']} copies of this book left.")
            return book['copies']

# new function #3:
# if the lender borrowed a book on the lucky day, penalty becomes 0
def lucky_day(lender_id): # Rishika

    csv_fd_lender = open('lenders.csv', 'r')
    lender_list = list(csv.DictReader(csv_fd_lender))
    lucky_day = date(2021, 5, 3)

    for lender in lender_list:
        if lender['unique_id'] == lender_id and lender['date'] != '':
                borrowed_date_list = lender['date'].split('-')
                borrowed_date = date(int(borrowed_date_list[0]), int(borrowed_date_list[1]), int(borrowed_date_list[2]))

                if borrowed_date == lucky_day:
                    lender['penalty'] = 0

    csv_fd_lender = open('lenders.csv', 'w')
    writer = csv.DictWriter(csv_fd_lender, fieldnames = ['unique_id', 'name', 'book_id', 'date', 'penalty', 'age'])
    writer.writeheader()
    writer.writerows(lender_list)
           
           



if __name__ == "__main__":
    pass

    # get_lenders()
    # get_books()
    # borrow_book('6', '1397')
    # modify_book_count('1584', 14, True)
    # return_book('6')
    # pay_penalty('6')


    # lender_1 = Lender(1, 'Bob', '43', date(2020, 4, 2), 0, 35)
    # book_1 = Book(7,'Hatchet','Stillman',4,1, '18+')
    # # lender_1.print_()
    # lenders = get_lenders()
    # for i in lenders:
    #     i.print_lender() # all this works 


    # book = get_books()
    # for i in book:
    #     i.print_book() # works 
    # add_book(book_1)
    # remove_book(str(7))
    # # add_lender(lender_1) #works
    # # remove_lender(str(3)) #works 

    # check_to_borrow('2', '1584')

    # return_copies('1584')
    # borrow_book('6', '1584')
    # lucky_day('6')
