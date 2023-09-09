from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class MapBase(BaseModel):
    longitude: float = Field(..., description="Longitude of the location", example=126.9780)
    latitude: float = Field(..., description="Latitude of the location", example=37.5665)
    Region: str = Field(..., max_length=10, description="Region of the location", example="Seoul")
    Country: str = Field(..., max_length=10, description="Country where the location is situated", example="South Korea")
    City: str = Field(..., max_length=10, description="City of the location", example="Seoul")
    State: str = Field(..., max_length=10, description="State of the location", example="Gangnam")
    Area: str = Field(..., max_length=10, description="Area of the location", example="Samseong-dong")

class MapCreate(MapBase):
    pass

class MapResponse(MapBase):
    mapId: int = Field(..., description="Unique identifier for the map")
    imageId: int = Field(..., description="Unique identifier for the associated image")
