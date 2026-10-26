"""Estructuras de datos base del blog."""

# Perfil del autor (diccionario que se anida dentro de cada post)
perfil_autor = {
    "nombre": "Ignacio Garcia Fadul",
    "email": "ignacio@blog.com",
    "bio": "Estudiante de Python y desarrollo web.",
}

# Estados posibles de un post (tupla: no cambian)
estados_post = ("borrador", "publicado", "archivado")

# Etiquetas disponibles en el blog (set: sin repetidos)
etiquetas_blog = {"python", "django", "programacion", "web", "consejos"}

# Lista de posts
posts = [
    {
        "id": 1,
        "titulo": "Introduccion a Python",
        "contenido": "Python es un lenguaje simple y poderoso.",
        "autor": perfil_autor,
        "tags": ["python", "programacion"],
        "estado": "publicado",
    },
    {
        "id": 2,
        "titulo": "Primeros pasos con Django",
        "contenido": "Django es un framework web para Python.",
        "autor": perfil_autor,
        "tags": ["django", "web", "python"],
        "estado": "borrador",
    },
    {
        "id": 3,
        "titulo": "Consejos para aprender a programar",
        "contenido": "Practicar todos los dias es la clave.",
        "autor": perfil_autor,
        "tags": ["consejos", "programacion"],
        "estado": "publicado",
    },
    {
        # Post con errores a proposito, para probar la validacion
        "id": 4,
        "titulo": "",
        "contenido": "Este post no tiene titulo.",
        "autor": "Autor sin perfil",
        "tags": "web",
        "estado": "pendiente",
    },
]
