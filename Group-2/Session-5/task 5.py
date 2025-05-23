def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.books, file, ensure_ascii=False, indent=4)
                
def add_book(self, title, author, year):
        book = {
           "title": title,
           "author": author,
            "year" : year
        }        
        self.books.append(book)
        self.save_books()

        
def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book["title"].lower()]

    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book["author"].lower()]
