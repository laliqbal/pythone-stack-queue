class BookStack:
    def __init__(self):
        self.stack = []

    def push(self, book):
        self.stack.append(book)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book_stack = BookStack()

while True:
    print("\n=== Menu ===")
    print("1. Tambahkan Buku")
    print("2. Hapus Buku Terakhir")
    print("3. Tampilkan Buku Teratas")
    print("0. Keluar")

    choice = input("Pilih menu: ")

    if choice == "1":
        title = input("Masukkan judul buku: ")
        author = input("Masukkan pengarang buku: ")
        book = Book(title, author)
        book_stack.push(book)
        print("Buku ditambahkan ke dalam tumpukan.")

    elif choice == "2":
        if book_stack.is_empty():
            print("Tumpukan buku kosong.")
        else:
            removed_book = book_stack.pop()
            print(f"Buku '{removed_book.title}' Di Karang oleh {removed_book.author} dihapus dari tumpukan.")

    elif choice == "3":
        if book_stack.is_empty():
            print("Tumpukan buku kosong.")
        else:
            top_book = book_stack.peek()
            print(f"Buku teratas: '{top_book.title}' DI Karang oleh {top_book.author}.")

    elif choice == "0":
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
