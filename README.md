# Blog por Consola – Preentrega 6: POO y Persistencia JSON

Sistema de blog por consola en Python. Permite ver, buscar, filtrar, crear y validar posts, y guarda la información en un archivo `posts.json` para que no se pierda entre ejecuciones.

En esta versión el proyecto pasó de usar diccionarios y funciones sueltas a usar **Programación Orientada a Objetos** (clases `Autor`, `Post` y `Blog`) con **persistencia en JSON**.

## Cómo ejecutarlo

Requiere Python 3. Desde la carpeta raíz del proyecto (donde está `main.py`):

```bash
python main.py
```

## Estructura del proyecto

```
blog_consola/
│
├── main.py
├── README.md
├── posts.json
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── modelos.py
    ├── operaciones.py
    └── validaciones.py
```

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Punto de entrada. Carga los posts, crea la instancia de `Blog`, muestra el menú y llama a los métodos del blog. Usa `if __name__ == "__main__":`. |
| `blog/__init__.py` | Hace que Python reconozca la carpeta `blog/` como paquete. |
| `blog/modelos.py` | Clases `Autor`, `Post` y `Blog`. |
| `blog/datos.py` | Persistencia: `cargar_posts()` y `guardar_posts()` con el módulo `json`. También tiene los posts de ejemplo. |
| `blog/menu.py` | Menú y `input()` del usuario, incluyendo los datos para crear un post. |
| `blog/operaciones.py` | Muestra en consola los resultados que devuelve el `Blog`. |
| `blog/validaciones.py` | Reglas de validación de un objeto `Post` y la tupla de estados válidos. |

## Clases principales (`blog/modelos.py`)

### `Autor`
Representa a la persona que escribe en el blog.
- Atributos: `nombre`, `bio`, `email`.
- `to_dict()`: convierte el autor en diccionario.
- `Autor.from_dict(datos)`: crea un autor a partir de un diccionario.

### `Post`
Representa una publicación.
- Atributos: `id`, `titulo`, `contenido`, `autor`, `tags`, `estado`.
- **Composición:** el atributo `autor` es un objeto `Autor`, no un texto. Si se pasa otra cosa, lanza `TypeError`.
- `tiene_tag(tag)`: indica si el post tiene una etiqueta (sin distinguir mayúsculas).
- `to_dict()`: convierte el post y su autor en un diccionario.
- `Post.from_dict(datos)`: reconstruye un post desde un diccionario. Si faltan claves, lanza `ValueError`.

### `Blog`
Centraliza la lógica del sistema. Su atributo `posts` es una **lista de objetos `Post`**.
- `agregar_post(post)`, `obtener_posts()`, `listar_posts()`
- `buscar_por_titulo(termino)` y `filtrar_por_tag(tag)`: ignoran mayúsculas y minúsculas.
- `crear_post(titulo, contenido, autor, tags, estado)`: crea una instancia de `Post`, le asigna el próximo id y la agrega al blog.
- `validar_posts()`: valida cada post con `validaciones.py`.
- `to_list()`: convierte todos los posts en una lista de diccionarios.

## Cómo se guarda y carga la información (`posts.json`)

JSON no puede guardar objetos de Python directamente, por eso se convierten:

```
Guardar:  Blog.posts (objetos Post) ──to_dict()──► lista de diccionarios ──json.dump──► posts.json
Cargar:   posts.json ──json.loads──► lista de diccionarios ──Post.from_dict()──► objetos Post ──► Blog
```

- **Al iniciar**, `main.py` llama a `cargar_posts()`, que lee `posts.json` y reconstruye los objetos `Post` (con su `Autor`). Con esa lista se crea la instancia de `Blog`.
- **Al guardar** (opción 6, y también automáticamente al salir con la opción 7), `guardar_posts()` convierte cada `Post` con `to_dict()` y escribe el archivo con `json.dump`.

### Manejo de errores
- `posts.json` no existe, está vacío o tiene JSON inválido → se avisa y se cargan los posts de ejemplo, sin cerrar el programa.
- Un post del JSON está incompleto → se avisa cuál es y se omite; el resto se carga igual.
- Se intenta guardar algo que no es un `Post` (por ejemplo, un diccionario) → mensaje de error y no se guarda.
- Opción de menú incorrecta → se avisa y se vuelve a mostrar el menú.
- Campos vacíos al crear un post → se vuelven a pedir.

## Menú

```
--- MENU DEL BLOG ---
1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Crear nuevo post
5. Validar posts
6. Guardar posts en JSON
7. Salir
```

El post 4 de los datos de ejemplo tiene errores a propósito (sin título, sin etiquetas y estado inválido) para demostrar la validación.

## Qué cambió respecto a la Preentrega 5

- Se agregó `blog/modelos.py` con las clases `Autor`, `Post` y `Blog`.
- Los posts dejaron de ser diccionarios: ahora son objetos `Post`, y el autor es un objeto `Autor`.
- La lógica de listar, buscar y filtrar pasó de funciones en `operaciones.py` a métodos de la clase `Blog`.
- `datos.py` ahora se encarga de la persistencia: carga y guarda los posts en `posts.json`.
- Se agregaron las opciones **Crear nuevo post** y **Guardar posts en JSON** al menú.
- `validaciones.py` ahora valida objetos `Post` en lugar de diccionarios.

## Autor

Ignacio Garcia Fadul
