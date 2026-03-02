from sqlalchemy.orm import Session
from app.models.mensaje import Mensaje
from app.models.conversacion import Conversacion
from app.schemas.mensaje import MensajeCreate

def guardar_mensaje(db: Session, data: MensajeCreate):
    # 1️⃣ Buscar la conversación
    conversacion = db.query(Conversacion).filter(
        Conversacion.id == data.conversacion_id
    ).first()

    if not conversacion:
        return None

    # 2️⃣ Verificar si está activa
    if conversacion.activa is not True:
        return None

    # 3️⃣ Guardar mensaje
    msg = Mensaje(
        conversacion_id=data.conversacion_id,
        contenido=data.contenido,
        rol=data.rol
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg


def historial_por_conversacion(db: Session, conversacion_id: int):
    return db.query(Mensaje).filter(
        Mensaje.conversacion_id == conversacion_id
    ).order_by(Mensaje.creado_en).all()