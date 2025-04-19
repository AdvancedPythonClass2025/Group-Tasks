
import json
import os

class Library:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = []
        self.load_books()
def save_books(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.books, file, ensure_ascii=False, indent=4)

def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book["title"].lower()]

    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book["author"].lower()]
