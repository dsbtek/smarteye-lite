from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class TankLogs(Base):
    __tablename__ = "tank_logs"

    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    transaction_id = Column(String, unique=True)
    local_id = Column(String, unique=True)
    multicont_polling_address = Column(Integer, index=True)
    mac_address = Column(String)
    pv = Column(String)
    pv_flag = Column(String)
    tank_index = Column(Integer)
    sv = Column(Integer)
    read_at = Column(String, default=None)
    db_fill_time = Column(DateTime, default=func.now())
    controller_type = Column(String)
    temperature = Column(String)
    water = Column(String)
    tc_volume = Column(String)
    probe_address = Column(String)
    status = Column(Integer)
    flag_log = Column(Boolean)
    tank_id = Column(String)

class LatestTankLog(Base):
    __tablename__ = "latest_tank_log"
    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    tank_name = Column(String)
    volume = Column(Integer)
    height = Column(Integer)
    temperature = Column(Integer)
    water = Column(Integer)
    updated_at = Column(DateTime, default=func.now())
    capacity = Column(Integer)
    product = Column(String)
    fill = Column(Integer) # (pv / capacity )* 100
    tank_status = Column(Integer)
    tank_id = Column(String, unique=True, index=True)


class TankTemperature(Base):
    __tablename__ = "tank_temperature"
    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    local_id = Column(String, unique=True)
    date_time = Column(String)
    multicont_polling_address = Column(Integer)
    tank_index = Column(Integer)
    temp_1 = Column(Float)
    temp_2 = Column(Float)
    temp_3 = Column(Float)
    temp_4 = Column(Float)
    temp_5 = Column(Float)
    avg_temp = Column(Float)
    tank_id = Column(Integer)
    vol = Column(Float)
    tcv = Column(Float)
    height = Column(Float)
    capacity = Column(Float)
    product = Column(String)
    
