from sqlalchemy.orm import Session
from . import model, schema

def get_map_byId(db: Session, mapId: int):
    return db.query(model.Map).filter(model.Map.mapId == mapId).first()

def get_map_byGps(db: Session, longitude: float, latitude: float):
    return db.query(model.Map).filter(model.Map.longitude == longitude and \
                                      model.Map.latitude == latitude).first()
def create_map(db: Session, map: schema.MapCreate):
    db_map = model.Map(
        # imageId = map.imageId,  # 이 부분은 imageId를 어떻게 얻느냐에 따라 변경이 필요할 수 있습니다.
        longitude = map.longitude,
        latitude = map.latitude,
        Region = map.Region,
        Country = map.Country,
        City = map.City,
        State = map.State,
        Area = map.Area
    )

    db.add(db_map)
    db.commit()
    db.refresh(db_map)
    return db_map

def get_maps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Map).all()