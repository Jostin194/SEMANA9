class Usuario:
    """
    Representa de forma general a una persona registrada en el sistema
    (identificación, nombre y correo). El sistema podrá evolucionar más
    adelante hacia distintos tipos de usuario, sin implementar todavía
    una jerarquía adicional.
    """

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> str:
        return (f"ID: {self.identificacion:<10} | Usuario: {self.nombre:<20} | "
                f"Correo: {self.correo}")

    def __str__(self) -> str:
        return self.mostrar_informacion()