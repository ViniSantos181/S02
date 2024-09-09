from database import Database
from book import book
from cli import BookCLI

db = Database(database="relatorio-5", collection="livros")
bookModel = book(database=db)

bookCLI = BookCLI(bookModel)
bookCLI.run()