from tkinter import messagebox
from db_connection import connect_db
from tkinter_ui import LibraryGUI

# Conectar a la base de datos
db_connection = connect_db()

# Iniciar la interfaz grafica
if db_connection:
    library_gui = LibraryGUI(db_connection)
    library_gui.start()
else:
    messagebox.showerror("Error", "No se pudo conectar a la base de datos")