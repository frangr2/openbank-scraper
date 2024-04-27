# openbank-scraper

## Scraper de Fondos Indexados en el Sitio Web de Openbank

Este proyecto de Python es un web scraper diseñado para extraer información financiera de fondos indexados de un sitio web específico. Utiliza Playwright para automatizar la navegación web y sigue el modelo de Page Object para organizar el código de manera eficiente.

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

1. Ejecuta el script principal para iniciar el scraper:

    ```bash
    python scraper.py
    ```

2. El scraper automatizará la navegación web y extraerá la información financiera de los fondos indexados del sitio web objetivo.

### Estructura del Proyecto

- `scraper.py`: El script principal que contiene la lógica del scraper.
- `poms/`: Directorio que contiene los Page Objects utilizados para interactuar con las páginas web.
- `utils/`: Directorio que contiene utilidades auxiliares para el proyecto.

### Contribuyendo

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad: `git checkout -b feature/nueva-funcionalidad`.
3. Realiza tus cambios y haz commits describiendo tus modificaciones siguiendo [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/): `git commit -m '<type>[optional scope]: <description>'`.
4. Sube tus cambios a tu repositorio: `git push origin feature/nueva-funcionalidad`.
5. Envía un pull request para que revisemos tus cambios.

### Soporte

Si tienes preguntas, problemas o sugerencias, por favor abre un issue en este repositorio.

### Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
