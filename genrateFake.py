from faker import Faker
import random
from DB import *

fake = Faker()

# Generate fake data for a Book
def generate_fake_book():
    title = fake.sentence(nb_words=3)
    author = fake.name()
    publication_year = fake.year()
    copies_available = random.randint(1, 20)
    total_copies = copies_available 
    num_pages = random.randint(50, 500)
    genre = fake.word()
    price = round(random.uniform(5, 50), 2)
    
    return Book(title, author, publication_year, copies_available, total_copies, num_pages, genre, price)

# Generate fake data for a Magazine
def generate_fake_magazine():
    title = fake.sentence(nb_words=3)
    author = fake.name()
    publication_year = fake.year()
    copies_available = random.randint(1, 15)
    total_copies = copies_available 
    issue_num = random.randint(1, 12)
    frequency = fake.word()
    price = round(random.uniform(5, 50), 2)
    
    return Magazine(title, author, publication_year, copies_available, total_copies, issue_num, frequency, price)

# Generate fake data for a Journal
def generate_fake_journal():
    title = fake.sentence(nb_words=3)
    author = fake.name()
    publication_year = fake.year()
    copies_available = random.randint(1, 20)
    total_copies = copies_available
    issue = random.randint(1, 100)
    
    return Journal(title, author, publication_year, copies_available, total_copies, issue)

# main function
def main():
    # Connect to the SQLite database file
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Define your classes and generate fake data (assuming you have already defined the classes and generated fake data)

    # generate 10 fake data for a Book , Magazine and Journal and insert them into the database
    for i in range(10):
        book = generate_fake_book()
        book.insert_into_database(cursor)
        magazine = generate_fake_magazine()
        magazine.insert_into_database(cursor)
        journal = generate_fake_journal()
        journal.insert_into_database(cursor)

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()