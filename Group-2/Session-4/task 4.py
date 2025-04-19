    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book["title"].lower()]

    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book["author"].lower()]