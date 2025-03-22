# Urban Routes - Pruebas Automatizadas

## Descripción del Proyecto

Este proyecto contiene un conjunto de pruebas automatizadas para la aplicación web **Urban Routes**. Las pruebas validan la funcionalidad principal de la plataforma, incluyendo la selección de rutas, la solicitud de taxis, el ingreso de datos de usuario y métodos de pago, entre otros casos clave.

## Tecnologías y Técnicas Utilizadas

- **Lenguaje:** Python
- **Framework de pruebas:** `pytest`
- **Automatización web:** Selenium WebDriver
- **Gestión de espera:** `selenium.webdriver.support.expected_conditions`
- **Manejo de logs:** API de Chrome DevTools
- **Ejecutor del navegador:** ChromeDriver

## Requisitos Previos

Antes de ejecutar las pruebas, asegúrate de tener instalado lo siguiente:

- Python 3.8 o superior
- Google Chrome (última versión recomendada)
- ChromeDriver (compatible con la versión de Chrome instalada)
- Virtualenv (opcional, pero recomendado)

## Instalación

Clona este repositorio y navega hasta el directorio del proyecto:

```
 git clone https://github.com/usuario/urban-routes-tests.git
 cd urban-routes-tests
```

Crea un entorno virtual y actívalo:

```
python -m venv env  # Para Windows: python -m venv env
source env/bin/activate  # Para Windows: env\Scripts\activate
```

Instala las dependencias necesarias:

```
pip install -r requirements.txt
```

## Ejecución de las Pruebas

Para ejecutar todas las pruebas, usa el siguiente comando:

```
pytest
```

Si deseas ejecutar pruebas específicas, usa:

```
pytest -k "nombre_de_la_prueba"
```

Para generar un reporte detallado:

```
pytest --html=report.html --self-contained-html
```

