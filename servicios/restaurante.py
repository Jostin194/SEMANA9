from typing import Dict, List, Optional, Set

from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """
    Servicio encargado de administrar las colecciones y las operaciones
    del sistema (productos y usuarios). Concentra toda la lógica de
    registro, búsqueda, actualización, eliminación y listado.
    """

    def __init__(self, nombre_restaurante: str) -> None:
        self.nombre_restaurante: str = nombre_restaurante

        # Lista
        self.lista_productos: List[Producto] = []
        self.lista_usuarios: List[Usuario] = []

    # ------------------------------------------------------------------
    # PRODUCTOS
    # ------------------------------------------------------------------
    def registrar_producto(self, producto: Producto) -> bool:
        # Evita códigos de producto duplicados
        if self.buscar_producto(producto.codigo) is not None:
            print(f"\n[ERROR] Ya existe un producto registrado con el código '{producto.codigo}'.")
            return False
        self.lista_productos.append(producto)
        print(f"\n[EXITO] Producto '{producto.nombre}' registrado correctamente.")
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for producto in self.lista_productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None,
                             categoria: Optional[str] = None,
                             precio: Optional[float] = None) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            print(f"\n[ERROR] No existe un producto con el código '{codigo}'.")
            return False

        if nombre:
            producto.nombre = nombre
        if categoria:
            producto.categoria = categoria
        if precio is not None:
            producto.cambiar_precio(precio)

        print(f"\n[EXITO] Producto '{codigo}' actualizado correctamente.")
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            print(f"\n[ERROR] No existe un producto con el código '{codigo}'.")
            return False
        self.lista_productos.remove(producto)
        print(f"\n[EXITO] Producto '{codigo}' eliminado correctamente.")
        return True

    def listar_productos(self) -> None:
        print("=" * 75)
        print(f" LISTADO DE PRODUCTOS - {self.nombre_restaurante.upper()} ".center(75, "="))
        print("=" * 75)
        if not self.lista_productos:
            print("No hay productos registrados en el menú actualmente.")
        else:
            for producto in self.lista_productos:
                print(producto.mostrar_informacion())
        print("=" * 75)

    def obtener_categorias(self) -> Set[str]:
        return {producto.categoria for producto in self.lista_productos}

    def mostrar_categorias(self) -> None:
        categorias = self.obtener_categorias()
        print("=" * 75)
        print(" CATEGORÍAS DE PRODUCTOS REGISTRADAS ".center(75, "="))
        print("=" * 75)
        if not categorias:
            print("No hay categorías registradas todavía.")
        else:
            for categoria in sorted(categorias):
                print(f"- {categoria}")
        print("=" * 75)

    # ------------------------------------------------------------------
    # USUARIOS
    # ------------------------------------------------------------------
    def registrar_usuario(self, usuario: Usuario) -> bool:
        # Evita identificaciones de usuario duplicadas
        for u in self.lista_usuarios:
            if u.identificacion == usuario.identificacion:
                print(f"\n[ERROR] Ya existe un usuario registrado con la identificación "
                      f"'{usuario.identificacion}'.")
                return False
        self.lista_usuarios.append(usuario)
        print(f"\n[EXITO] Usuario '{usuario.nombre}' registrado correctamente.")
        return True

    def listar_usuarios(self) -> None:
        print("=" * 75)
        print(" LISTADO DE USUARIOS REGISTRADOS ".center(75, "="))
        print("=" * 75)
        if not self.lista_usuarios:
            print("No hay usuarios registrados en el sistema.")
        else:
            for usuario in self.lista_usuarios:
                print(usuario.mostrar_informacion())
        print("=" * 75)