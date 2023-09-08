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
    imageId = Column(BigInteger, ForeignKey('Image.imageId'), nullable=False)
    longitude = Column(Float(53))
    latitude = Column(Float(53))
    Region = Column(String(10))
    Country = Column(String(10))
    City = Column(String(10))
    State = Column(String(10))
    Area = Column(String(10))
    image = relationship("Image", back_populates="map")