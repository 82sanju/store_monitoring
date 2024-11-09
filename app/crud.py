from sqlalchemy.orm import Session
from . import models

def get_store_status(db: Session, store_id: int):
    return db.query(models.StoreStatus).filter(models.StoreStatus.store_id == store_id).all()

def get_business_hours(db: Session, store_id: int):
    return db.query(models.BusinessHours).filter(models.BusinessHours.store_id == store_id).all()

def get_timezone(db: Session, store_id: int):
    return db.query(models.Timezone).filter(models.Timezone.store_id == store_id).first()
