from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    full_name = Column(String)
    user_type = Column(String)

    def verify_password(self, password: str):
        return pwd_context.verify(password, self.hashed_password)

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
    fill = Column(Integer)
    tank_status = Column(Integer)
    tank_id = Column(String, unique=True, index=True)

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=False)
    Code = Column(String(10), nullable=False)
    density = Column(String(10), nullable=False)
    Created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    Updated_at = Column(DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    Deleted_at = Column(DateTime, nullable=True)
    tank = relationship("Tanks", back_populates="product")

    def __repr__(self):
        return self.Name

class Tanks(Base):
    __tablename__ = 'tanks'

    shape_list = [
        ('LC', 'Lying Cylindrical'),
        ('SC', 'Standing Cylindrical'),
        ('LR', 'Lying Rectangular'),
        ('SR', 'Standing Rectangular'),
        ('SRV', 'Standard Round View')
    ]

    controllers = [
        ('MTC', 'Multicont'),
        ('TLS', 'Veeder'),
        ('SEN', 'Sensor'),
        ('HYD', 'Hydrostatic'),
    ]

    id = Column(Integer, primary_key=True)
    Name = Column(String(50), nullable=True)
    Control_mode = Column(String(50), default='C')
    Tank_controller = Column(String(50), default='MTC')
    Controller_polling_address = Column(Integer, nullable=False, server_default='1')
    Tank_index = Column(Integer, nullable=False, server_default='1')
    Capacity = Column(Integer, nullable=False)
    UOM = Column(String(50), default='L')
    Shape = Column(String(50), default='LC')
    LL_Level = Column(Integer, nullable=True, server_default='0')
    L_Level = Column(Integer, nullable=True, server_default='0')
    HH_Level = Column(Integer, nullable=True, server_default='0')
    H_Level = Column(Integer, nullable=True, server_default='0')
    Reorder = Column(Integer, nullable=True, server_default='0')
    Leak = Column(Integer, nullable=True, server_default='0')
    Created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())
    Updated_at = Column(DateTime, nullable=False, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
    Deleted_at = Column(DateTime, nullable=True)
    Status = Column(Boolean, default=True)
    Offset = Column(Float, nullable=True, server_default='0.0')
    Po4 = Column(Float, nullable=True, server_default='0.0')
    Display_unit = Column(String(50), nullable=True, default='L')
    Density = Column(Float, nullable=True)
    Tank_height = Column(Float, nullable=True)
    Anomaly_period = Column(Float, nullable=True)
    Anomaly_volume = Column(Float, nullable=True)
    Tank_Note = Column(String(25), nullable=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship("Products", back_populates="tank")
    

    def __repr__(self):
        return f'Tank:{self.Name}'

class TankTemperature(Base):
    __tablename__ = "tank_temperature"

    id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    local_id = Column(String, unique=True)
    date_time = Column(String)
    multicont_polling_address = Column(Integer)
    tank_index = Column(Integer)
    tank_id = Column(Integer)
    temp_1 = Column(Float)
    temp_2 = Column(Float)
    temp_3 = Column(Float)
    temp_4 = Column(Float)
    temp_5 = Column(Float)
    avg_temp = Column(Float)
    tank_name = Column(String, nullable=True)
    vol = Column(Float)
    tcv = Column(Float)
    height = Column(Float)
    capacity = Column(Float)
    atg_time = Column(String, nullable=True)
    product = Column(String, nullable=True)
    
    
