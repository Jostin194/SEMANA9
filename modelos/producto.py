class Producto:
    """Representa un producto del restaurante (código, nombre, categoría y precio)."""

    def __init__(self, codigo: str, nombre: str, categoria: str,
                 precio: float, disponible: bool = True) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.disponible: bool = disponible

        # Atributo encapsulado para el precio
        self.__precio: float = 0.0
        self.cambiar_precio(precio)

    def obtener_precio(self) -> float:
        return self.__precio

    def cambiar_precio(self, nuevo_precio: float) -> None:
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f"[ERROR] El precio de '{self.nombre}' debe ser mayor a 0. Operación rechazada.")

    def mostrar_informacion(self) -> str:
        estado = "Disponible" if self.disponible else "Agotado"
        return (f"[{self.codigo}] Producto: {self.nombre:<18} | "
                f"Cat: {self.categoria:<10} | Precio: ${self.obtener_precio():.2f} | Estado: {estado}")

    def __str__(self) -> str:
        return self.mostrar_informacion()