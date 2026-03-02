from pydantic import BaseModel
from datetime import datetime

class MensajeCreate(BaseModel):
    conversacion_id: int
    contenido: str
    rol: str  # user / assistant

class MensajeResponse(BaseModel):
    id: int
    conversacion_id: int
    contenido: str
    rol: str
    creado_en: datetime

    class Config:
        from_attributes = True