from sqlalchemy import BigInteger, \
    Column, Float, ForeignKey, Identity, \
    PrimaryKeyConstraint, String
from sqlalchemy.orm import declarative_base, relationship

from default.config.database import Base

class Map(Base):
    __tablename__ = 'Map'
    __table_args__ = (
        PrimaryKeyConstraint('mapId', name='Map_pkey'),
    )
    mapId = Column(BigInteger, primary_key=True, nullable=False, autoincrement=True)
    imageId = Column(BigInteger, ForeignKey('Image.imageId'), nullable=True)
    longitude = Column(Float(53))
    latitude = Column(Float(53))
    Region = Column(String(10))
    Country = Column(String(100))
    City = Column(String(100))
    State = Column(String(100))
    Area = Column(String(100))
    image = relationship("Image", back_populates="map")