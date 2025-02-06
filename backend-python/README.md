# fraudat backend-python

## Uso de la Aplicación con Uvicorn, FastAPI y Pyenv (opcional)

### Instalación de Pyenv
* Puedes encontrar más información y el enlace de descarga en: https://github.com/pyenv/pyenv

### Instalación de una Versión Específica de Python
* Para instalar y usar una versión específica de Python (por ejemplo, 3.9.7): 
```bash
pyenv install 3.9.7
pyenv global 3.9.7
pyenv versions
```

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