"""Reglas de validacion del blog."""

from blog.datos import estados_post

CLAVES_REQUERIDAS = ("id", "titulo", "contenido", "autor", "tags", "estado")


def validar_post(post):
    """Valida la estructura de un post.

    Retorna una lista de errores. Si la lista esta vacia, el post es valido.
    """
    errores = []

    if not isinstance(post, dict):
        return ["El post no es un diccionario."]

    for clave in CLAVES_REQUERIDAS:
        if clave not in post:
            errores.append(f"Falta la clave '{clave}'.")
    if errores:
        return errores

    if str(post["titulo"]).strip() == "":
        errores.append("El titulo esta vacio.")

    if str(post["contenido"]).strip() == "":
        errores.append("El contenido esta vacio.")

    if not isinstance(post["autor"], dict):
        errores.append("El autor no es un diccionario.")
    elif not post["autor"].get("nombre"):
        errores.append("El autor no tiene nombre.")

    if not isinstance(post["tags"], list):
        errores.append("Los tags no estan guardados como lista.")

    if post["estado"] not in estados_post:
        errores.append(f"Estado invalido: '{post['estado']}'.")

    return errores


def validar_posts(lista):
    """Valida todos los posts e informa cuales son validos y cuales no."""
    validos = 0
    for post in lista:
        errores = validar_post(post)
        identificador = post.get("id", "?") if isinstance(post, dict) else "?"
        if errores:
            print(f"Post {identificador}: INVALIDO")
            for error in errores:
                print(f"   - {error}")
        else:
            validos += 1
            print(f"Post {identificador}: valido")
    print(f"\nResumen: {validos} validos de {len(lista)} posts.")
