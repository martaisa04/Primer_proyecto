from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.base import Base

class Conversacion(Base):
    __tablename__ = "conversaciones"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    # INICIO DE CONVERSACIÓN
    creada_en = Column(DateTime, default=datetime.utcnow)

    # FIN DE CONVERSACIÓN
    cerrada_en = Column(DateTime, nullable=True)

    activa = Column(Boolean, default=True)

    # relaciones
    
    usuario = relationship(
        "Usuario",
          back_populates="conversaciones")
    

    mensajes = relationship(
        "Mensaje",
        back_populates="conversacion",
        cascade="all, delete-orphan"
    )