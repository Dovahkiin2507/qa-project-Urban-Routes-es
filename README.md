# Urban Routes - Pruebas Automatizadas

# Urban Routes – Automatización de pruebas para solicitud de taxi (Sprint 8)

Este proyecto automatiza el flujo de pedido de taxi en la versión web de Urban Routes. Se desarrolla como parte de un ejercicio práctico de QA para verificar que todo el proceso de reserva de un viaje funcione correctamente desde el punto de vista del usuario.

## 🧪 Contexto del proyecto

El equipo de desarrollo entregó una versión funcional de la aplicación Urban Routes. La tarea fue automatizar, en un entorno realista, el proceso de solicitud de un taxi, asegurando que todas las funcionalidades clave estén operativas: seleccionar tarifa, ingresar los datos del usuario, agregar una tarjeta de crédito, personalizar la solicitud y finalizar el viaje.

La automatización incluye una prueba end-to-end que simula el comportamiento del usuario paso a paso.

## ⚙️ Tecnologías utilizadas

- **Python 3.x**
- **Selenium WebDriver** (automatización del navegador)
- **pytest** (ejecución de pruebas)
- **ChromeDriver** (navegador utilizado en pruebas)
- **Git** y **GitHub** (control de versiones y entrega)

## 🗂️ Estructura del repositorio

- `main.py`: contiene las pruebas automatizadas principales dentro de la clase `TestUrbanRoutes`.
- `urban_routes_page.py`: contiene la clase `UrbanRoutesPage` con los métodos y localizadores necesarios para interactuar con los elementos de la página.
- `data.py`: contiene la URL base del servidor.
- `retrieve_phone_code.py`: función preparada para interceptar el código SMS necesario para validar la tarjeta.
- `.gitignore`: para evitar subir archivos innecesarios al repositorio.
- `README.md`: este archivo de documentación.

## ▶️ Cómo ejecutar las pruebas

1. Clona el repositorio:

   ```
   git clone https://github.com/Dovahkiin2507/qa-project-Urban-Routes-es.git
   cd qa-project-Urban-Routes-es
   ```
2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
3.Asegúrate de que data.py contenga la URL base del servidor entregado por la plataforma.

4.Ejecuta las pruebas:
   ```
   pytest main.py
   ```
💡 Recomendación: usa un entorno virtual para mantener organizadas tus dependencias.

##✅ Funcionalidades probadas
Configurar dirección de recogida.

Seleccionar tarifa “Comfort”.

Ingresar número de teléfono.

Agregar una tarjeta de crédito (con cambio de enfoque en el campo CVV).

Escribir mensaje para el conductor.

Solicitar manta y pañuelos.

Pedir 2 helados.

Confirmar solicitud y esperar la asignación del conductor.

##📌 Conclusión
Este proyecto demuestra cómo automatizar un flujo complejo de interacción de usuario en una aplicación web. Las pruebas se ejecutan correctamente, simulando de forma realista el proceso de solicitud de un taxi. Se verificó el correcto funcionamiento de cada paso del proceso, así como las interacciones con formularios, modales y validaciones. Esta práctica refuerza habilidades fundamentales de automatización para entornos reales de trabajo en QA.
