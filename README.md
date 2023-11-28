# Practica-patrones-estructurales

crear menu (combos)

no hay que hacer builder para el menu pq peta

se reciclan las bebidas(madridaje)

hay que actualizar a poder pedir postres con la pizza y aparte los combos

generar un id para cada elemento ( cada ingrediente...)

podemos usar bases de datos(relacionales(sql)) 


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

![UML](https://github.com/tereesaalvarez/Practica-patrones-estructurales/blob/main/Ejercicio2/UML/umlbien.png?raw=true)

