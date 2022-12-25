from fastapi import Depends, APIRouter, status, HTTPException
from .. import models
from ..database import get_db
from sqlalchemy.orm import Session
from ..utils.sync_members import query_members, insert_or_update_members
from typing import List

router = APIRouter(
    prefix="/member"
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[models.MemberModel])
def get_all_members(db: Session = Depends(get_db)):

    members = db.query(models.MemberOrm).all()
    return members

@router.get("/{code}", status_code=status.HTTP_200_OK, response_model=models.MemberModel)
def get_member(code: str, db: Session = Depends(get_db)):

    member = db.query(models.MemberOrm).filter(models.MemberOrm.stock_code.contains(code.upper())).first()
    if member:
        return member
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{code} not found.")

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=models.InsertUpdateResult)
def sync_members():
    members = query_members()
    result = insert_or_update_members(members)
    
    return result