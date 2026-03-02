from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=True)

    conversaciones = relationship(
        "Conversacion",
        back_populates="usuario"
    )