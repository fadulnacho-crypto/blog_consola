"""Menu e interaccion con el usuario (manejo de input)."""


def mostrar_menu():
    """Muestra las opciones y retorna la opcion elegida por el usuario."""
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")
    return input("Elegi una opcion: ").strip()


def pedir_texto(mensaje):
    """Pide un texto al usuario y no acepta valores vacios."""
    texto = input(mensaje).strip()
    while texto == "":
        print("El valor no puede estar vacio.")
        texto = input(mensaje).strip()
    return texto
