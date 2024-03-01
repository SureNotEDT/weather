from database import Base
from sqlalchemy import String, Column, Numeric


class Users(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    lat = Column(Numeric, nullable=False)
    lon = Column(Numeric, nullable=False)