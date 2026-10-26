"""Operaciones principales del blog: listar, buscar y filtrar."""


def mostrar_post(post):
    """Muestra los datos principales de un post."""
    autor = post.get("autor")
    nombre = autor.get("nombre", "Sin nombre") if isinstance(autor, dict) else "Autor invalido"
    titulo = post.get("titulo") or "(sin titulo)"
    print(f"- [{post.get('id')}] {titulo} | Autor: {nombre} | Estado: {post.get('estado')}")


def listar_posts(lista):
    """Muestra todos los posts de la lista recibida."""
    if not lista:
        print("No hay posts para mostrar.")
        return
    print(f"\nPosts encontrados: {len(lista)}")
    for post in lista:
        mostrar_post(post)


def buscar_por_titulo(lista, termino):
    """Retorna los posts cuyo titulo contiene el termino (ignora mayusculas)."""
    termino = termino.lower()
    return [p for p in lista if termino in str(p.get("titulo", "")).lower()]


def filtrar_por_tag(lista, tag):
    """Retorna los posts que tienen el tag indicado (ignora mayusculas)."""
    tag = tag.lower()
    resultado = []
    for post in lista:
        tags = post.get("tags", [])
        if isinstance(tags, list) and tag in [t.lower() for t in tags]:
            resultado.append(post)
    return resultado
