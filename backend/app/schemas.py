from pydantic import BaseModel, Field, PositiveInt, conint
from typing import List, Optional, Union
from datetime import datetime

class UserBase(BaseModel):
    email: str
    is_active: bool
    full_name: str
    user_type: str

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int

class UserCredentials(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None
    
class UserLogin(BaseModel):
    username: str
    password: str

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
    product: str
    atg_time: str
    

class TankTemperatureCreate(TankTemperatureBase):
    tank_data: List
    class Config:
        orm_mode = True

class TankTemperatureInput(TankTemperatureBase):
    tank_data: List
    class Config:
        orm_mode = True

class TankTemperature(TankTemperatureCreate):
    id: int
class ProductBase(BaseModel):
    Name: str
    Code: str
    density: str
    Created_at: datetime
    class Config:
        orm_mode = True

class Product(ProductBase):
    id: Optional[int]
    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    Name: Optional[str]
    Code: Optional[str]
    density: Optional[str]
    Updated_at: datetime
    class Config:
        orm_mode = True

class TankBase(BaseModel):
    Name: str
    product: PositiveInt
    # Control_mode: str
    # Tank_controller: str
    Controller_polling_address: conint(ge=1, le=10)
    Tank_index: conint(ge=1, le=999999)
    Capacity: PositiveInt
    # UOM: str
    # Shape: str
    # LL_Level: int
    # L_Level: int
    # HH_Level: int
    # H_Level: int
    # Reorder: int
    # Leak: int
    Created_at: datetime
    Status: bool
    # Offset: float
    # Po4: float
    # Display_unit: str
    # Density: Optional[float]
    Tank_height: Optional[float]
    # Anomaly_period: Optional[float]
    # Anomaly_volume: Optional[float]
    # Tank_Note: str
    
class TankCreate(TankBase):
    product: int
    class Config:
        orm_mode = True

class TankUpdate(BaseModel):
    Name: Optional[str]
    Product: Optional[PositiveInt]  # Optional field for updating the product
    # Control_mode: Optional[str]
    # Tank_controller: Optional[str]
    Controller_polling_address: Optional[conint(ge=1, le=10)]
    Tank_index: Optional[conint(ge=1, le=999999)]
    Capacity: Optional[PositiveInt]
    # UOM: Optional[str]
    # Shape: Optional[str]
    # LL_Level: Optional[int]
    # L_Level: Optional[int]
    # HH_Level: Optional[int]
    # H_Level: Optional[int]
    # Reorder: Optional[int]
    # Leak: Optional[int]
    Updated_at: Optional[datetime]
    Status: Optional[bool]
    # Offset: Optional[float]
    # Po4: Optional[float]
    # Display_unit: Optional[str]
    # Density: Optional[float]
    Tank_height: Optional[float]
    # Anomaly_period: Optional[float]
    # Anomaly_volume: Optional[float]
    # Tank_Note: Optional[str]
    class Config:
        orm_mode = True

class Tank(TankBase):
    id: int
    class Config:
        orm_mode = True
