from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StoreStatus(Base):
    __tablename__ = "store_status"
    
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, index=True)
    timestamp_utc = Column(DateTime)
    status = Column(String)

class BusinessHours(Base):
    __tablename__ = "business_hours"
    
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, index=True)
    day_of_week = Column(Integer)
    start_time_local = Column(String)
    end_time_local = Column(String)

class Timezone(Base):
    __tablename__ = "timezones"
    
    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer, index=True)
    timezone_str = Column(String)
