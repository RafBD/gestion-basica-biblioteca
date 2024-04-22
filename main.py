from db_connection import connect_db
from tkinter import messagebox
from tkinter_ui import LibraryGUI

# Iniciar la interfaz grafica
if __name__ == "__main__":
    # Conectar a la base de datos
    db_connection = connect_db()

    if db_connection:
        library_gui = LibraryGUI(db_connection)
        library_gui.window.mainloop()
    else:
        messagebox.showerror("Error", "Error al conectar con la base de datos")