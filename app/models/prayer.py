from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Prayer(Base):
    __tablename__ = "prayers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    category = Column(String, index=True)
