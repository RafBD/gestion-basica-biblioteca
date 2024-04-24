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

        # Boton para registrar usuarios
        self.add_user_button = tk.Button(self.main_frame, text="Registrar Nuevo Usuario")
        self.add_user_button.config(command=self.add_user, font=(font_family, font_size, font_weight), background=("lightgreen"), foreground='black')
        self.add_user_button.pack(pady = pady)

        # Boton de agregar libro
        self.add_book_button = tk.Button(self.main_frame, text="Agregar Libro")
        self.add_book_button.config(command=self.add_book, font=(font_family, font_size, font_weight), background=("green"), foreground=foreground_color)
        self.add_book_button.pack(pady = pady)

        # Boton para buscar libro
        self.search_book_button = tk.Button(self.main_frame, text="Buscar Libro")
        self.search_book_button.config(command=self.search_book, font=(font_family, font_size, font_weight), background = ("indigo"), foreground = foreground_color)
        self.search_book_button.pack(pady = pady)

        # Boton para prestar libro
        self.lend_book_button = tk.Button(self.main_frame, text="Prestar Libro")
        self.lend_book_button.config(command=self.book_loan ,font=(font_family, font_size, font_weight), background=("Brown"), foreground = foreground_color)
        self.lend_book_button.pack(pady = pady)

        # Boton para devolver libro
        self.lend_book_button = tk.Button(self.main_frame, text="Devolver Libro")
        self.lend_book_button.config(command=self.return_of_books ,font=(font_family, font_size, font_weight), background=("Gray"), foreground = 'black')
        self.lend_book_button.pack(pady = pady)

        # Boton para ver todos los libros
        self.view_books_button = tk.Button(self.main_frame, text="Ver Todos los Libros")
        self.view_books_button.config(command=self.show_all_books, font=(font_family, font_size, font_weight), background=("lightpink"), foreground = 'black')
        self.view_books_button.pack(pady = pady)

        # Ver todos los usuarios
        self.view_users_button = tk.Button(self.main_frame, text="Ver Todos los Usuarios")
        self.view_users_button.config(command=self.show_all_users, font=(font_family, font_size, font_weight), background=("coral"), foreground = foreground_color)
        self.view_users_button.pack(pady = pady)

        # Guardar conexion a la base de datos como atributo de instancia
        self.db_connection = db_connection
    
    def add_user(self):
        # Crear ventana para agregar usuario
        self.add_user_window = tk.Toplevel()
        self.add_user_window.geometry("600x400")
        self.add_user_window.title("Registrar Nuevo Usuario")

        # Crear campos de texto
        self.name_label = tk.Label(self.add_user_window, text="Nombre:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.add_user_window)
        self.name_entry.pack()

        self.last_name_label = tk.Label(self.add_user_window, text="Apellido:")
        self.last_name_label.pack()
        self.last_name_entry = tk.Entry(self.add_user_window)
        self.last_name_entry.pack()

        self.address_label = tk.Label(self.add_user_window, text="Direccion:")
        self.address_label.pack()
        self.address_entry = tk.Entry(self.add_user_window)
        self.address_entry.pack()

        self.phone_label = tk.Label(self.add_user_window, text="Telefono:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self.add_user_window)
        self.phone_entry.pack()

        self.email_label = tk.Label(self.add_user_window, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.add_user_window)
        self.email_entry.pack()

        # Boton para guardar usuario
        self.save_button = tk.Button(self.add_user_window, text="Guardar")
        self.save_button.config(command=self.save_user, font=(font_family, font_size, font_weight), background=("green"), foreground=foreground_color)
        self.save_button.pack(pady = 20)

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

        self.available_copies_label = tk.Label(self.add_book_window, text="Copias Disponibles:")
        self.available_copies_label.pack()
        self.available_copies_entry = tk.Entry(self.add_book_window)
        self.available_copies_entry.pack()

        # Boton para guardar libro
        self.save_button = tk.Button(self.add_book_window, text="Guardar")
        self.save_button.config(command=self.save_book, font=(font_family, font_size, font_weight), background=("green"), foreground=foreground_color)
        self.save_button.pack(pady = 20)
    
    def save_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        editorial = self.editorial_entry.get()
        isbn = self.ISBN_entry.get()
        publication_date = int(self.publication_date_entry.get())
        genre = self.genre_entry.get()
        available_copies = self.available_copies_entry.get()

        # Validar que los campos no esten vacios
        if title == "" or author == "" or editorial == "" or isbn == "" or publication_date == "" or genre == "":
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return
        
        try:
            # Insertar libro en la base de datos
            cursor = self.db_connection.cursor()
            insert_query = "INSERT INTO libros (titulo, autor, editorial, isbn, fecha_publicacion, genero, ejemplares_disponibles) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (title, author, editorial, isbn, publication_date, genre, available_copies))
            self.db_connection.commit()
            cursor.close()

            messagebox.showinfo("Exito", "Libro guardado exitosamente")

            # Cerrar ventana
            self.add_book_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar libro: {e}")

    def save_user(self):
        # Obtener datos del usuario
        name = self.name_entry.get()
        last_name = self.last_name_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        # Validar que los campos no esten vacios
        if name == "" or last_name == "" or email == "":
            messagebox.showerror("Error", "El nombre, apellido y correo electrónico son requeridos")
            return
        
        try:
            # Insertar usuario en la base de datos
            cursor = self.db_connection.cursor()
            insert_query = "INSERT INTO usuarios (nombre, apellidos, direccion, telefono, correo_electronico) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (name, last_name, address, phone, email))
            self.db_connection.commit()
            cursor.close()

            messagebox.showinfo("Exito", "Usuario guardado exitosamente")

            # Cerrar ventana
            self.add_user_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar usuario: {e}")

    def search_book(self):
        # Crear ventana para buscar libro
        self.search_book_window = tk.Toplevel()
        self.search_book_window.geometry("600x400")
        self.search_book_window.resizable(True, True)
        self.search_book_window.title("Buscar Libro")

        # Buscar por ID
        self.search_label = tk.Label(self.search_book_window, text="Buscar por ID: ")
        self.search_label.pack()
        self.search_entry_id = tk.Entry(self.search_book_window)
        self.search_entry_id.pack()

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
        book_id = self.search_entry_id.get()
        title = self.search_entry_title.get()
        author = self.search_entry_author.get()
        editorial = self.search_entry_editorial.get()
        publication_year = self.search_entry_publication_year.get()

        # Realizar la búsqueda basada en el campo no vacío
        if book_id:
            self.perform_generic_search("libro_id", book_id)
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
                    book_label = tk.Label(self.search_book_window, text=f"ID: {book[0]} | Título: {book[1]} | Autor: {book[2]} | Editorial: {book[3]} | ISBN:{book[4]} | Año de Publicación: {book[5]} | Género: {book[6]} | Copias Disponibles: {book[7]}")
                    book_label.pack()
            else:
                messagebox.showinfo("Resultado de Busqueda ", "Libro no encontrado")
        except Exception as e:
            messagebox.showerror("Error", f"Error al buscar libro: {e}")
    
    def book_loan(self):
        # Crear ventana para prestar libro
        self.book_loan_window = tk.Toplevel()
        self.book_loan_window.geometry("600x400")
        self.book_loan_window.resizable(True, True)
        self.book_loan_window.title("Prestar Libro")

        # Crear campos de texto
        self.book_id_label = tk.Label(self.book_loan_window, text="ID del Libro:")
        self.book_id_label.pack()
        self.book_id_entry = tk.Entry(self.book_loan_window)
        self.book_id_entry.pack()

        self.user_id_label = tk.Label(self.book_loan_window, text="ID del Usuario:")
        self.user_id_label.pack()
        self.user_id_entry = tk.Entry(self.book_loan_window)
        self.user_id_entry.pack()

        # Boton para prestar libro
        self.loan_button = tk.Button(self.book_loan_window, text="Prestar")
        self.loan_button.config(command=self.loan_book, font=(font_family, font_size, font_weight), background=("green"), foreground=foreground_color)
        self.loan_button.pack(pady = 20)

    def loan_book(self):
        # Obtener datos del prestamo
        book_id = self.book_id_entry.get()
        user_id = self.user_id_entry.get()

        # Validar que los campos no esten vacios
        if book_id == "" or user_id == "":
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return
        
        try:
            # Verificar que el libro esté disponible
            cursor = self.db_connection.cursor()
            select_query = "SELECT ejemplares_disponibles FROM libros WHERE libro_id = %s"
            cursor.execute(select_query, (book_id,))
            available_copies = cursor.fetchone()[0]

            if available_copies > 0:
                # Insertar prestamo en la base de datos
                insert_query = "INSERT INTO prestamos (libro_id, usuario_id) VALUES (%s, %s)"
                cursor.execute(insert_query, (book_id, user_id))
                self.db_connection.commit()

                # Actualizar el número de ejemplares disponibles
                update_query = "UPDATE libros SET ejemplares_disponibles = ejemplares_disponibles - 1 WHERE libro_id = %s"
                cursor.execute(update_query, (book_id,))
                self.db_connection.commit()

                messagebox.showinfo("Exito", "Libro prestado exitosamente")

                # Cerrar ventana
                self.book_loan_window.destroy()
            else:
                messagebox.showerror("Error", "El libro no está disponible")
        except Exception as e:
            messagebox.showerror("Error", f"Error al prestar libro: {e}")
        finally:
            cursor.close()

    def return_of_books(self):
        # Crear ventana para devolver libro
        self.return_of_books_window = tk.Toplevel()
        self.return_of_books_window.geometry("600x400")
        self.return_of_books_window.resizable(True, True)
        self.return_of_books_window.title("Devolver Libro")

        # Crear campos de texto
        self.book_id_label = tk.Label(self.return_of_books_window, text="ID del Libro:")
        self.book_id_label.pack()
        self.book_id_entry = tk.Entry(self.return_of_books_window)
        self.book_id_entry.pack()

        self.user_id_label = tk.Label(self.return_of_books_window, text="ID del Usuario:")
        self.user_id_label.pack()
        self.user_id_entry = tk.Entry(self.return_of_books_window)
        self.user_id_entry.pack()

        # Boton para devolver libro
        self.return_button = tk.Button(self.return_of_books_window, text="Devolver")
        self.return_button.config(command=self.return_book, font=(font_family, font_size, font_weight), background=("green"), foreground=foreground_color)
        self.return_button.pack(pady = 20)
    
    def return_book(self):
        # Obtener datos de la devolución
        book_id = self.book_id_entry.get()
        user_id = self.user_id_entry.get()

        # Validar que los campos no esten vacios
        if book_id == "" or user_id == "":
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return
        
        try:
            # Verificar que el libro esté prestado
            cursor = self.db_connection.cursor()
            select_query = "SELECT * FROM prestamos WHERE libro_id = %s AND usuario_id = %s"
            cursor.execute(select_query, (book_id, user_id))
            loan = cursor.fetchone()

            if loan:
                # Eliminar prestamo de la base de datos
                delete_query = "DELETE FROM prestamos WHERE libro_id = %s AND usuario_id = %s"
                cursor.execute(delete_query, (book_id, user_id))
                self.db_connection.commit()

                # Actualizar el número de ejemplares disponibles
                update_query = "UPDATE libros SET ejemplares_disponibles = ejemplares_disponibles + 1 WHERE libro_id = %s"
                cursor.execute(update_query, (book_id,))
                self.db_connection.commit()

                messagebox.showinfo("Exito", "Libro devuelto exitosamente")

                # Cerrar ventana
                self.return_of_books_window.destroy()
            else:
                messagebox.showerror("Error", "El libro no está prestado")
        except Exception as e:
            messagebox.showerror("Error", f"Error al devolver libro: {e}")
        finally:
            cursor.close()

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
            book_label = tk.Label(self.show_books_window, text=f"ID: {book[0]} | Título: {book[1]} | Autor: {book[2]} | Editorial: {book[3]} | ISBN:{book[4]} | Año de Publicación: {book[5]} | Género: {book[6]}")
            book_label.pack()

    def show_all_users(self):
        # Crear ventana para mostrar todos los usuarios
        self.show_users_window = tk.Toplevel()
        self.show_users_window.geometry("800x600")
        self.show_users_window.resizable(True, True)
        self.show_users_window.title("Todos los Usuarios")

        # Mostrar todos los usuarios en una lista
        cursor = self.db_connection.cursor()
        select_query = "SELECT * FROM usuarios"
        cursor.execute(select_query)
        users = cursor.fetchall()
        cursor.close()

        for user in users:
            user_label = tk.Label(self.show_users_window, text=f"ID: {user[0]} | Nombre: {user[1]} | Apellidos: {user[2]} | Direccion: {user[3]} | Telefono:{user[4]} | Correo Electronico: {user[5]}")
            user_label.pack()

if __name__ == "__main__":
    library_gui = LibraryGUI()
    library_gui.window.mainloop()