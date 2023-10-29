import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        reader1 = BookLover("rachel","rach@gmail.com","Horror")
        reader1.add_book("Dune",3)
        self.assertIn("Dune", reader1.book_list['book_name'].values)
    def test_2_add_book(self):
        reader2 = BookLover("Rosie","rosie@gmail.com","scifi")
        firstadd = reader2.add_book("Bones and All",4)
        secondadd = reader2.add_book("Bones and All",4)
        count = reader2.book_list['book_name'].value_counts()["Bones and All"]
        self.assertEqual(count,1)
    def test_3_has_read(self): 
        reader3 = BookLover("Jill","jill@gmail.com","Adventure")
        reader3.add_book("Indiana Jones",5)
        self.assertTrue(reader3.has_read("Indiana Jones"))
    def test_4_has_read(self): 
        reader4 = BookLover("Jack","jack@gmail.com","Fantasy")
        reader4.add_book("Game of Thrones",3)
        self.assertFalse(reader4.has_read("Indiana Jones"))
    def test_5_num_books_read(self): 
        reader5 = BookLover("James","james@gmail.com","Historical Fiction")
        reader5.add_book("Dune",4)
        reader5.add_book("Dracula",2)
        reader5.add_book("Gone with the wind",5)
        expected = 3
        self.assertEqual(expected,reader5.num_books_read())
    def test_6_fav_books(self):
        reader6 = BookLover("Alex","alex@gmail.com","Romance")
        reader6.add_book("Dune",2)
        reader6.add_book("The Notebook",5)
        reader6.add_book("Gone with the wind",5)
        reader6.add_book("Game of Thrones",3)
        df = reader6.fav_books()
        result = df.book_rating
        self.assertTrue((df['book_rating'] > 3).all())

if __name__ == '__main__':

    unittest.main(verbosity=3)
    
