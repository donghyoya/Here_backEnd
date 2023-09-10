from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime
from typing import Optional

class NFTBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    hashCode: Optional[str] = Field(..., description="nft hash code", example="0x3aa6d66bfbf8e09d5d97012dba72374c7069e0d3f3ababc7a39d06ea9f51748b")
    name: Optional[str] = Field(None, max_length=20, example="NFT Artwork")
    description: Optional[str] = Field(None, example="This is a beautiful NFT artwork")
    imagePath: Optional[str] = Field(None, example="s3://bucket/path/to/image.jpg")
    createDate: Optional[datetime] = Field(None, example="2023-09-12T00:00:00Z")
    owner: Optional[str] = Field(None, max_length=10, example="owner123")
    bfOwner: Optional[str] = Field(None, max_length=10, example="ownerXYZ")

class NFTCreate(NFTBase):
    pass

class NFTResponse(NFTBase):
    NFTId: int  # Assuming NFTId is an integer, adjust the type as necessary
    imageId: int  # Including the imageId in the response as well