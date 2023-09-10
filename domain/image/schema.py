from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional

class ImageBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    imageName: Optional[str] = Field(None, example="Sample Image")
    imageUrl: Optional[str] = Field(None, example="http://example.com/sample.jpg")
    imageSize: Optional[str] = Field(None, example="1024x768")
    fileType: Optional[str] = Field(None, example="jpg")
    uploaderId: Optional[int] = Field(None, example=123)
    createTime: Optional[datetime] = Field(None, example="2023-09-01T00:00:00")
    tag: Optional[str] = Field(None, example="sample")
    views: Optional[int] = Field(None, example=100)

class ImageCreate(ImageBase):
    userId: int = Field(..., example=1)

class ImageResponse(ImageBase):
    imageId: int
    userId: int