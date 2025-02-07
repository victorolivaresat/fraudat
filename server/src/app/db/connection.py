from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os


# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Construir la URL de conexión a la base de datos
DATABASE_URL = (
    f"postgresql://{os.getenv('DATABASE_USER')}:"
    f"{os.getenv('DATABASE_PASSWORD')}"
    f"@{os.getenv('DATABASE_HOST')}:"
    f"{os.getenv('DATABASE_PORT')}/"
    f"{os.getenv('DATABASE_NAME')}"
)

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL, echo=True)


# Función para inicializar la base de datos
def init_db():
    # Crear las tablas en la base de datos
    SQLModel.metadata.create_all(engine)


# Crear una sesión de base de datos
def get_session():
    with Session(engine) as session:
        yield session
