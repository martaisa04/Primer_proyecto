from fastapi import FastAPI
from app.database import engine
from app.base import Base
from app.models import Usuario
from app.routes.conversacion import router as conversacion_router
from app.routes.mensaje import router as mensaje_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(conversacion_router)
app.include_router(mensaje_router)

# 👇 ACTIVO
Base.metadata.create_all(bind=engine)

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente "}

@app.get("/db-test")    
def test_db():
    engine.connect()
    return {"status": "Conectado a PostgreSQL"}