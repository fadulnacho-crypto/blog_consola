"""Reglas de validacion de los posts."""

# Estados posibles de un post (tupla: no cambian)
ESTADOS_POST = ("borrador", "publicado", "archivado")


def validar_post(post):
    """Valida los datos de un objeto Post.

    Retorna una lista de errores. Si la lista esta vacia, el post es valido.
    """
    errores = []

    if str(post.titulo).strip() == "":
        errores.append("El titulo esta vacio.")

    if str(post.contenido).strip() == "":
        errores.append("El contenido esta vacio.")

    if str(post.autor.nombre).strip() == "":
        errores.append("El autor no tiene nombre.")

    if not isinstance(post.tags, list) or len(post.tags) == 0:
        errores.append("El post no tiene etiquetas.")

    if post.estado not in ESTADOS_POST:
        errores.append(f"Estado invalido: '{post.estado}'. Debe ser uno de {ESTADOS_POST}.")

    return errores
