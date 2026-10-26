"""Archivo principal: coordina el flujo del blog por consola."""

from blog.datos import posts
from blog.menu import mostrar_menu, pedir_texto
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_posts


def main():
    print("Bienvenido al Blog por Consola")
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            listar_posts(posts)
        elif opcion == "2":
            termino = pedir_texto("Termino a buscar: ")
            listar_posts(buscar_por_titulo(posts, termino))
        elif opcion == "3":
            tag = pedir_texto("Tag a filtrar: ")
            listar_posts(filtrar_por_tag(posts, tag))
        elif opcion == "4":
            validar_posts(posts)
        elif opcion == "5":
            print("Gracias por usar el blog. Hasta luego!")
            break
        else:
            print("Opcion invalida. Ingresa un numero del 1 al 5.")


if __name__ == "__main__":
    main()
