from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class ImageBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    imageName: Optional[str] = None
    imageUrl: Optional[str] = None
    imageSize: Optional[str] = None
    fileType: Optional[str] = None
    uploaderId: Optional[int] = None
    createTime: Optional[datetime] = None
    tag: Optional[str] = None
    views: Optional[int] = None

class ImageCreate(ImageBase):
    userId: int

class ImageResponse(ImageBase):
    imageId: int
    userId: int