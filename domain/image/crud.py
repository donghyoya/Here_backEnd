from sqlalchemy.orm import Session
from . import model as image_model
from . import schema as image_schema
from domain.nft import model as nft_model
from domain.nft import schema as nft_schema

def create_image_and_nft(db: Session, image: image_schema.ImageBase, nft: nft_schema.NFTBase):
    # Image 객체 생성
    new_image = image_model.Image(
        imageName=image.imageName,
        imageUrl=image.imageUrl,
        imageSize=image.imageSize,
        fileType=image.fileType,
        uploaderId=image.uploaderId,
        createTime=image.createTime,
        tag=image.tag,
        views=image.views
        # 여기에 다른 필드를 추가하세요...
    )
    
    # NFT 객체 생성
    new_nft = nft_model.NFT(
        name=nft.name,
        description=nft.description,
        imagePath=nft.imagePath,
        createDate=nft.createDate,
        owner=nft.owner,
        bfOwner=nft.bfOwner,
        # 여기에 다른 필드를 추가하세요...
        image=new_image  # Image 객체를 NFT 객체에 연결
    )

    db.add(new_nft)  # NFT 객체 (및 관련 Image 객체)를 데이터베이스에 추가
    db.commit()
    db.refresh(new_nft)

    return new_image,new_nft
