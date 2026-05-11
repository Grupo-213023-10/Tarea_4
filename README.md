# Tarea_4
Curso de Programación

# Sistema Integral de Gestión - SOFTWARE FJ

## Descripción

Este proyecto consiste en un sistema integral de gestión desarrollado en Python para administrar clientes, servicios y reservas de una empresa llamada SOFTWARE FJ.

El sistema permite:

- Registrar clientes
- Crear servicios
- Gestionar reservas
- Confirmar y cancelar reservas
- Procesar pagos
- Aplicar impuestos y descuentos
- Registrar eventos en logs

## Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos
- Manejo de excepciones
- Clases abstractas
- Encapsulamiento
- Herencia
- Polimorfismo
- Logging

## Clases principales

### Cliente
Gestiona la información de los clientes.

### Servicio
Clase abstracta base para los servicios.

### ReservaSala
Permite reservar salas por horas.

### AlquilerEquipo
Permite alquilar equipos por días.

### AsesoriaEspecializada
Gestiona asesorías por horas.

### Reserva
Administra el proceso completo de reserva.
## Conceptos de Programación Orientada a Objetos aplicados

### Encapsulamiento
Se utilizaron atributos privados en la clase Cliente.

### Herencia
Las clases ReservaSala, AlquilerEquipo y AsesoriaEspecializada heredan de Servicio.

### Polimorfismo
Cada servicio implementa su propio método calcular_costo().

### Abstracción
Se implementaron clases abstractas mediante ABC y abstractmethod.

## Manejo de excepciones

El sistema implementa excepciones personalizadas:

- ClienteError
- ServicioError
- ReservaError

Además, se usa try, except y finally para controlar errores y garantizar estabilidad.

## Registro de logs

El sistema almacena eventos y errores en el archivo:

logs.txt

## Ejecución del programa

1. Abrir el proyecto en Visual Studio Code
2. Ejecutar el archivo principal
3. Ingresar los datos solicitados en consola

## Ejemplo de salida

===== FACTURA =====
Cliente: Juan
Servicio: Reserva de sala
Estado: Confirmada
Total a pagar: $84000

## Autor

Emilson Aguilar Feria