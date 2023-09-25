from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import model as image_model
from . import schema as image_schema
from domain.nft import model as nft_model
from domain.nft import schema as nft_schema
from sqlalchemy import or_

def create_image_and_nft(db: Session, image: image_schema.ImageCreate, nft: nft_schema.NFTBase):
    # Image 객체 생성
    new_image = image_model.Image(
        userId=image.userId,
        imageName=image.imageName,
        imageUrl=image.imageUrl,
        imageSize=image.imageSize,
        fileType=image.fileType,
        uploaderId=image.uploaderId,
        createTime=image.createTime,
        tag=image.tag,
        views=image.views
    )
    
    # NFT 객체 생성
    new_nft = nft_model.NFT(
        hashCode=nft.hashCode,
        name=nft.name,
        description=nft.description,
        imagePath=nft.imagePath,
        createDate=nft.createDate,
        owner=nft.owner,
        bfOwner=nft.bfOwner,
        image=new_image  # Image 객체를 NFT 객체에 연결
    )

    db.add(new_nft)  # NFT 객체 (및 관련 Image 객체)를 데이터베이스에 추가
    db.commit()
    db.refresh(new_nft)

    return new_image,new_nft

def get_Images_byName(db: Session, name: str, skip: int = 0, limit: int = 20):
    query = db.query(image_model.Image).filter(
        or_(
            image_model.Image.imageName == name,
            image_model.Image.imageName.like(f"{name}%"),
            image_model.Image.imageName.like(f"%{name}"),
            image_model.Image.imageName.like(f"%{name}%"),
        )
    )
    query = query.order_by(

        (image_model.Image.imageName == name),
        (image_model.Image.imageName.like(f"{name}%")).desc(),
        (image_model.Image.imageName.like(f"%{name}")).desc(),
        (image_model.Image.imageName.like(f"%{name}%")).desc(),
        image_model.Image.imageName
    )

    return query.offset(skip).limit(limit).all()
def update_rmData_status(db: Session, imageId: int, nftId: int, status: str) -> bool:
    image_db_user = db.query(image_model.Image).filter(image_model.Image.imageId == imageId).first()
    nft_db_user = db.query(nft_model.NFT).filter(nft_model.NFT.NFTId == nftId).first()

    if not image_db_user or not nft_db_user:
        return False

    try:
        if status == "remove":
            image_db_user.rmData = True
            nft_db_user.rmData = True
        elif status == "append":
            image_db_user.rmData = False
            nft_db_user.rmData = False
        else:
            raise ValueError(f"Invalid status value: {status}")

        db.commit()
    except IntegrityError:
        db.rollback()
        return False
    except ValueError as e:
        print(e)
        return False
    else:
        db.refresh(image_db_user)
        db.refresh(nft_db_user)
        return True