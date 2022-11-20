from .database import Base
from sqlalchemy import Column, String, DateTime
from pydantic import BaseModel
import datetime

class MemberOrm(Base):
    __tablename__ = "member"

    stock_code = Column(String, primary_key=True)
    kap_member_id = Column(String)
    mkk_member_id = Column(String)
    title = Column(String)
    updated_at = Column(DateTime)


class MemberModel(BaseModel):
    stock_code: str
    kap_member_id: str
    mkk_member_id: str
    title: str
    updated_at: datetime.datetime

    class Config:
        orm_mode = True

class InsertUpdateResult(BaseModel):
    updated: int
    inserted: int