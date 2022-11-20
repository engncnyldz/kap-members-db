from ..database import SessionLocal
from ..models import MemberOrm, MemberModel, InsertUpdateResult
import httpx
import json
from datetime import datetime
from typing import List
from ..config import logger

def query_members():
    members = []

    try:

        members_url = "https://www.kap.org.tr/tr/api/kapmembers/IGS/A"

        with httpx.Client() as client:
            r = client.get(url= members_url, follow_redirects=True)

        members_returned = json.loads(r.text)
    
    
        for member in members_returned:

            memberOrm = MemberOrm(
                stock_code = member["stockCode"],
                kap_member_id = member["kapMemberOid"],
                mkk_member_id = member["mkkMemberOid"],
                title = member["kapMemberTitle"],
                updated_at = datetime.now()
            )
        
            members.append(memberOrm)
    except:
        logger.error("Error occured while fetching KAP members")
    return members


def insert_or_update_members(members=List[MemberOrm]):
    session = SessionLocal()
    result = InsertUpdateResult(
        inserted=0,
        updated=0
    )

    for member in members:
        member_query = session.query(MemberOrm).filter(MemberOrm.stock_code == member.stock_code)
        member_record = member_query.first()

        if(member_record):
            member_model = MemberModel.from_orm(member)
            member_query.update(member_model.dict(), synchronize_session=False)
            result.updated= result.updated +1

        else:
            session.add(member)
            result.inserted= result.inserted +1
        
    session.commit()    
    session.close() 

    logger.info(f"total inserted: {result.inserted}, total updated: {result.updated}")
    return result