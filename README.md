# Blog por Consola – Preentrega 5

Sistema de blog por consola en Python, organizado en módulos y paquetes.
Permite listar posts, buscar por título, filtrar por tag y validar la estructura de los posts.

## Cómo ejecutarlo

Requiere Python 3. Desde la carpeta raíz del proyecto (donde está `main.py`):

```bash
python main.py
```

El archivo que se ejecuta es **`main.py`**.

## Estructura del proyecto

```
blog_consola/
│
├── main.py
├── README.md
│
└── blog/
    ├── __init__.py
    ├── datos.py
    ├── menu.py
    ├── operaciones.py
    └── validaciones.py
```

## Responsabilidad de cada archivo

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Archivo principal. Importa los módulos del paquete `blog` y coordina el flujo del menú. La ejecución está protegida con `if __name__ == "__main__":`. |
| `blog/__init__.py` | Hace que Python reconozca la carpeta `blog/` como paquete. |
| `blog/datos.py` | Datos base: `perfil_autor`, `estados_post`, `etiquetas_blog` y la lista `posts`. El autor es un diccionario anidado en cada post. |
| `blog/menu.py` | Muestra el menú y maneja el `input()` del usuario. |
| `blog/operaciones.py` | Listar, buscar por título y filtrar por tag (usa `.lower()` para ignorar mayúsculas). |
| `blog/validaciones.py` | Valida cada post: que sea diccionario, que tenga las claves requeridas, título y contenido no vacíos, autor como diccionario con nombre, tags como lista y estado válido. |

## Funcionalidades del menú

```
--- MENU DEL BLOG ---
1. Ver todos los posts
2. Buscar por titulo
3. Filtrar por tag
4. Validar posts
5. Salir
```

1. **Ver todos los posts:** muestra título, autor y estado.
2. **Buscar por título:** coincidencia total o parcial, sin distinguir mayúsculas.
3. **Filtrar por tag:** muestra los posts con esa etiqueta, sin distinguir mayúsculas.
4. **Validar posts:** indica qué posts son válidos y cuáles tienen errores (el post 4 tiene errores a propósito para demostrar la validación).
5. **Salir:** muestra un mensaje de despedida y termina el programa.

## Autor

Ignacio Garcia Fadul
