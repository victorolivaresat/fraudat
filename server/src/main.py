from fastapi import FastAPI
from database import init_db
from server.src.app.routes.user_routes import router as user_router

app = FastAPI()


# Inicializar base de datos al iniciar
@app.lifespan("startup")
def startup():
    init_db()


# Montar rutas
app.include_router(user_router)


# Ruta de prueba
@app.get("/")
async def root():
    return {"message": "¡Hola desde FastAPI!"}
