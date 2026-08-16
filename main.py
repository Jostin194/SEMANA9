from typing import Callable, Dict

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario

# Tupla: opciones del menú principal
OPCIONES_MENU: tuple = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir",
)


def mostrar_menu() -> None:
    print("\n" + "=" * 45)
    print("SISTEMA DE RESTAURANTE".center(45))
    print("=" * 45)
    for indice, opcion in enumerate(OPCIONES_MENU, start=1):
        print(opcion)
        if indice in (5, 7):
            print("-" * 45)
    print("=" * 45)


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto: ").strip()
    nombre = input("Ingrese el nombre del producto: ").strip()
    categoria = input("Ingrese la categoría: ").strip()
    try:
        precio = float(input("Ingrese el precio: "))
        nuevo_producto = Producto(codigo, nombre, categoria, precio)
        restaurante.registrar_producto(nuevo_producto)
    except ValueError:
        print("\n[ERROR] El precio debe ser un número válido.")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- BUSCAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a buscar: ").strip()
    producto = restaurante.buscar_producto(codigo)
    if producto is not None:
        print(f"\n{producto.mostrar_informacion()}")
    else:
        print(f"\n[ERROR] No se encontró ningún producto con el código '{codigo}'.")


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- ACTUALIZAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a actualizar: ").strip()
    nombre = input("Nuevo nombre (Enter para mantener el actual): ").strip()
    categoria = input("Nueva categoría (Enter para mantener la actual): ").strip()
    precio_texto = input("Nuevo precio (Enter para mantener el actual): ").strip()
    try:
        precio = float(precio_texto) if precio_texto else None
        restaurante.actualizar_producto(
            codigo,
            nombre=nombre or None,
            categoria=categoria or None,
            precio=precio,
        )
    except ValueError:
        print("\n[ERROR] El precio debe ser un número válido.")


def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n--- ELIMINAR PRODUCTO ---")
    codigo = input("Ingrese el código del producto a eliminar: ").strip()
    restaurante.eliminar_producto(codigo)


def listar_productos(restaurante: Restaurante) -> None:
    print()
    restaurante.listar_productos()


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- REGISTRAR USUARIO ---")
    identificacion = input("Ingrese la identificación (Cédula/RUC): ").strip()
    nombre = input("Ingrese el nombre completo del usuario: ").strip()
    correo = input("Ingrese el correo electrónico: ").strip()
    if identificacion and nombre and correo:
        nuevo_usuario = Usuario(identificacion, nombre, correo)
        restaurante.registrar_usuario(nuevo_usuario)
    else:
        print("\n[ERROR] Todos los campos son obligatorios para registrar un usuario.")


def listar_usuarios(restaurante: Restaurante) -> None:
    print()
    restaurante.listar_usuarios()


def mostrar_categorias(restaurante: Restaurante) -> None:
    print()
    restaurante.mostrar_categorias()


def salir(restaurante: Restaurante) -> None:
    print("\n¡Gracias por utilizar el Sistema de Restaurante! Saliendo...")


def main() -> None:
    mi_restaurante = Restaurante("Restaurante de Mariscos")

    # Diccionario
    acciones: Dict[str, Callable[[Restaurante], None]] = {
        "1": registrar_producto,
        "2": buscar_producto,
        "3": actualizar_producto,
        "4": eliminar_producto,
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": mostrar_categorias,
        "9": salir,
    }

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        accion = acciones.get(opcion)
        if accion is None:
            print("\n[ERROR] Opción no válida. Por favor, intente de nuevo.")
            continue

        accion(mi_restaurante)

        if opcion == "9":
            break


if __name__ == "__main__":
    main()