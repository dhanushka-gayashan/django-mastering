class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return '"{}" was written by {} and it has {} pages'.format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print('"{}" has been destroyed'.format(self.title))


my_book = Book('Black Magick', 'Finn Bin', 1500)

print(my_book)
print(len(my_book))

del my_book

