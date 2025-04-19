  def search_by_title(self, title):
        results = []
        for book in self.books:
            if title.lower() in book['title'].lower():
                results.append(book)
        return results

file.write(f"{datetime.datetime.now()} - تابع '{func.__name__}' اجرا شد\n")
            return result
        return wrapper


  def search_by_author(self, author):
         result = []
        for book in self.books:
          if author.lower() in book['author'].lower():
                 results.append(book)
            return results
