from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    email: str
    is_active: bool

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class LatestTankLogBase(BaseModel):
    tank_name: str
    volume: int
    height: str
    temperature: str
    water: str
    updated_at: datetime
    capacity: str
    product: str
    fill: str
    tank_status: int
    tank_id: str

class LatestTankLogCreate(LatestTankLogBase):
    pass

class LatestTankLog(LatestTankLogBase):
    id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True  # Ignore schema generation error


class TankLogsBase(BaseModel):
    transaction_id: str
    local_id: str
    multicont_polling_address: int
    mac_address: str
    pv: int
    pv_flag: int
    tank_index: int
    sv: int
    read_at: Optional[datetime]
    db_fill_time: datetime
    controller_type: int
    temperature: int
    water: int
    tc_volume: int
    probe_address: int
    status: int
    flag_log: int
    tank_id: int

class TankLogsCreate(TankLogsBase):
    pass

class TankLogs(TankLogsBase):
    id: int
    latest_tank_log: LatestTankLogBase

    class Config:
        from_attributes = True

class TankTemperatureBase(BaseModel):
    local_id: str
    date_time: str
    multicont_polling_address: int
    tank_index: int
    temp_1: float
    temp_2: float
    temp_3: float
    temp_4: float
    temp_5: float
    tcv: float
    avg_temp: float
    vol: float
    tank_id: int
    height: float
    capacity: float

class TankTemperatureCreate(TankTemperatureBase):
    tank_data: List

class TankTemperatureInput(TankTemperatureBase):
    tank_data: List

class TankTemperature(TankTemperatureCreate):
    id: int

    class Config:
        from_attributes = True