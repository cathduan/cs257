'''
   booksdatasourcetest.py
   Jeff Ondich, 24 September 2021
   Authors: Cathy Duan and Ali Ramazani
'''

from booksdatasource import Author, Book, BooksDataSource
import unittest

class BooksDataSourceTester(unittest.TestCase):
    def setUp(self):
        self.data_source = BooksDataSource('books1.csv')

    def tearDown(self):
        pass

    #Checks to see whether an author's name is unique in the csv file
    def test_unique_author(self):
        authors = self.data_source.authors('Pratchett')
        self.assertTrue(len(authors) == 1)
        self.assertTrue(authors[0] == Author('Pratchett', 'Terry'))

    #Checks to see whether a book title is unique in the csv file
    def test_unique_title(self):
        titles = self.data_source.titles("Emma")
        self.assertTrue(len(titles) == 1)
        self.assertTrue(titles[0] == Book("Emma"))
    
    #Checks whether all the books are present in the csv file
    def test_all_books(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books()
        self.assertTrue(len(books) == 3)
        self.assertTrue(books[0].title == 'Emma')
        self.assertTrue(books[1].title == 'Neverwhere')
        self.assertTrue(books[2].title == 'Omoo')
        
    #Checks for the valid year by excluding negative numbers
    def test_negative_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books()
        self.assertFalse(books[0].year < 0)
        self.assertFalse(books[1].year < 0)
        self.assertFalse(books[2].year < 0)
    
    #Checks whether the given publication year contains only 4 digits
    def test_publication_year_length(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books()
        self.assertTrue(len(books[0]).year == 4)
        self.assertTrue(len(books[1]).year == 4)
        self.assertTrue(len(books[2]).year == 4)
    
    #Checks to see whether a given publication year is not in the csv file
    def test_invalid_publication_year(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books()
        invalidYear = 1975
        self.assertFalse((books[0]).year == invalidYear)
        self.assertFalse((books[1]).year == invalidYear)
        self.assertFalse((books[2]).year == invalidYear)
    
    #Checks if a title does not exist in the csv file
    def test_invalid_titles(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        books = tiny_data_source.books()
        invalidTitle = "Harry Potter"
        self.assertFalse((books[0]).title == invalidTitle)
        self.assertFalse((books[1]).title == invalidTitle)
        self.assertFalse((books[2]).title == invalidTitle)
    
    #Check if an author name does not exist in the csv file
    def test_invalid_authors(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        authors = tiny_data_source.authors()
        invalidAuthor = "J.K. Rowling"
        self.assertFalse((authors[0]) == invalidAuthor)
        self.assertFalse((authors[1]) == invalidAuthor)
        self.assertFalse((authors[2]) == invalidAuthor)

    #Check to see whether the amount of how many times a certain author is in the list is counted correctly
    def test_author_appearance(self): 
        authors = self.data_source.authors()
        count = 0
        for author in authors():
            if author == "Jane Austen":
                count = count + 1
        self.assertTrue(count == 3)

    #Check to see whether the amount of how many times a certain year is in the list is counted correctly
    def test_year_appearance(self):
        books = self.data_source.books()
        count = 0
        for book in books():
            if book.publication_year == 1934:
                count = count + 1
        self.assertTrue(count == 2)
    
    def test_line_contents(self):
        pass
        
    #Checks to see whether a title list is alphabetically sorted correctly
    def test_title_alphabet_sort(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        title = tiny_data_source.books.title()
        sortedTitle = title.sort()
        self.assertTrue(sortedTitle[0] == title[2])
        self.assertTrue(sortedTitle[1] == title[1])
        self.assertTrue(sortedTitle[2] == title[0])

    #Checks to see whether a year list is numerical sorted correctly
    def test_year_numeric_sort(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        years = tiny_data_source.books.publication_year()
        sortedYears = years.sorted()
        self.assertTrue(sortedYears[0] == years[2])
        self.assertTrue(sortedYears[1] == years[0])
        self.assertTrue(sortedYears[2] == years[1])

    #Checks to see whether an author list is alphabetically sorted correctly
    def test_author_alphabet_sort(self):
        tiny_data_source = BooksDataSource('tinybooks.csv')
        authors = tiny_data_source.authors()
        sortedAuthors = authors.sort()
        self.assertTrue(sortedAuthors[0] == authors[0])
        self.assertTrue(sortedAuthors[1] == authors[2])
        self.assertTrue(sortedAuthors[2] == authors[1])

        #self.assertEqual(sortedAuthors, [authors[2], authors[0], authors[1]]) another potential way to write lines 115-117
        

if __name__ == '__main__':
    unittest.main()

