import tkinter as tk
from tkinter import ttk, messagebox

class LibraryGUI:
    

    def __init__(self, db_connection):

        # Crear ventana principal
        self.window = tk.Tk()
        self.window.geometry("800x600")
        self.window.resizable(True, True)


        self.window.title('Sistema de Gestion de Biblioteca')

        # Marco principal
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(padx=10, pady=10)

        # Etiqueta de titulo
        self.title_label = tk.Label(self.main_frame, text = "Sistema de Gestion de Biblioteca")
        self.title_label.config(font=('Arial', 16, "bold"))

        # Boton de agregar libro
        self.add_book_button = tk.Button(self.main_frame, text="Agregar Libro")
        self.add_book_button.config(command=self.add_book)
        self.add_book_button.pack(pady=10)

        # Boton para buscar libro
        self.search_book_button = tk.Button(self.main_frame, text="Buscar Libro")
        self.search_book_button.config(command=self.search_book)
        self.search_book_button.pack(pady=10)
    
    def add_book(self):
        # Crear ventana para agregar libro
        self.add_book_window = tk.Toplevel()
        self.add_book_window.geometry("400x300")
        self.add_book_window.title("Agregar Nuevo Libro")

        # Crear campos de texto
        self.title_label = tk.Label(self.add_book_window, text="Titulo:")
        self.title_label.pack()
        self.title_entry = tk.Entry(self.add_book_window)
        self.title_entry.pack()

        self.author_label = tk.Label(self.add_book_window, text="Autor:")
        self.author_label.pack()
        self.author_entry = tk.Entry(self.add_book_window)
        self.author_entry.pack()

        self.editorial_label = tk.Label(self.add_book_window, text="Editorial:")
        self.editorial_label.pack()
        self.editorial_entry = tk.Entry(self.add_book_window)
        self.editorial_entry.pack()

        self.ISBN_label = tk.Label(self.add_book_window, text="ISBN:")
        self.ISBN_label.pack()
        self.ISBN_entry = tk.Entry(self.add_book_window)
        self.ISBN_entry.pack()

        self.publication_date_label = tk.Label(self.add_book_window, text="Fecha de Publicacion:")
        self.publication_date_label.pack()
        self.publication_date_entry = tk.Entry(self.add_book_window)
        self.publication_date_entry.pack()

        self.genre_label = tk.Label(self.add_book_window, text="Genero:")
        self.genre_label.pack()
        self.genre_entry = tk.Entry(self.add_book_window)
        self.genre_entry.pack()

        # Boton para guardar libro
        self.save_button = tk.Button(self.add_book_window, text="Guardar")
        self.save_button.config(command=self.save_book)
        self.save_button.pack(pady=10)
    
    def save_book(self):
        # Obtener datos del libro
        title = self.title_entry.get()
        author = self.author_entry.get()
        editorial = self.editorial_entry.get()
        isbn = self.ISBN_entry.get()
        publication_date = self.publication_date_entry.get()
        genre = self.genre_entry.get()

        # Validar que los campos no esten vacios
        if title == "" or author == "" or editorial == "" or isbn == "" or publication_date == "" or genre == "":
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return
        
        # Insertar libro en la base de datos
        cursor = self.db_connection.cursor()
        insert_query = "INSERT INTO libros (titulo, autor, editorial, isbn, fecha_publicacion, genero) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (title, author, editorial, isbn, publication_date, genre))
        self.db_connection.commit()
        cursor.close()

        # Cerrar ventana
        self.add_book_window.destroy()
    
    def search_book(self):
        # Crear ventana para buscar libro
        self.search_book_window = tk.Toplevel()
        self.search_book_window.title("Buscar Libro")

        # Crear campo de texto
        self.search_label = tk.Label(self.search_book_window, text="Titulo:")
        self.search_label.pack()
        self.search_entry = tk.Entry(self.search_book_window)
        self.search_entry.pack()

        # Boton para buscar libro
        self.search_button = tk.Button(self.search_book_window, text="Buscar")
        self.search_button.config(command=self.search)
        self.search_button.pack(pady=10)


if __name__ == "__main__":
    library_gui = LibraryGUI()
    library_gui.window.mainloop()