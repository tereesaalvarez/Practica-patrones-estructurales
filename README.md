# Practica-patrones-estructurales

# Ejercicio 1 - Pizzeria Delizioso

# Clases y Módulos

### PizzaBuilder
- `PizzaBuilder`: Interfaz base para constructores de pizzas con métodos abstractos.
- `Director`: Clase que utiliza un `PizzaBuilder` para construir pizzas completas.

### Pizzas Concretas
- Clases que implementan constructores concretos de pizzas: `BarbacoaBuilder`, `CuatroQuesosBuilder`, `HawaianaBuilder`, `JamonyQuesoBuilder`, `MargaritaBuilder`, `VegetarianaBuilder`, `PersonalizadaBuilder`.

### PizzaComposite
- `Component`: Interfaz base para `Leaf` y `Composite`.
- `Leaf`: Clase que representa elementos individuales (pizzas individuales).
- `Composite`: Clase que representa composiciones de elementos (menús).

### Menú
- `Menu`: Clase que representa un menú especializado que puede contener pizzas individuales o menús compuestos.

### CSVHandler
- Funciones para guardar y cargar datos desde y hacia archivos CSV (`save_to_csv`, `read_from_csv`).
- Funciones específicas para manejar datos de pizzas y menús (`save_pizzas_to_csv`, `load_pizzas_from_csv`, `save_menus_to_csv`, `load_menus_from_csv`).

### Interfaz Gráfica (GUI)
- Clases para la interfaz gráfica con PyQt5 (`PantallaPrincipal`, `PaginaPizza`, `PaginaPersonalizada`, `PaginaMenu`).

## Funcionalidades Clave

### PizzaBuilder
- Utiliza el patrón Builder para construir pizzas de manera modular.
- Cada pizza concreta tiene su propio constructor que implementa los pasos específicos de la construcción.

### PizzaComposite
- Utiliza el patrón Composite para representar tanto pizzas individuales como menús compuestos.
- Proporciona una estructura jerárquica para organizar pizzas y menús.

### CSVHandler
- Gestiona la lectura y escritura de datos desde y hacia archivos CSV.
- Especializado en manejar datos relacionados con pizzas y menús.

### Interfaz Gráfica
- Desarrollada con PyQt5 para permitir a los usuarios interactuar con el sistema.
- Proporciona opciones para hacer pedidos de pizzas, personalizar pizzas y pedir menús.

## Flujo de la Aplicación

1. **Inicio de la Aplicación:**
   - Se crea una instancia de `PantallaPrincipal`.
   - Se muestra la página principal con opciones para hacer pedidos y personalizaciones.

2. **Pedido de Pizzas:**
   - El usuario puede seleccionar pizzas predefinidas (Barbacoa, Cuatro Quesos, etc.).
   - Se utiliza un `Director` para construir la pizza seleccionada.
   - Se añade la pizza al carrito.

3. **Personalización de Pizzas:**
   - El usuario puede personalizar su propia pizza.
   - Se utiliza el `PersonalizadaBuilder` para construir la pizza personalizada.
   - Se añade la pizza personalizada al carrito.

4. **Pedido de Menús:**
   - El usuario puede seleccionar menús predefinidos o compilar su propio menú.
   - Se utiliza el patrón Composite para construir el menú seleccionado.
   - Se añade el menú al carrito.

5. **Confirmación y Pago:**
   - El usuario revisa su carrito, confirma el pedido y realiza el pago.

## DiagramaUML

![UML]()




# Ejercicio 2 - Sistema de Gestión de Documentos

## Clases y Módulos

### Proxy
- `Subject`: Interfaz base para `RealSubject` y `Proxy`.
- `RealSubject`: Clase que realiza la operación real.
- `Proxy`: Clase proxy que controla el acceso a `RealSubject`, realiza operaciones adicionales y registra el acceso en la base de datos.

### Composite
- `Component`: Interfaz base para `Leaf` y `Carpeta`.
- `Leaf`: Clase que representa elementos individuales sin hijos.
- `Carpeta`: Clase que puede contener `Leaf`, `Carpeta` o `Link`.
- `Documento`: Clase que representa documentos específicos dentro de la estructura.
- `Link`: Clase que representa enlaces a carpetas dentro de la estructura.

### Base de Datos
- `Usuario`: Clase que modela un usuario con nombre de usuario y contraseña.
- `UsuarioDatabase`: Clase que gestiona la base de datos de usuarios y verifica la existencia de usuarios.
- `AccederDatabase`: Clase que maneja la base de datos de registros, registrando el acceso de los usuarios.

### Interfaz Gráfica
- `InterfazApp`: Clase principal que gestiona la aplicación.
- `PaginaInicio`: Página de bienvenida con botones para registro e inicio de sesión.
- `PaginaRegistro`: Página para registrar nuevos usuarios.
- `PaginaInicioSesion`: Página para iniciar sesión.
- `PaginaPrincipal`: Página principal después de iniciar sesión con una estructura de documentos.
- `main`: Punto de entrada de la aplicación.

## Funcionalidades Clave

### Proxy
- Implementa un patrón Proxy para controlar el acceso a `RealSubject` (`PaginaPrincipal`).
- Registra el acceso en la base de datos de registros.

### Composite
- Utiliza el patrón Composite para construir una estructura jerárquica de documentos.
- Permite la modificación y eliminación de elementos en la estructura.

### Base de Datos
- Utiliza SQLite para almacenar usuarios y registros.
- Registra información de usuario y acciones realizadas en la aplicación.

### Interfaz Gráfica
- Desarrollada con PyQt5 para proporcionar una interfaz intuitiva.
- Permite el registro de nuevos usuarios, inicio de sesión y manipulación de documentos.

## Flujo de la Aplicación

1. **Inicio de la Aplicación:**
   - Se crea una instancia de `InterfazApp`.
   - Se muestra la página de inicio.

2. **Registro de Usuario:**
   - Se muestra la página de registro al hacer clic en "Registro" desde la página de inicio.
   - Se ingresan los datos del usuario.
   - Se verifica la no existencia del usuario en la base de datos.
   - Se añade el usuario a la base de datos y se registra el acceso.
   - Se vuelve a la página de inicio.

3. **Inicio de Sesión:**
   - Se muestra la página de inicio de sesión al hacer clic en "Login" desde la página de inicio.
   - Se ingresan las credenciales del usuario.
   - Se verifica la existencia del usuario en la base de datos.
   - Si las credenciales son válidas, se muestra la página principal; de lo contrario, se muestra un mensaje de error.

4. **Página Principal:**
   - Muestra la estructura de documentos utilizando el patrón Composite.
   - Permite la modificación y eliminación de elementos.
   - Registra acciones realizadas por el usuario en la base de datos.

5. **Desconexión del Usuario:**
   - Al hacer clic en "Desconectar", se registra la acción y se cierra la sesión.

## Conexiones y Dependencias

- **Usuario y Base de Datos:**
  - Las clases `Usuario` y `UsuarioDatabase` manejan la información de los usuarios.
  - `AccederDatabase` registra acciones en la base de datos.

- **Interfaz Gráfica y Lógica de Aplicación:**
  - La interfaz gráfica (`PaginaInicio`, `PaginaRegistro`, `PaginaInicioSesion`, `PaginaPrincipal`) interactúa con la lógica de aplicación (`InterfazApp`).

- **Proxy y Composite:**
  - El patrón Proxy (`Proxy`) protege el acceso a la página principal (`PaginaPrincipal`), mientras que el patrón Composite se utiliza para estructurar los elementos en la página principal.

## Conclusiones

- Se ha implementado un sistema de gestión de documentos con funcionalidades de registro, inicio de sesión y manipulación de documentos.
- Se han aplicado patrones de diseño como Proxy y Composite para gestionar el acceso y la estructura de la información.
- La interfaz gráfica proporciona una experiencia de usuario intuitiva y fácil de usar.

## Diagrama UML
Se ha generado un diagrama UML para proporcionar una visualización clara de la estructura y relaciones entre clases y módulos.

![UML]()

