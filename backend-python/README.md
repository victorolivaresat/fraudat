# Total Secure:tm: By apuestatotal
___

### Uso de la Aplicación con Uvicorn, FastAPI y Pyenv (opcional)

### Instalación de Pyenv
* Puedes encontrar más información y el enlace de descarga en: https://github.com/pyenv/pyenv

### Instalación de una Versión Específica de Python
* Para instalar y usar una versión específica de Python (por ejemplo, 3.9.7): 
```bash
pyenv install 3.9.7
pyenv global 3.9.7
pyenv versions
```

### Entorno virtual
* Para crear un entorno virtual en el directorio actual:
```bash
python -m venv .venv
```

### Selección de la Versión de Python en VS Code
* Para trabajar con la versión de Python del entorno virtual en VS Code:
    1. Presiona `Ctrl + Shift + P` para abrir la paleta de comandos.
    2. Escribe y selecciona `Python: Select Interpreter`.
    3. Navega a la carpeta `Scripts` dentro de `.venv` y selecciona `python.exe`.

### Instalación de Dependencias
* Instala las dependencias del proyecto:
```bash
pip install -r requirements.txt
```

### Activación del Entorno Virtual
* Para activar el entorno virtual en Windows:
```bash
.venv\Scripts\activate
```

* Para activar el entorno virtual en Unix o MacOS:
```bash
source .venv/bin/activate
```

### Ejecución de la Aplicación
* Para ejecutar la aplicación con Uvicorn:
```bash
uvicorn src.main:app --reload
```

### Comando para generar las librerías instaladas
```bash
pip freeze > requeriments.txt
```

