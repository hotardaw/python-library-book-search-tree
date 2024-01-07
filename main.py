import csv
from BooksModule import Book
from TreeModule import TreeNode


class Main:

    def load_book_data(self, file_path):
        books = []
        with open(file_path, newline='', encoding='utf-8') as book_data:
            csv_reader = csv.reader(book_data)
            header = next(csv_reader)

            book_data = csv.DictReader(book_data, fieldnames=header)

            for row in book_data:
                bookID = int(row['bookID'])
                title = row['title']
                authors = row['authors']
                average_rating = float(row['average_rating'])
                isbn = row['isbn']
                isbn13 = row['isbn13']
                language_code = row['language_code']
                num_pages = int(row['num_pages'])
                ratings_count = int(row['ratings_count'])
                text_reviews_count = int(row['text_reviews_count'])
                publication_date_str = row['publication_date']
                publisher = row['publisher']

                book = Book(bookID, title, authors, average_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count, publication_date_str, publisher)
                books.append(book)
        return books

    def build_binary_tree(self, book_objects):
        root_node = None
        for book in book_objects:
            if root_node is None:
                root_node = TreeNode(book)
            else:
                root_node.insert(book, root_node)
        return root_node

    def inorder_traverse_and_print(self, node):
        if node is None:
            return
        self.inorder_traverse_and_print(node.leftChild)
        print(node.book)
        self.inorder_traverse_and_print(node.rightChild)

    # root_node = None


main_instance = Main()
file_path = 'books.csv'
book_objects = main_instance.load_book_data(file_path)
root_node_ = main_instance.build_binary_tree(book_objects)
main_instance.inorder_traverse_and_print(root_node_)
