class CLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            
            if command == "sair":
                break
            
            elif command in self.commands:
                self.commands[command]()
            
            else:
                print("Comando invalido")

class BookCLI(CLI):
    def __init__(self, book):
        super().__init__()
        self.book = book
        self.add_command("criar", self.create_book)
        self.add_command("ler", self.read_book)
        self.add_command("modificar", self.update_book)
        self.add_command("deletar", self.delete_book)


    def create_book(self):
        titulo = input("Digite o titulo: ")
        autor = input("Digite o autor: ")
        ano = int(input("Digite o ano: "))
        preco = float(input("Digite o preço: "))
        
        self.book.create_book(titulo, autor, ano, preco)

    def read_book(self):
        id = input("Digite o id: ")
        
        book = self.book.read_book_by_id(id)
        
        if book:
            print(f"titulo: {book['titulo']}")
            print(f"autor: {book['autor']}")
            print(f"ano: {book['ano']}")
            print(f"preço: {book['preco']}")

    def update_book(self):
        id = input("Digite o id: ")
        
        titulo = input("Digite o novo titulo: ")
        autor = input("Digite o novo autor: ")
        ano = int(input("Digite o novo ano: "))
        preco = float(input("Digite o novo preço: "))
        
        self.book.update_book(id, titulo, autor, ano, preco)

    def delete_book(self):
        id = input("Digite o id: ")
        
        self.book.delete_book(id)
        
    def run(self):
        print("Comandos: criar, ler, modificar, deletar, sair ")
        super().run()