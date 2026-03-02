from pydantic import BaseModel
from datetime import datetime

class ConversacionCreate(BaseModel):
    titulo: str
    usuario_id: int

class ConversacionResponse(BaseModel):
    id: int
    titulo: str
    usuario_id: int
    creada_en: datetime
    fecha_fin: datetime | None = None
    activa: bool

    class Config:
        orm_mode = True