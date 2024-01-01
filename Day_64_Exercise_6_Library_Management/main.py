# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesn't persist the books after the program is stopped!
class Library():
  def __init__(self):
    self.__books = [] #stores total books
    self.__no_of_books = 0

  @property
  def get_books(self):
    if self.__books:
      book_names = [name["Name"] for name in self.__books]
      return ', '.join(book_names)
    else:
      print("No books in library")

  @property
  def total_books(self):
    return self.__no_of_books

  @get_books.setter
  def addBook(self, book_dict):
    self.__books.append(book_dict)
    self.__no_of_books += 1
    print(f"Successfully added {book} book to library")


bookShelf = Library()
exit_code =['quit','exit','0']
while True:
  book = input("Enter the book name: ")
  if book in exit_code:
    break
  author = input(f"Enter the name of the author of {book} book: ")
  bookShelf.addBook = {'Name': book,'Author':author}
