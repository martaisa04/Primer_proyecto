from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.deps import get_db
from app.schemas.mensaje import MensajeCreate, MensajeResponse
from app.crud.mensaje import guardar_mensaje, historial_por_conversacion
from app.models.conversacion import Conversacion
from typing import Optional
from app.models.mensaje import Mensaje

router = APIRouter(prefix="/mensajes", tags=["Mensajes"])

@router.post("/", response_model=MensajeResponse)
def crear(data: MensajeCreate, db: Session = Depends(get_db)):
    msg = guardar_mensaje(db, data)
    if not msg:
        raise HTTPException(
            status_code=400,
            detail="No se pueden agregar mensajes a una conversación cerrada o inexistente"
        )
    return msg

from datetime import datetime

@router.get("/conversacion/{conversacion_id}", response_model=list[MensajeResponse])
def historial(
    conversacion_id: int,
    rol: Optional[str] = Query(None),
    fecha_inicio: Optional[datetime] = Query(None),
    fecha_fin: Optional[datetime] = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Mensaje).filter(
        Mensaje.conversacion_id == conversacion_id
    )

    if rol:
        query = query.filter(Mensaje.rol == rol)

    if fecha_inicio:
        query = query.filter(Mensaje.creado_en >= fecha_inicio)

    if fecha_fin:
        query = query.filter(Mensaje.creado_en <= fecha_fin)

    return query.order_by(Mensaje.creado_en.asc()).all()
