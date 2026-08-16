# Sistema de Gestión de Restaurante (restaurante_app)
**Nombre:** Jostin Steeven Villalta Coello

## Descripción del Sistema Desarrollado
Solución basada en el diseño de un sistema modular de gestión de restaurante utilizando los principios de la Programación Orientada a Objetos (POO) en Python y aplicando de forma práctica el principio de Responsabilidad Única. El sistema evoluciona esta semana desde el manejo de objetos individuales hacia la **administración organizada de colecciones de objetos y datos**, incorporando de manera funcional y justificada las cuatro estructuras de datos fundamentales de Python: `list`, `tuple`, `dict` y `set`.

En esta versión, el sistema permite registrar, buscar, actualizar, eliminar y listar productos del menú, así como registrar y listar usuarios generales del sistema, almacenando los datos en tiempo real mediante un servicio de administración centralizado que garantiza la integridad de la información mediante validaciones de unicidad para evitar registros duplicados.

**Estructura:** Desarrollado bajo un esquema modular estructurado dentro de la carpeta principal `restaurante_app/`, distribuyendo sus componentes en los paquetes `modelos/`, `servicios/` y el script de arranque principal `main.py`.

### Componentes de los Modelos (`modelos/`):
* **Clase Producto (`producto.py`):** Clase que representa un artículo del menú del restaurante. Define atributos esenciales fuertemente tipados (`codigo: str`, `nombre: str`, `categoria: str` y `disponible: bool`). Incorpora un mecanismo de encapsulamiento para el precio (`__precio`) con métodos de acceso seguro (`obtener_precio`, `cambiar_precio`) que validan rigurosamente que el valor sea estrictamente mayor a cero antes de actualizarlo. Implementa el método común `mostrar_informacion()`.
* **Clase Usuario (`usuario.py`):** Clase general que representa a cualquier persona registrada en el sistema, sin implementar todavía una jerarquía adicional de tipos de usuario. Contiene los atributos `identificacion: str`, `nombre: str` y `correo: str`, además de su propio método `mostrar_informacion()` para visualizar su información de forma estructurada.

### Componentes del Servicio (`servicios/`):
* **Clase Restaurante (`restaurante.py`):** Representa la capa lógica y de negocio que administra de forma centralizada las colecciones de datos en memoria. Mantiene una **lista** independiente para productos (`lista_productos: List[Producto]`) y otra para usuarios (`lista_usuarios: List[Usuario]`). Proporciona los métodos para registrar, **buscar**, **actualizar** y **eliminar** productos aplicando validaciones de unicidad (evita la duplicación de códigos de productos y de identificaciones de usuarios), listar los registros de forma formateada, y obtener las categorías únicas de productos mediante un **conjunto (`set`)**.

### Punto de Entrada (`main.py`):
* **Flujo y Control de Ejecución:** Archivo de arranque del software. Implementa un menú interactivo infinito (`while True`) ejecutado desde consola que guía al usuario a través de nueve opciones numéricas, representadas mediante una **tupla** estable (`OPCIONES_MENU`). Cada opción del menú se organiza mediante **funciones independientes**, asociadas a través de un **diccionario** (`acciones`) que relaciona cada clave con su función correspondiente, evitando concentrar la interacción en una cadena extensa de condicionales. Se encarga de capturar las entradas del teclado mediante `input()`, realizar el casteo seguro de datos, instanciar los objetos correspondientes y delegar su registro y consulta al servicio `Restaurante`, controlando potenciales excepciones de entrada mediante bloques `try-except`.

## Estructuras de Datos Aplicadas

* **Lista (`list`):** Utilizada en `lista_productos` y `lista_usuarios` dentro de `Restaurante`, para administrar colecciones dinámicas de objetos que crecen y cambian durante la ejecución mediante operaciones de registro, búsqueda, actualización, eliminación y listado.
* **Tupla (`tuple`):** Utilizada en `OPCIONES_MENU` dentro de `main.py`, para representar las opciones del menú principal como información estable que no se modifica durante la ejecución del programa.
* **Diccionario (`dict`):** Utilizado en la variable `acciones` dentro de `main()`, asociando cada opción del menú (clave) con la función que la resuelve (valor), permitiendo un despacho ordenado de funcionalidades.
* **Conjunto (`set`):** Utilizado en el método `obtener_categorias()` de `Restaurante`, para obtener y presentar las categorías de productos registrados sin elementos duplicados.

## Principios SOLID Aplicados

* **S — Responsabilidad Única (Single Responsibility Principle):** Cada archivo y clase del proyecto cumple un único propósito. Las clases en `modelos/` representan y validan datos, la clase en `servicios/` gestiona las colecciones y las reglas de negocio, y `main.py` actúa exclusivamente como la interfaz de usuario en consola.
* **O — Abierto/Cerrado (Open/Closed Principle):** La clase `Restaurante` puede extenderse con nuevas operaciones sobre las colecciones (como las funciones de búsqueda, actualización y eliminación agregadas esta semana) sin necesidad de alterar la estructura interna de las clases `Producto` o `Usuario`.
* **D — Inversión de Dependencias (Dependency Inversion aplicada al diseño):** `main.py` no manipula directamente las listas internas del servicio; depende únicamente de los métodos públicos que expone `Restaurante`, manteniendo desacoplada la interfaz de consola de la lógica de almacenamiento.


## Reflexión sobre el Diseño de Software Modular

### Importancia de Seleccionar la Estructura de Datos Adecuada

* **Elección Justificada de Estructuras:** Cada estructura de datos utilizada cumple una función concreta dentro del programa y no solo demuestra su sintaxis: la lista administra colecciones que cambian, la tupla protege información estable, el diccionario expresa una relación directa clave-valor, y el conjunto garantiza unicidad sin lógica adicional.
* **Integridad y Validación en Tiempo Real:** Al capturar los datos desde `input()` y canalizarlos inmediatamente a través de los constructores y métodos de validación, el sistema actúa como una primera línea de defensa, rechazando de manera preventiva precios inválidos (menores o iguales a cero) o registros duplicados (códigos de producto e identificaciones de usuario) antes de persistirlos en las listas del servicio.
* **Acoplamiento Débil y Cohesión Alta:** La separación entre la interfaz de usuario (`main.py`), la lógica de negocio (`restaurante.py`) y las entidades (`modelos/`) asegura que los cambios en la forma en que se presentan los datos o se capturan no afecten las reglas de negocio, y viceversa.
* **Organización mediante Funciones y Diccionarios:** El uso de funciones independientes por cada opción del menú, asociadas mediante un diccionario, evita una cadena extensa de condicionales y hace que el programa sea significativamente más limpio, legible y fácil de escalar en el futuro.
* **Adherencia a Estándares Profesionales:** Todo el código y estructura del proyecto siguen de manera estricta las convenciones de estilo PEP 8 (uso de *PascalCase* para clases, *snake_case* para variables y funciones, y anotaciones explícitas de tipos de datos), garantizando que el software sea autodocumentado y fácil de mantener por otros desarrolladores.