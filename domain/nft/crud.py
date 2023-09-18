from sqlalchemy.orm import Session
from sqlalchemy import or_
from . import model, schema

def get_nftToken_byId(db: Session, nftId: int):
    return db.query(model.NFT).filter(model.NFT.NFTId == nftId)

def get_nftTokens_byName(db: Session, name: str, skip: int = 0, limit: int = 20):
    '''
    result_list = []

    # Step 1: Get exact match
    exact_match_query = db.query(model.NFT).filter(model.NFT.name == name).all()
    result_list.extend(exact_match_query)

    # Step 2: Get prefix match (e.g., "fire*")
    prefix_match_query = db.query(model.NFT).filter(
        model.NFT.name.like(f"{name}%"),
        ~model.NFT.name.in_([record.name for record in exact_match_query])
    ).all()
    result_list.extend(prefix_match_query)

    # Step 3: Get suffix match (e.g., "*fire")
    suffix_match_query = db.query(model.NFT).filter(
        model.NFT.name.like(f"%{name}"),
        ~model.NFT.name.in_([record.name for record in result_list])
    ).all()
    result_list.extend(suffix_match_query)

    # Step 4: Get partial match (e.g., "*fire*")
    partial_match_query = db.query(model.NFT).filter(
        model.NFT.name.like(f"%{name}%"),
        ~model.NFT.name.in_([record.name for record in result_list])
    ).all()
    result_list.extend(partial_match_query)
    '''

    query = db.query(model.NFT).filter(
        or_(
            model.NFT.name == name,  # Exact match
            model.NFT.name.like(f"{name}%"),  # Prefix match
            model.NFT.name.like(f"%{name}"),  # Suffix match
            model.NFT.name.like(f"%{name}%"),  # Partial match
        )
    )
    
    # Adding custom ordering to respect the priority
    query = query.order_by(
        (model.NFT.name == name).desc(),
        (model.NFT.name.like(f"{name}%")).desc(),
        (model.NFT.name.like(f"%{name}")).desc(),
        (model.NFT.name.like(f"%{name}%")).desc(),
        model.NFT.name
    )

    return query.offset(skip).limit(limit).all()
