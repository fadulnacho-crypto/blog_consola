"""Operaciones de presentacion: muestran en consola los resultados del Blog."""


def mostrar_posts(posts, titulo="Posts"):
    """Muestra una lista de objetos Post."""
    if not posts:
        print("No hay posts para mostrar.")
        return
    print(f"\n{titulo}: {len(posts)}")
    for post in posts:
        print(f"- {post}")


def mostrar_validacion(resultados):
    """Muestra el resultado de Blog.validar_posts()."""
    if not resultados:
        print("No hay posts para validar.")
        return
    for post, errores in resultados:
        if errores:
            print(f"\nPost {post.id}: INVALIDO")
            for error in errores:
                print(f"   - {error}")
        else:
            print(f"\nPost {post.id}: valido")
