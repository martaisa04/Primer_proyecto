from sqlalchemy.orm import Session
from app.models.conversacion import Conversacion
from app.schemas.conversacion import ConversacionCreate
from datetime import datetime


def crear_conversacion(db: Session, data: ConversacionCreate):
    conv = Conversacion(
        titulo=data.titulo,
        usuario_id=data.usuario_id
    )
    db.add(conv)
    db.commit()
    db.refresh(conv)
    return conv

def listar_conversaciones_por_usuario(db: Session, usuario_id: int):
    return db.query(Conversacion).filter(
        Conversacion.usuario_id == usuario_id
    ).all()



def cerrar_conversacion(db: Session, conversacion_id: int):
    conv = db.query(Conversacion).filter(
        Conversacion.id == conversacion_id,
        Conversacion.activa == True
    ).first()

    if not conv:
        return None

    conv.activa = False
    conv.cerrada_en = datetime.utcnow()

    db.commit()
    db.refresh(conv)

    return conv