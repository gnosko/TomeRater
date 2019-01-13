# TomeRater - An application that allows users to read and rate books.
# Written by Aaron Siller, January 2019

# Class definitions:
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, email):
        self.email = email
        print("The email address for {user} has been updated to: {email}".format(email))

    def __repr__(self):
        return "User: " + self.name + " - " + self.email + " (books read: " + str(len(self.books)) + ")"

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
        
    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        ratings_total = 0
        number_of_ratings = 0
        for key in self.books:
            if self.books[key] != None:
                ratings_total += self.books[key]
                number_of_ratings += 1
        return ratings_total / number_of_ratings
    
    def __hash__(self):
        return hash((self.name, self.email))

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn
        
    def set_isbn(self, isbn):
        self.isbn = isbn
        return self.title + " ISBN number was set to: " + str(self.isbn)

    def add_rating(self, rating):
        if rating < 0 or rating > 4:
            print("Invalid Rating")
            return False
        self.ratings.append(rating)
        
    def __repr__(self):
        return self.title + " - ISBN " + str(self.isbn)
        
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
    
    def get_average_rating(self):
        ratings_total = 0
        for rating in self.ratings:
            ratings_total += rating
        return ratings_total / len(self.ratings)
    
    def __hash__(self):
        return hash((self.title, self.isbn))
        
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)
        
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        for book in self.books:
            if isbn == book.get_isbn():
                print("A book with the supplied ISBN already exists!")
                return False
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        for book in self.books:
            if isbn == book.get_isbn():
                print("A book with the supplied ISBN already exists!")
                return False
        return Fiction(title, author, isbn)
        
    def create_non_fiction(self, title, subject, level, isbn):
        for book in self.books:
            if isbn == book.get_isbn():
                print("A book with the supplied ISBN already exists!")
                return False
        return Non_Fiction(title, subject, level, isbn)
        
    def add_book_to_user(self, book, email, rating=None):
        # Error: check if user has not been added
        if email not in self.users:
            print("No user with email {email}!".format(email=email))
            return False
        
        # Add book to user
        self.users[email].read_book(book, rating)
        
        # Add user's rating
        if rating is not None:
            book.add_rating(rating)
        
        # Increase book's read count
        if book not in self.books:
            # Add book with read count 1 if not in list
            self.books[book] = 1
        else:
            # Increase book's read count
            self.books[book] += 1
        
    def add_user(self, name, email, user_books=None):
        # Error: check for valid email address
        if "@" not in email:
            print("User account was NOT created because an invalid email address was supplied!")
            return False
            
        # Error: check if user has already been added
        if email in self.users:
            print("User {} already exists!".format(email))
            return False
            
        # Add new user
        self.users[email] = User(name, email)
        print("User {} has been created.".format(email))
        
        # Add books to user if necessary
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)
    
    def print_catalog(self):
        for book in self.books:
            print(book.title)
    
    def print_users(self):
        for user in self.users:
            print(user)
    
    def most_read_book(self):
        # Determine highest read count
        max_reads = max(self.books.values())
        # Create list of books in self.books that hold the highest read count (could be multiple books)
        most_read_book = [book for book, reads in self.books.items() if reads == max_reads]
        # Print list
        print("{} is the most read at {} times.".format(most_read_book, max_reads))
    
    def highest_rated_book(self):
        # Create dict of Books and rating averages
        book_average_ratings = {}
        for book in self.books: 
            book_average_ratings[book] = book.get_average_rating()
        
        # Determine highest rating value
        highest_rating = max(book_average_ratings.values())
        
        # Create list of books that hold the highest rating
        highest_rated_book = [book for book, rating in book_average_ratings.items() if rating == highest_rating]
        
        # Print list
        print("{} holds the highest rating at {}".format(highest_rated_book, highest_rating))
    
    def most_positive_user(self):
        # Create dict of Users and rating averages
        user_average_ratings = {}
        for user in self.users.values(): 
            user_average_ratings[user] = user.get_average_rating()
        
        # Determine highest average rating value
        highest_rating = max(user_average_ratings.values())
        
        # Create list of users that hold the highest average rating
        most_positive_user = [user for user, rating in user_average_ratings.items() if rating == highest_rating]
        
        # Print list
        print("{} is the most positive user leaving a highest average rating of {}".format(most_positive_user, highest_rating))





# Debug Tests:
# Test Users
'''
owen = User("Owen", "owen@test.com")
simon = User("Simon", "simon@test.com")
'''
#Test Books, Fiction, Non_Fiction
'''
#white_fang = Book("White Fang", 9781858137407)
#merriam = Book("Merriam-Webster's Dictionary of English Usage", 9780877791324)
white_fang = Fiction("White Fang", "Jack London", 9781858137407)
merriam = Non_Fiction("Merriam-Webster's Dictionary of English Usage", "English Language", "advanced", 9780877791324)
'''
# Test user actions
'''
owen.read_book(white_fang, 4)
simon.read_book(white_fang)
owen.read_book(merriam, 1)
simon.read_book(merriam, 4)
#print(owen.books, simon.books)
print(owen.get_average_rating(), simon.get_average_rating())
'''
# Test TomeRater class
'''
Tome_Rater = TomeRater()
book1 = Tome_Rater.create_book("The Jewish Centaur", 9781625646248)
novel1 = Tome_Rater.create_novel("The Brothers Karamazov", "Fyodor Dostoevsky", 9780374528379)
nonfiction1 = Tome_Rater.create_non_fiction("I'm Just Here for the Food: Food + Heat = Cooking", "Cooking", "beginner", 9781584790839)
#print(book1, novel1, nonfiction1)
Tome_Rater.add_user("Eliana", "eliana@test.com")
Tome_Rater.add_user("Owen", "owen@test.com")
Tome_Rater.add_user("Simon", "simon@test.com", user_books=[book1, novel1, nonfiction1])
#Tome_Rater.add_user("Eliana", "eliana@test.com")
print(Tome_Rater.users)
Tome_Rater.add_book_to_user(book1, "eliana@test.com", 2)
Tome_Rater.add_book_to_user(book1, "owen@test.com", 4)
Tome_Rater.add_book_to_user(novel1, "eliana@test.com")
Tome_Rater.add_book_to_user(novel1, "owen@test.com", 3)
print("\n")
print(Tome_Rater.users)
print("\n")
print(Tome_Rater.books)
print("\nRatings for:\n  {title} - {ratings}".format(title=book1.title, ratings=book1.ratings))
print("Ratings for:\n  {title} - {ratings}".format(title=novel1.title, ratings=novel1.ratings))
print("Ratings for:\n  {title} - {ratings}".format(title=nonfiction1.title, ratings=nonfiction1.ratings))
'''

# Analysis method tests were preformed using popluate.py
