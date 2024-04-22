import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import connect_db
from tkinter_ui import LibraryGUI

# Conectar a la base de datos
db_connection = connect_db()

# Iniciar la interfaz grafica
if db_connection:
    library_gui = LibraryGUI(db_connection)
    library_gui.window.mainloop()
else:
    messagebox.showerror("Error", "No se pudo conectar a la base de datos")