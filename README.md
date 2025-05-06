# openbank-scraper

## ⚠️ Aviso Importante

Este proyecto es **exclusivamente educativo** y tiene como único propósito practicar y mejorar mis habilidades de programación en Python. La elección de la web de OpenBank como objetivo del scraper se debe únicamente a un interés personal en el ámbito financiero, sin ningún otro criterio específico.

Este scraper no está destinado para uso en producción ni tiene afiliación alguna con OpenBank. Se recomienda no utilizar este código para propósitos comerciales o de producción.

## Descripción del Proyecto

Este proyecto es un ejercicio de práctica que implementa un web scraper en Python para extraer información de fondos indexados. Utiliza Playwright para automatizar la navegación web y sigue el patrón de diseño Page Object Model (POM) como ejercicio de buenas prácticas de programación.

### Objetivos de Aprendizaje

- Practicar programación en Python
- Implementar patrones de diseño (Page Object Model)
- Trabajar con bibliotecas de automatización web (Playwright)
- Manejar datos y exportación a JSON
- Aplicar principios de código limpio y modular

### Requisitos del Sistema

- Python 3.12
- pip (administrador de paquetes de Python)
- virtualenv (opcional pero recomendado)

### Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/frangr2/openbank-scraper.git
    ```

2. Crea y activa un entorno virtual (opcional pero recomendado):

    ```bash
    virtualenv -p python3 venv
    source venv\Scripts\activate   # En sistemas Linux/Mac
    venv\Scripts\activate      # En sistemas Windows
    ```

    Para salir del entorno virtual:

    ```bash
    deactivate
    ```

4. Instala las dependencias del proyecto desde el archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

### Uso

**Nota**: Este código es solo para fines educativos y de práctica. No se recomienda su uso en entornos de producción.

1. Ejecuta el script principal:

    ```bash
    python scraper.py
    ```

2. El scraper automatizará la navegación web como ejercicio de práctica.

### Estructura del Proyecto

- `scraper.py`: El script principal que contiene la lógica del scraper.
- `poms/`: Directorio que contiene los Page Objects utilizados para interactuar con las páginas web.
- `utils/`: Directorio que contiene utilidades auxiliares para el proyecto.

### Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).

### Descargo de Responsabilidad

Este proyecto es un ejercicio personal de programación y no está asociado, respaldado ni afiliado de ninguna manera con OpenBank o cualquier otra institución financiera. El autor no se hace responsable del uso que se pueda dar a este código.
