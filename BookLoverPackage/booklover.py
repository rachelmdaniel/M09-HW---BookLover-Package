import pandas as pd

class BookLover:
    def __init__(self,name,email,fav_genre):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        self.num_books = 0
    def add_book(self,book_name,book_rating):
        if book_name in self.book_list['book_name'].values:
            return "Book already exists"
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)  
            self.num_books += 1
    def has_read(self,book_name):
        if book_name in self.book_list['book_name'].values:
            return True
        else:
            return False
    def num_books_read(self):
        return len(self.book_list)
    def fav_books(self):
        return self.book_list[self.book_list.book_rating > 3]
                                     
        
if __name__ == '__main__':

    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
