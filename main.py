"""Punto de entrada del blog por consola (Preentrega 6: POO + JSON)."""

from blog.datos import autor_por_defecto, cargar_posts, guardar_posts
from blog.menu import mostrar_menu, pedir_datos_post, pedir_texto
from blog.modelos import Blog
from blog.operaciones import mostrar_posts, mostrar_validacion


def main():
    # Cargar los posts desde posts.json y crear la instancia de Blog
    blog = Blog("Blog de Ignacio", cargar_posts())
    autor = autor_por_defecto()
    print(f"Bienvenido a '{blog.nombre}'. Posts cargados: {len(blog.obtener_posts())}")

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            mostrar_posts(blog.obtener_posts(), "Todos los posts")

        elif opcion == "2":
            termino = pedir_texto("Texto a buscar en el titulo: ")
            mostrar_posts(blog.buscar_por_titulo(termino), "Resultados")

        elif opcion == "3":
            tag = pedir_texto("Tag a filtrar: ")
            mostrar_posts(blog.filtrar_por_tag(tag), f"Posts con el tag '{tag}'")

        elif opcion == "4":
            datos = pedir_datos_post()
            post = blog.crear_post(datos["titulo"], datos["contenido"], autor,
                                   datos["tags"], datos["estado"])
            print(f"Post creado: {post}")
            print("Recorda guardar (opcion 6) para que quede en posts.json.")

        elif opcion == "5":
            mostrar_validacion(blog.validar_posts())

        elif opcion == "6":
            if guardar_posts(blog.obtener_posts()):
                print(f"Se guardaron {len(blog.obtener_posts())} posts en posts.json.")

        elif opcion == "7":
            guardar_posts(blog.obtener_posts())
            print("Cambios guardados en posts.json. Hasta luego!")
            break

        else:
            print("Opcion invalida. Ingresa un numero del 1 al 7.")


if __name__ == "__main__":
    main()
