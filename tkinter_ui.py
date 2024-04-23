import tkinter as tk
from tkinter import messagebox

font_size = 16
font_weight = "bold"
font_family = "Arial"
background_color = "lightblue"
foreground_color = "white"
pady = 10

class LibraryGUI:

    def __init__(self, db_connection):

        # Crear ventana principal
        self.window = tk.Tk()
        self.window.geometry("1920x1080")
        self.window.configure(background = background_color)
        self.window.resizable(True, True)

        self.window.title('Sistema de Gestion de Biblioteca')

        # Marco principal
        self.main_frame = tk.Frame(self.window)
        self.main_frame.configure(background = background_color)
        self.main_frame.pack(padx=10, pady=10)

        # Etiqueta de titulo
        self.title_label = tk.Label(self.main_frame, text = "Sistema de Gestion de Biblioteca")

        # Boton de agregar libro
        self.add_book_button = tk.Button(self.main_frame, text="Agregar Libro")
        self.add_book_button.config(command=self.add_book, font=(font_family, font_size, font_weight), background=("green"), foreground=foreground_color)
        self.add_book_button.pack(pady = pady)

        # Boton para buscar libro
        self.search_book_button = tk.Button(self.main_frame, text="Buscar Libro")
        self.search_book_button.config(command=self.search_book, font=(font_family, font_size, font_weight), background = ("indigo"), foreground = foreground_color)
        self.search_book_button.pack(pady = pady)

        # Boton para ver todos los libros
        self.view_books_button = tk.Button(self.main_frame, text="Ver Todos los Libros")
        self.view_books_button.config(command=self.show_all_books, font=(font_family, font_size, font_weight), background=("coral"), foreground = foreground_color)
        self.view_books_button.pack(pady = pady)

        # Guardar conexion a la base de datos como atributo de instancia
        self.db_connection = db_connection
    
    def add_book(self):
        # Crear ventana para agregar libro
        self.add_book_window = tk.Toplevel()
        self.add_book_window.geometry("600x400")
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
        self.save_button.config(command=self.save_book, font=(font_family, font_size, font_weight), background=("green"), foreground=foreground_color)
        self.save_button.pack(pady = 20)
    
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
        
        try:
            # Insertar libro en la base de datos
            cursor = self.db_connection.cursor()
            insert_query = "INSERT INTO libros (titulo, autor, editorial, isbn, fecha_publicacion, genero) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (title, author, editorial, isbn, publication_date, genre))
            self.db_connection.commit()
            cursor.close()

            messagebox.showinfo("Exito", "Libro guardado exitosamente")

            # Cerrar ventana
            self.add_book_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar libro: {e}")
    
    def search_book(self):
        # Crear ventana para buscar libro
        self.search_book_window = tk.Toplevel()
        self.search_book_window.geometry("600x400")
        self.search_book_window.resizable(True, True)
        self.search_book_window.title("Buscar Libro")

        # Buscar por titulo
        self.search_label = tk.Label(self.search_book_window, text="Buscar por titulo:")
        self.search_label.pack()
        self.search_entry_title = tk.Entry(self.search_book_window)
        self.search_entry_title.pack()

        # Buscar por autor
        self.search_label = tk.Label(self.search_book_window, text="Buscar por autor:")
        self.search_label.pack()
        self.search_entry_author = tk.Entry(self.search_book_window)
        self.search_entry_author.pack()

        # Buscar por Editorial
        self.search_label = tk.Label(self.search_book_window, text="Buscar por editorial:")
        self.search_label.pack()
        self.search_entry_editorial = tk.Entry(self.search_book_window)
        self.search_entry_editorial.pack()

        # Buscar por Editorial
        self.search_label = tk.Label(self.search_book_window, text="Buscar por año de publicacion:")
        self.search_label.pack()
        self.search_entry_publication_year = tk.Entry(self.search_book_window)
        self.search_entry_publication_year.pack()

        # Boton para buscar libro
        self.search_button = tk.Button(self.search_book_window, text="Buscar")
        self.search_button.config(command = self.save_book, font = (font_family, font_size, font_weight), background=("purple"), foreground = foreground_color) 
        self.search_button.config(command = self.perform_search)
        self.search_button.pack(pady = 20)

        # Frame para mostrar los resultados
        self.search_results_frame = tk.Frame(self.search_book_window)
        self.search_results_frame.pack()

    def perform_search(self):
        # Obtener los valores de búsqueda
        title = self.search_entry_title.get()
        author = self.search_entry_author.get()
        editorial = self.search_entry_editorial.get()
        publication_year = self.search_entry_publication_year.get()

        if title == "" or author == "" or editorial == "" or publication_year == "":
            messagebox.showerror("Error", "Debe ingresar al menos un campo para buscar")
            

        # Realizar la búsqueda basada en el campo no vacío
        if title:
            self.perform_generic_search("titulo", title)
        elif author:
            self.perform_generic_search("autor", author)
        elif editorial:
            self.perform_generic_search("editorial", editorial)
        elif publication_year:
            self.perform_generic_search("fecha_publicacion", publication_year)

    def perform_generic_search(self, column, value):
        try:
            # Limpiar ventana
            for widget in self.search_results_frame.winfo_children():
                widget.destroy()

            # Buscar libro en la base de datos
            cursor = self.db_connection.cursor()
            select_query = f"SELECT * FROM libros WHERE {column} LIKE %s"
            cursor.execute(select_query, (f"%{value}%",))
            self.db_connection.commit()

            # Mostrar resultados
            books = cursor.fetchall()
            cursor.close()

            if books:
                for book in books:
                    book_label = tk.Label(self.search_book_window, text=f"Título:{book[1]} | Autor: {book[2]} | Editorial: {book[3]} | ISBN:{book[4]} | Año de Publicación: {book[5]} | Género: {book[6]}")
                    book_label.pack()
            else:
                messagebox.showinfo("Resultado de Busqueda ", "Libro no encontrado")
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar libro: {e}")
    
    def show_all_books(self):
        # Crear ventana para mostrar todos los libros
        self.show_books_window = tk.Toplevel()
        self.show_books_window.geometry("800x600")
        self.show_books_window.resizable(True, True)
        self.show_books_window.title("Todos los Libros")

        # Mostrar todos los libros en una lista
        cursor = self.db_connection.cursor()
        select_query = "SELECT * FROM libros"
        cursor.execute(select_query)
        books = cursor.fetchall()
        cursor.close()

        for book in books:
            book_label = tk.Label(self.show_books_window, text=f"Título:{book[1]} | Autor: {book[2]} | Editorial: {book[3]} | ISBN:{book[4]} | Año de Publicación: {book[5]} | Género: {book[6]}")
            book_label.pack()




if __name__ == "__main__":
    library_gui = LibraryGUI()
    library_gui.window.mainloop()