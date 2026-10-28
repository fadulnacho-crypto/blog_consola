"""Persistencia del blog: carga y guardado de posts en posts.json."""

import json
import os

from blog.modelos import Autor, Post

RUTA_JSON = "posts.json"


def autor_por_defecto():
    """Autor principal del blog."""
    return Autor(
        "Ignacio Garcia Fadul",
        "Estudiante de Python y desarrollo web.",
        "ignacio@blog.com",
    )


def posts_iniciales():
    """Posts de ejemplo que se usan si posts.json no existe o no sirve."""
    autor = autor_por_defecto()
    return [
        Post(1, "Introduccion a Python", "Python es un lenguaje simple y poderoso.",
             autor, ["python", "programacion"], "publicado"),
        Post(2, "Primeros pasos con Django", "Django es un framework web para Python.",
             autor, ["django", "web", "python"], "borrador"),
        Post(3, "Consejos para aprender a programar", "Practicar todos los dias es la clave.",
             autor, ["consejos", "programacion"], "publicado"),
        # Post con errores a proposito, para probar la validacion
        Post(4, "", "Este post no tiene titulo.", autor, [], "pendiente"),
    ]


def cargar_posts(ruta=RUTA_JSON):
    """Lee posts.json y retorna una lista de objetos Post.

    Maneja los casos de archivo inexistente, vacio o con contenido invalido.
    Los posts incompletos se descartan con un aviso.
    """
    if not os.path.exists(ruta):
        print(f"Aviso: no existe '{ruta}'. Se cargan los posts de ejemplo.")
        return posts_iniciales()

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except OSError as error:
        print(f"Error: no se pudo leer '{ruta}' ({error}). Se cargan los posts de ejemplo.")
        return posts_iniciales()

    if contenido.strip() == "":
        print(f"Aviso: '{ruta}' esta vacio. Se cargan los posts de ejemplo.")
        return posts_iniciales()

    try:
        datos = json.loads(contenido)
    except json.JSONDecodeError:
        print(f"Error: '{ruta}' no tiene un JSON valido. Se cargan los posts de ejemplo.")
        return posts_iniciales()

    if not isinstance(datos, list):
        print(f"Error: '{ruta}' debe contener una lista de posts. Se cargan los posts de ejemplo.")
        return posts_iniciales()

    posts = []
    for posicion, item in enumerate(datos, start=1):
        try:
            posts.append(Post.from_dict(item))
        except (ValueError, TypeError) as error:
            print(f"Aviso: el post #{posicion} del JSON no se pudo cargar: {error}.")
    return posts


def guardar_posts(posts, ruta=RUTA_JSON):
    """Convierte los objetos Post a diccionarios y los guarda en posts.json.

    Retorna True si se guardo correctamente, False si hubo un error.
    """
    lista_dicts = []
    for post in posts:
        if not isinstance(post, Post):
            print(f"Error: se intento guardar un objeto que no es un Post ({type(post).__name__}).")
            return False
        lista_dicts.append(post.to_dict())

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(lista_dicts, archivo, ensure_ascii=False, indent=4)
    except TypeError as error:
        print(f"Error: hay datos que no se pueden convertir a JSON ({error}).")
        return False
    except OSError as error:
        print(f"Error: no se pudo escribir '{ruta}' ({error}).")
        return False
    return True
