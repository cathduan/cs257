
'''
    booksdatasource.py
    Jeff Ondich, 21 September 2022
    Authors: Cathy Duan, Ali Ramazani
    For use in the "books" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2022.
'''

import csv
from unittest import result

class Author:
    def __init__(self, surname='', given_name='', birth_year=None, death_year=None, books = []):
        self.surname = surname
        self.given_name = given_name
        self.birth_year = birth_year
        self.death_year = death_year
        self.books = books

    def __eq__(self, other):
        ''' For simplicity, we're going to assume that no two authors have the same name. '''
        return self.surname == other.surname and self.given_name == other.given_name

class Book:
    def __init__(self, title='', publication_year=None, authors=[]):
        ''' Note that the self.authors instance variable is a list of
            references to Author objects. '''
        self.title = title
        self.publication_year = publication_year
        self.authors = authors

    def __eq__(self, other):
        ''' We're going to make the excessively simplifying assumption that
            no two books have the same title, so "same title" is the same
            thing as "same book". '''
        return self.title == other.title

class BooksDataSource:
    def __init__(self, books_csv_file_name):
        ''' The books CSV file format looks like this:

                title,publication_year,author_description

            For example:

                All Clear,2010,Connie Willis (1945-)
                "Right Ho, Jeeves",1934,Pelham Grenville Wodehouse (1881-1975)

            This __init__ method parses the specified CSV file and creates
            suitable instance variables for the BooksDataSource object containing
            a collection of Author objects and a collection of Book objects.
        '''
       
       # Adds lines of a file into a list
        fileLines = []
        self.csv_file = books_csv_file_name
        self.fileLines = []
        self.authorsList = []
        self.titleList = []
        self.yearList = []
        self.bookList = []
        
        with open(books_csv_file_name) as file:
            for line in file:
                fileLines.append(line.rstrip()) 
            file.close()

       # can combine this with the code above. 
        for i in range(len(fileLines)):
            fileLines[i] = fileLines[i].split(",")
        
        #Accounts for book titles that include commas
        for i in range(len(fileLines)):
            if len(fileLines[i]) > 3:
                fileLines[i] = fileLines[i][0] + "," + fileLines[i][1], fileLines[i][2], fileLines[i][3]   
        
        for list in fileLines:
            self.authorsList.append(list[2])
            self.titleList.append(list[0])
            self.yearList.append(list[1])
            
        
        
        for i in range(len(fileLines)):
            #if authors exist, don't create a new author object?? just add it to the existing author object
            b = Book(self.titleList[i], self.yearList[i], self.authorsList[i])
            self.bookList.append(b)
        
        
        self.authorObjectList = []
        # To create the author objects
        for author in self.authorsList:
            authorSplitLines = author.split(" ")
            if len(authorSplitLines) == 3:  #Case 1: if the author is the only author and has no middle name
                date = authorSplitLines[2].split("-")
                date[0] = date[0].replace("(", "")
                date[-1] = date[-1].replace(")", "")
                if date[-1] == "": # if there is no death year, set to None
                    date[-1] = None
    
                a = Author(authorSplitLines[1], authorSplitLines[0], date[0], date[-1])
                if a not in self.authorObjectList:
                    self.authorObjectList.append(a)
                
            elif len(authorSplitLines) == 4: #Case 2: if the author has a middle name
                date = authorSplitLines[3].split("-")
                date[0] = date[0].replace("(", "")
                date[-1] = date[-1].replace(")", "")
                if date[-1] == "":
                    date[-1] = None

                a = Author(authorSplitLines[2], authorSplitLines[0] + " " + authorSplitLines[1], date[0], date[-1])
                if a not in self.authorObjectList:
                    self.authorObjectList.append(a)
                
            elif len(authorSplitLines) > 4: #Case 3: if there are multiple authors, then parse each one individually
                authorSplitLines = " ".join(authorSplitLines) # join the split strings
                authorSplitLines = authorSplitLines.split("and")
                author1, author2 = authorSplitLines[0].split(" "), authorSplitLines[1].split(" ")
                author1.remove(author1[3]) # accounts for the extra space that shifts the indexes
                author2.remove(author2[0]) # accounts for the extra space that shifts the indexes
                
                date1, date2 = author1[2].split("-"), author2[2].split("-") 
                date1[0], date2[0] = date1[0].replace("(", ""), date2[0].replace("(", "")
                date1[-1], date2[-1] = date1[-1].replace(")", ""), date2[-1].replace(")", "")
                if date1[-1] == "":
                        date1[-1] = None
                if date2[-1] == "":
                    date2[-1] = None

                a1 = Author(author1[1], author1[0], date1[0], date1[-1])
                a2 = Author(author2[1], author2[0], date2[0], date2[-1]) 
                if a1 not in self.authorObjectList:
                    self.authorObjectList.append(a1)
                if a2 not in self.authorObjectList:
                    self.authorObjectList.append(a2)
                
        lst = []
        for i in range(0, len(self.authorObjectList)):
            given_name = (self.authorObjectList[i].given_name)
            surname = (self.authorObjectList[i].surname)
            birth = (self.authorObjectList[i].birth_year)
            death = (self.authorObjectList[i].death_year)
            lst.append(given_name)
            lst.append(surname)
            lst.append(birth)
            lst.append(death)
        print(lst)
            
    
        

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        # print(self.bookList.author)
        # book = BooksDataSource("books1.csv")
        # authorsList = book.authors
        # sortedAuthorList = authorsList.sorted()
        # print(sortedAuthorList)
        resultAuthorList = []
        
        if search_text == None:
            return sorted(self.authorObjectList.surname)
        else:
            for author in self.authorsList:
                if  (search_text.lower()) in author.lower() : #== search_text.lower():
                    resultAuthorList.append(author)
        #lol need to figure out how to incorporate the author objects haha
        return sorted(resultAuthorList)

    def books(self, search_text=None, sort_by='title'):
        ''' Returns a list of all the Book objects in this data source whose
            titles contain (case-insensitively) search_text. If search_text is None,
            then this method returns all of the books objects.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                'title' -- sorts by (case-insensitive) title, breaking ties with publication_year
                default -- same as 'title' (that is, if sort_by is anything other than 'year'
                            or 'title', just do the same thing you would do for 'title')
        '''
        book1 = BooksDataSource("books1.csv")
        bookList = book1.bookList
        resultBookList = []
        
        if search_text == None:
            return sorted(self.bookList)
        else:
            for book in self.bookList:
                if book.lower() == search_text.lower():
                    resultBookList.append(book.title) # still need to do the sorting
    
        if sort_by == "title":
            resultBookList.sorted()
        elif sort_by == "year":
            pass
            
            
        return sorted(resultBookList)
    
        #return []

    def books_between_years(self, start_year=None, end_year=None):
        ''' Returns a list of all the Book objects in this data source whose publication
            years are between start_year and end_year, inclusive. The list is sorted
            by publication year, breaking ties by title (e.g. Neverwhere 1996 should
            come before Thief of Time 1996).

            If start_year is None, then any book published before or during end_year
            should be included. If end_year is None, then any book published after or
            during start_year should be included. If both are None, then all books
            should be included.
        '''






        return []
    
def main():
    #get command-line arguments
    data_source = BooksDataSource("books1.csv")
    print(len(data_source.authors()))
    '''
    if user wants book by searchstring:
        books = data_source.books(searchstring)
        print books
    elif ...
    '''

if __name__ == '__main__':
    main()
    