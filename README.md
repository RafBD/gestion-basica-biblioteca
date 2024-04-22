# Sistema de Gestión Básica de una Biblioteca

## Funcionalidad

El sistema utiliza la biblioteca **tkinter** para crear una interfaz gráfica muy básica. Con esta se crean un menú principal y dos ventanas diferentes.

## Tecnologías utilizadas

- Python3 (3.12.3)
- PyMySQL (1.1.0)
- Tkinter (8.6.13)

## Segmentación del código

El sistema esta dividido en tres archivos principales: _main.py, db_connection.py & tkinter.py_

- **main.py**: Archivo principal que importa los archivos db_connection y tkinter. Utiliza la biblioteca Tkinter para crear una interfaz gráfica de usuario (GUI). Importa las clases necesarias para manejar cuadros de diálogo de mensajes, conectar a una base de datos y definir la interfaz de usuario principal. Intenta establecer una conexión con la base de datos y, si tiene éxito, crea y muestra la interfaz de usuario. En caso de que la conexión falle, muestra un mensaje de error al usuario.
- **db_connection.py**: Se realiza la conexión a la base de datos, así como el cierre de la misma.
- **tkinter.py**:
  - Define una clase llamada LibraryGUI.
  - En el método **init**, crea la ventana principal de la aplicación y define sus componentes, como etiquetas y botones para agregar y buscar libros.
  - Define métodos para agregar libros (add_book) y buscar libros (search_book), cada uno de los cuales crea una nueva ventana secundaria con campos de entrada para los detalles del libro y botones para guardar o buscar libros.
  - En el método save_book, recupera los datos ingresados por el usuario desde los campos de entrada y los valida. Luego, inserta los datos del libro en una base de datos MySQL utilizando PyMySQL.
  - En el método search_book, crea una ventana secundaria para buscar libros por título.
  - En el bloque if **name** == "**main**", crea una instancia de la clase LibraryGUI y ejecuta el bucle principal de eventos de la aplicación.
