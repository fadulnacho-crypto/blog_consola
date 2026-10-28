"""Menu e interaccion con el usuario (manejo de input)."""

from blog.validaciones import ESTADOS_POST


def mostrar_menu():
    """Muestra las opciones y retorna la opcion elegida por el usuario."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Crear nuevo post")
    print("5. Validar posts")
    print("6. Guardar posts en JSON")
    print("7. Salir")
    return input("Elegi una opcion: ").strip()


def pedir_texto(mensaje):
    """Pide un texto al usuario y no acepta valores vacios."""
    texto = input(mensaje).strip()
    while texto == "":
        print("Error: este campo no puede quedar vacio.")
        texto = input(mensaje).strip()
    return texto


def pedir_datos_post():
    """Pide los datos de un nuevo post y los retorna en un diccionario."""
    titulo = pedir_texto("Titulo: ")
    contenido = pedir_texto("Contenido: ")
    tags_texto = pedir_texto("Tags separados por coma: ")
    tags = [t.strip().lower() for t in tags_texto.split(",") if t.strip()]

    estado = input(f"Estado {ESTADOS_POST} [borrador]: ").strip().lower() or "borrador"
    while estado not in ESTADOS_POST:
        print(f"Error: el estado debe ser uno de {ESTADOS_POST}.")
        estado = input(f"Estado {ESTADOS_POST} [borrador]: ").strip().lower() or "borrador"

    return {"titulo": titulo, "contenido": contenido, "tags": tags, "estado": estado}
