"""Clases principales del sistema: Autor, Post y Blog."""

from blog.validaciones import validar_post


class Autor:
    """Representa a una persona autora del blog."""

    def __init__(self, nombre, bio="", email=""):
        self.nombre = nombre
        self.bio = bio
        self.email = email

    def to_dict(self):
        """Convierte el autor en un diccionario compatible con JSON."""
        return {"nombre": self.nombre, "bio": self.bio, "email": self.email}

    @classmethod
    def from_dict(cls, datos):
        """Crea un Autor a partir de un diccionario.

        Lanza ValueError si el diccionario no es valido o le falta el nombre.
        """
        if not isinstance(datos, dict):
            raise ValueError("los datos del autor no son un diccionario")
        if "nombre" not in datos:
            raise ValueError("al autor le falta la clave 'nombre'")
        return cls(datos["nombre"], datos.get("bio", ""), datos.get("email", ""))

    def __str__(self):
        return self.nombre


class Post:
    """Representa una publicacion del blog. El autor es un objeto Autor."""

    CLAVES_REQUERIDAS = ("id", "titulo", "contenido", "autor", "tags", "estado")

    def __init__(self, id, titulo, contenido, autor, tags=None, estado="borrador"):
        # Composicion: el post debe tener un objeto Autor, no un texto
        if not isinstance(autor, Autor):
            raise TypeError("el autor de un post debe ser una instancia de Autor")
        self.id = id
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.tags = tags if tags is not None else []
        self.estado = estado

    def tiene_tag(self, tag):
        """Indica si el post tiene la etiqueta (ignora mayusculas)."""
        return tag.lower() in [t.lower() for t in self.tags]

    def to_dict(self):
        """Convierte el post (y su autor) en un diccionario compatible con JSON."""
        return {
            "id": self.id,
            "titulo": self.titulo,
            "contenido": self.contenido,
            "autor": self.autor.to_dict(),
            "tags": list(self.tags),
            "estado": self.estado,
        }

    @classmethod
    def from_dict(cls, datos):
        """Crea un Post a partir de un diccionario cargado desde JSON.

        Lanza ValueError si el diccionario esta incompleto o es invalido.
        """
        if not isinstance(datos, dict):
            raise ValueError("el post no es un diccionario")
        faltantes = [c for c in cls.CLAVES_REQUERIDAS if c not in datos]
        if faltantes:
            raise ValueError("faltan las claves " + ", ".join(faltantes))
        autor = Autor.from_dict(datos["autor"])
        tags = datos["tags"] if isinstance(datos["tags"], list) else [str(datos["tags"])]
        return cls(datos["id"], datos["titulo"], datos["contenido"], autor, tags, datos["estado"])

    def __str__(self):
        titulo = self.titulo or "(sin titulo)"
        return f"[{self.id}] {titulo} | Autor: {self.autor} | Estado: {self.estado}"


class Blog:
    """Centraliza la logica del sistema y guarda la lista de objetos Post."""

    def __init__(self, nombre, posts=None):
        self.nombre = nombre
        self.posts = []
        for post in posts or []:
            self.agregar_post(post)

    def agregar_post(self, post):
        """Agrega un objeto Post a la lista del blog."""
        if not isinstance(post, Post):
            raise TypeError("solo se pueden agregar objetos Post al blog")
        self.posts.append(post)

    def obtener_posts(self):
        """Retorna todos los posts cargados."""
        return self.posts

    def listar_posts(self):
        """Retorna una lista de textos con titulo, autor y estado de cada post."""
        return [str(post) for post in self.posts]

    def buscar_por_titulo(self, termino):
        """Retorna los posts cuyo titulo contiene el termino (ignora mayusculas)."""
        termino = termino.lower()
        return [p for p in self.posts if termino in p.titulo.lower()]

    def filtrar_por_tag(self, tag):
        """Retorna los posts que tienen la etiqueta indicada (ignora mayusculas)."""
        return [p for p in self.posts if p.tiene_tag(tag)]

    def siguiente_id(self):
        """Calcula el id del proximo post."""
        ids = [p.id for p in self.posts if isinstance(p.id, int)]
        return max(ids, default=0) + 1

    def crear_post(self, titulo, contenido, autor, tags, estado="borrador"):
        """Crea un nuevo objeto Post, lo agrega al blog y lo retorna."""
        post = Post(self.siguiente_id(), titulo, contenido, autor, tags, estado)
        self.agregar_post(post)
        return post

    def validar_posts(self):
        """Retorna una lista de tuplas (post, errores) para cada post."""
        return [(post, validar_post(post)) for post in self.posts]

    def to_list(self):
        """Convierte todos los posts en una lista de diccionarios."""
        return [post.to_dict() for post in self.posts]
