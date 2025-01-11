class Ebook():
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.is_open = False
        self.current_page = 1


    def open_a_book(self):
        self.is_open = True

    def close_a_book(self):
        self.is_open = False

    def trun_the_page(self):
        if self.is_open:
            self.current_page += 1
        else:
            print("The book is closed")
    
    def book_status(self):
        if self.is_open:
            print(f"The book is opened. You are on the {self.current_page} out of {self.number_of_pages}")
        else:
            print("The book is closed")






def main():
    book = Ebook("Bible", "Unknown", 7777)

    
    book.book_status()

    book.open_a_book()

    book.book_status()

    book.trun_the_page()
    book.trun_the_page()
    book.trun_the_page()
    book.trun_the_page()

    book.book_status()

    book.close_a_book()

    book.book_status()

if __name__ == "__main__":
    main()














# Each book has a title, author, number of pages and the current page number that is currently being read. It is possible to open a book - then we can read it. If a book is open, it is possible to go to the next or previous page.