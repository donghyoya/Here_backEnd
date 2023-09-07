from sqlalchemy import BigInteger, Boolean, CheckConstraint, Column, DateTime, Float, ForeignKeyConstraint, Identity, Index, Integer, PrimaryKeyConstraint, SmallInteger, String, Text, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Map(Base):
    __tablename__ = 'Map'
    __table_args__ = (
        ForeignKeyConstraint(['imageId'], ['Image.imageId'], name='FK_Image_TO_Map_1'),
        PrimaryKeyConstraint('mapid', 'imageId', name='PK_MAP')
    )

    mapid = Column(BigInteger, primary_key=True, nullable=False)
    imageId = Column(BigInteger, primary_key=True, nullable=False)
    longitude = Column(Float(53))
    latitude = Column(Float(53))
    Region = Column(Text)
    Country = Column(Text)
    City = Column(Text)
    State = Column(Text)
    Area = Column(Text)

    Image_ = relationship('Image', back_populates='Map')