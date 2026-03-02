from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.conversacion import ConversacionCreate, ConversacionResponse
from app.crud.conversacion import crear_conversacion, cerrar_conversacion

router = APIRouter(prefix="/conversaciones", tags=["Conversaciones"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ConversacionResponse)
def crear(data: ConversacionCreate, db: Session = Depends(get_db)):
    return crear_conversacion(db, data)

@router.put("/{conversacion_id}/cerrar", response_model=ConversacionResponse)
def cerrar(
    conversacion_id: int,
    db: Session = Depends(get_db)
):
    conv = cerrar_conversacion(db, conversacion_id)

    if not conv:
        raise HTTPException(
            status_code=404,
            detail="Conversación no encontrada o ya cerrada"
        )

    return conv


from app.models.conversacion import Conversacion  # 👈 IMPORTANTE

from typing import Optional
from fastapi import Query

@router.get("/", response_model=list[ConversacionResponse])
def listar_conversaciones(
    activa: Optional[bool] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Conversacion)

    if activa is not None:
        query = query.filter(Conversacion.activa == activa)

    return query.all()