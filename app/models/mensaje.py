from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.base import Base

class Mensaje(Base):
    __tablename__ = "mensajes"

    id = Column(Integer, primary_key=True, index=True)

    conversacion_id = Column(
        Integer,
        ForeignKey("conversaciones.id"),
        nullable=False
    )

    # contenido del mensaje (texto libre)
    contenido = Column(Text, nullable=False)

    # quién envía el mensaje: user / assistant
    rol = Column(String(20), nullable=False)

    # fecha de creación del mensaje
    creado_en = Column(DateTime, default=datetime.utcnow)

    # relación con conversación
    conversacion = relationship(
        "Conversacion",
        back_populates="mensajes"
    )