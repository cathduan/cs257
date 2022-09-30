#!/usr/bin/env python3
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
        self.bookObjectList = []
        
        # Adds all lines in the file to a list
        with open(books_csv_file_name) as file:
            for line in file:
                fileLines.append(line.rstrip()) 
            file.close()

       # can combine this with the code above. 
        for i in range(len(fileLines)):
            fileLines[i] = fileLines[i].split(",")
        
        # Accounts for book titles that include commas
        for i in range(len(fileLines)):
            
            if len(fileLines[i]) > 3:
                fileLines[i] = fileLines[i][0].replace("\"", "") + "," + fileLines[i][1].replace("\"", ""), fileLines[i][2], fileLines[i][3]   
        
        for list in fileLines:
            self.authorsList.append(list[2])
            self.titleList.append(list[0])
            self.yearList.append(list[1])
            
        
        
        self.authorObjectList = []
        # Creates Author and Book objects
        for i in range(len(self.authorsList)):
            authorSplitLines = self.authorsList[i].split(" ")
            if len(authorSplitLines) == 3:  #Case 1: if the author is the only author and has no middle name
                date = authorSplitLines[2].split("-")
                date[0] = date[0].replace("(", "")
                date[-1] = date[-1].replace(")", "")
                if date[-1] == "": # if there is no death year, set to None
                    date[-1] = None
    
                a = Author(authorSplitLines[1], authorSplitLines[0], date[0], date[-1])
                if a not in self.authorObjectList:
                    self.authorObjectList.append(a)
                b = Book(self.titleList[i], self.yearList[i], [a])
                self.bookObjectList.append(b)
                
            elif len(authorSplitLines) == 4: #Case 2: if the author has a middle name
                date = authorSplitLines[3].split("-")
                date[0] = date[0].replace("(", "")
                date[-1] = date[-1].replace(")", "")
                if date[-1] == "":
                    date[-1] = None

                a = Author(authorSplitLines[2], authorSplitLines[0] + " " + authorSplitLines[1], date[0], date[-1])
                if a not in self.authorObjectList:
                    self.authorObjectList.append(a)
                b = Book(self.titleList[i], self.yearList[i], [a])
                self.bookObjectList.append(b)
                
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
                b = Book(self.titleList[i], self.yearList[i], [a1, a2])
                self.bookObjectList.append(b)
        
        

    def authors(self, search_text=None):
        ''' Returns a list of all the Author objects in this data source whose names contain
            (case-insensitively) the search text. If search_text is None, then this method
            returns all of the Author objects. In either case, the returned list is sorted
            by surname, breaking ties using given name (e.g. Ann Brontë comes before Charlotte Brontë).
        '''
        authorList = []
        resultAuthorList = []
        for author_object in range(0, len(self.authorObjectList)):
            given_name = (self.authorObjectList[author_object].given_name)
            surname = (self.authorObjectList[author_object].surname)
            authorList.append((surname, given_name, author_object))
      
        
        if search_text == None:
            for author in sorted(authorList):
                resultAuthorList.append([self.authorObjectList[author[2]].given_name, self.authorObjectList[author[2]].surname])
        else:
            for author in sorted(authorList):
                full_name = self.authorObjectList[author[2]].given_name + " " + self.authorObjectList[author[2]].surname
                if (search_text.lower()) in author[0].lower() or (search_text.lower()) in author[1].lower():
                    resultAuthorList.append([self.authorObjectList[author[2]].given_name, self.authorObjectList[author[2]].surname])
                elif (search_text.lower() in full_name.lower()):
                    resultAuthorList.append([self.authorObjectList[author[2]].given_name, self.authorObjectList[author[2]].surname])
                   
        return resultAuthorList


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
        bookList = []
        resultBookList = []
        for book_object in range(0, len(self.bookObjectList)):
            title = (self.bookObjectList[book_object].title)
            year = (self.bookObjectList[book_object].publication_year)
            bookList.append((title, year, book_object))
            
        yearSortList = sorted(bookList, key=lambda x:x[1])
        
        if search_text == None:
            if sort_by == "title" or sort_by != "year":
                for book in sorted(bookList):
                    resultBookList.append([self.bookObjectList[book[2]].title, self.bookObjectList[book[2]].publication_year])
               
            elif sort_by == "year":
                for book in yearSortList:
                    resultBookList.append([self.bookObjectList[book[2]].title, self.bookObjectList[book[2]].publication_year])
               
        else:
            if sort_by == "title" or sort_by != "year":
                for book in sorted(bookList):
                    if (search_text.lower()) in book[0].lower():
                        resultBookList.append([self.bookObjectList[book[2]].title, self.bookObjectList[book[2]].publication_year])
            elif sort_by == "year":
                for book in yearSortList:
                    if (search_text.lower()) in book[0].lower():
                        resultBookList.append([self.bookObjectList[book[2]].title, self.bookObjectList[book[2]].publication_year])
               
        return resultBookList
                        
 

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

        bookList = []
        resultBookList = []
        for book_object in range(0, len(self.bookObjectList)):
            year = (self.bookObjectList[book_object].publication_year)
            title = (self.bookObjectList[book_object].title)
            bookList.append((title, year, book_object))
        
        yearSortList = sorted(bookList, key=lambda x:x[1])
        
        if start_year == None and end_year == None:
            for book in yearSortList:
                resultBookList.append([self.bookObjectList[book[2]].title, self.bookObjectList[book[2]].publication_year])
                
        elif start_year != None and end_year == None:
            for book in yearSortList:
                if int(book[1]) >= start_year:
                    resultBookList.append([self.bookObjectList[book[2]].title, self.bookObjectList[book[2]].publication_year])
               
        elif start_year == None and end_year != None:
            for book in yearSortList:
                if int(book[1]) <= end_year:
                    resultBookList.append([self.bookObjectList[book[2]].title, self.bookObjectList[book[2]].publication_year])
        return resultBookList
    
def main():
    #get command-line arguments
    #Testing all default cases:
    data_source = BooksDataSource("books1.csv")
    print("Testing the authors method: ", data_source.authors())
    print("------------------------------------------------------------------------------------")
    print("Testing the books method: ", data_source.books(None, ""))
    print("------------------------------------------------------------------------------------")
    print("Testing the books_between_years method: ", data_source.books_between_years(None, None))

if __name__ == '__main__':
    main()
    