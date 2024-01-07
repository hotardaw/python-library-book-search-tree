from datetime import datetime


class Book:

    def __init__(self, bookID: int, title: str, authors: str, average_rating: float, isbn: str, isbn13: str,
                 language_code: str, num_pages: int, ratings_count: int, text_reviews_count: int,
                 publication_date_str: str, publisher: str):
        self.bookID = bookID
        self.title = title
        self.authors = authors
        self.average_rating = average_rating
        self.isbn = isbn
        self.isbn13 = isbn13
        self.language_code = language_code
        self.num_pages = num_pages
        self.ratings_count = ratings_count
        self.text_reviews_count = text_reviews_count
        self.publication_date_str = publication_date_str
        #self.publication_date = datetime.strptime(publication_date_str, "%m/%d/%Y")
        self.publisher = publisher

    def __gt__(self, other):
        return self.title > other.title

    def __eq__(self, other):
        return self.title == other.title

    def __lt__(self, other):
        return self.title < other.title

    # "represent" fn, represents objs as str
    def __repr__(self):
        return f"BookTitles(title='{self.title}')"
        #return f"BookInfo(title='{self.title}', authors='{self.authors}', isbn={self.isbn})"