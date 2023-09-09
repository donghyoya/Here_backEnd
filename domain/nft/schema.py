from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class NFTBase(BaseModel):
    name: Optional[str] = Field(None, max_length=20, description="Name of the NFT", example="NFT Artwork")
    description: Optional[str] = Field(None, description="Description of the NFT", example="This is a beautiful NFT artwork")
    imagePath: Optional[str] = Field(None, description="S3 path of the NFT image", example="s3://bucket/path/to/image.jpg")
    createDate: Optional[datetime] = Field(None, description="Creation date of the NFT")
    owner: Optional[str] = Field(None, max_length=10, description="Current owner of the NFT", example="owner123")
    bfOwner: Optional[str] = Field(None, max_length=10, description="Previous owner of the NFT", example="ownerXYZ")

