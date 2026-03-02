from sqlalchemy import Column, Integer, String
from app.base import Base

class EstadoTicket(Base):
    __tablename__ = "estados_ticket"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), nullable=False)