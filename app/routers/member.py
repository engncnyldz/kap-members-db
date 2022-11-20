from fastapi import Depends, APIRouter
from .. import models
from ..database import get_db
from sqlalchemy.orm import Session
from ..utils.sync_members import query_members, insert_or_update_members
from typing import List

router = APIRouter(
    prefix="/member"
)

@router.get("/", response_model=List[models.MemberModel])
def get_all_members(db: Session = Depends(get_db)):

    members = db.query(models.MemberOrm).all()
    return members

@router.post("/", response_model=models.InsertUpdateResult)
def sync_members():
    members = query_members()
    result = insert_or_update_members(members)
    
    return result