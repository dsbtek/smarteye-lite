from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import List, Union
from . import schemas, models, database
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from pydantic import ValidationError
from .schemas import ProductUpdate
from fastapi.responses import JSONResponse

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def convert_model_to_dict(model_instance):
    return {column.name: getattr(model_instance, column.name) for column in model_instance.__table__.columns}

# Create a new user
@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        # Hash the user's password before saving to the database
        hashed_password = pwd_context.hash(user.hashed_password)
        
        # Create a User model instance with the hashed password
        db_user = models.User(email=user.email, hashed_password=hashed_password, is_active=user.is_active, full_name=user.full_name, user_type=user.user_type)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return convert_model_to_dict(db_user)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="User with this email already exists")

# Get a user by ID
@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return convert_model_to_dict(db_user)

# Create or update tank logs with temperature
@router.post("/tank-logs-temp/")
async def create_or_update_temp_tank_logs(tank_datas: List[List[str]], db: Session = Depends(get_db)):
    for tank_data in tank_datas:
        local_id, date_time, multicont_polling_address, tank_index, temp_1, temp_2, temp_3, temp_4, temp_5, avg_temp, tank_id, vol, tcv, height, capacity, atg_time = tank_data

        existing_record = db.query(models.TankTemperature).filter(models.TankTemperature.tank_id == tank_id).first()

        update_data = {
            'date_time': date_time,
            'multicont_polling_address': multicont_polling_address,
            'tank_index': tank_index,
            'temp_1': temp_1,
            'temp_2': temp_2,
            'temp_3': temp_3,
            'temp_4': temp_4,
            'temp_5': temp_5,
            'avg_temp': avg_temp,
            'tank_id': tank_id,
            'vol': vol * 1000,
            'tcv': tcv,
            'local_id': local_id,
            'height': height,
            'capacity': capacity,
            'atg_time': atg_time
        }

        if existing_record:
            db.query(models.TankTemperature).filter(models.TankTemperature.tank_id == tank_id).update(update_data)
            db.commit()
        else:
            db_latest_tank_log_temp = models.TankTemperature(**update_data)
            db.add(db_latest_tank_log_temp)
            db.commit()

    return {"message": "Record(s) Inserted/Updated Successfully"}

# Get all tank logs with temperature
@router.get("/tank-logs-temp/")
def get_all_temp_tank_logs(db: Session = Depends(get_db)):
    temp_tank_logs = db.query(models.TankTemperature).all()
    res = []
    for tank in temp_tank_logs:
        try:
            get_tank = db.query(models.Tanks).filter(models.Tanks.id==tank.tank_id).first()
            if get_tank:
                tank.product = get_tank.product.Code
                tank.tank_name = get_tank.Name
                res.append(tank)
            else:
                continue
        except:
            continue
    return res

# Get tank log by ID
@router.get("/tank-logs/{tank_log_id}")
def read_tank_log(tank_log_id: int, db: Session = Depends(get_db)):
    db_tank_log = db.query(models.TankLogs).filter(models.TankLogs.id == tank_log_id).first()
    if db_tank_log is None:
        raise HTTPException(status_code=404, detail="Tank log not found")
    return db_tank_log

# Create or update latest tank log and create tank log
@router.post("/tank-logs/")
def create_or_update_tank_logs(
    request: Request,
    tank_log_data_list: List[schemas.TankLogsCreate],
    db: Session = Depends(get_db)
):
    for tank_log_data in tank_log_data_list:
        # Extract variables from tank_log_data
        tank_name = f"Tank {tank_log_data.tank_index}"
        volume = tank_log_data.pv
        height = tank_log_data.sv
        temperature = tank_log_data.temperature
        water = tank_log_data.water
        product = "AGO"
        fill = (tank_log_data.pv / 1) * 100
        tank_id = tank_log_data.tank_id

        # Check if tank_id already exists in LatestTankLog
        existing_latest_tank_log = db.query(models.LatestTankLog).filter(models.LatestTankLog.tank_id == tank_id).first()

        # Update or create LatestTankLog
        try:
            if existing_latest_tank_log:
                # Update existing LatestTankLog
                db.query(models.LatestTankLog).filter(models.LatestTankLog.tank_id == tank_id).update({
                    models.LatestTankLog.tank_name: tank_name,
                    models.LatestTankLog.volume: volume,
                    models.LatestTankLog.product: product,
                    models.LatestTankLog.fill: fill
                })
            else:
                # Create new LatestTankLog
                db_latest_tank_log = models.LatestTankLog(
                    tank_name=tank_name,
                    volume=volume,
                    height=height,
                    temperature=temperature,
                    water=water,
                    product=product,
                    fill=fill,
                    tank_id=tank_id
                )
                db.add(db_latest_tank_log)

            # Create new TankLogs entry for each tank log data
            db_tank_log = models.TankLogs(**tank_log_data.dict())
            db.add(db_tank_log)

            db.commit()
        except Exception as e:
            continue

    response = Response(content="Records Inserted/Updated successfully", status_code=200)
    return response

# Get latest tank log by ID
@router.get("/latest-tank-logs/{latest_tank_log_id}")
def read_latest_tank_log(latest_tank_log_id: int, db: Session = Depends(get_db)):
    db_latest_tank_log = db.query(models.LatestTankLog).filter(models.LatestTankLog.id == latest_tank_log_id).first()
    if db_latest_tank_log is None:
        raise HTTPException(status_code=404, detail="Latest tank log not found")
    return db_latest_tank_log

# Get a list of all created latest tank logs
@router.get("/latest-tank-logs/")
def get_all_latest_tank_logs(db: Session = Depends(get_db)):
    latest_tank_logs = db.query(models.LatestTankLog).all()
    return latest_tank_logs


# JWT Config
SECRET_KEY = "kutubujad"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

# Function to create access token
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependency to get the current user
def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="login"))):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
    return token_data

# Login endpoint
@router.post("/login")
async def login_for_access_token(form_data: schemas.UserLogin, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not user.verify_password(form_data.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer", "user":user}

@router.get("/protected")
async def protected_route(current_user: schemas.TokenData = Depends(get_current_user)):
    return {"message": "You are accessing a protected route!"}

@router.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductBase, db: Session = Depends(get_db)):
    try:
        db_product = models.Products(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return convert_model_to_dict(db_product)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="Product with this code already exists")

@router.get("/products/", response_model=List[schemas.Product])
def get_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        products = db.query(models.Products).offset(skip).limit(limit).all()
        return [
            {
                "id": product.id,
                "Name": product.Name,
                "Code": product.Code,
                "density": product.density,
                "Created_at": product.Created_at,
                "Updated_at": product.Updated_at,
                "Deleted_at": product.Deleted_at,
            }
            for product in products
        ]
    except Exception as e:
        # Handle exceptions here if needed
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.get("/users/", response_model=List[schemas.User])
def read_user(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
    
        users = db.query(models.User).offset(skip).limit(limit).all()
        return [
                {
                "id":user.id,
                "email": user.email,
                "is_active": user.is_active,
                "hashed_password": user.hashed_password,
                "full_name": user.full_name,
                "user_type": user.user_type
                }
                for user in users
            ]
    except Exception as e:
        # Handle exceptions here if needed
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/products/{product_id}", response_model=schemas.Product)
def update_product_endpoint(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    existing_product = db.query(models.Products).filter(models.Products.id == product_id).first()
    if existing_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    for field, value in product_update.dict(exclude_unset=True).items():
        setattr(existing_product, field, value)
    db.commit()
    db.refresh(existing_product)
    return convert_model_to_dict(existing_product)

@router.delete("/products/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = db.query(models.Products).filter(models.Products.id == product_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)
    db.commit()
    
    return convert_model_to_dict(db_product)

# Endpoint to create a new tank
@router.post("/tanks/")
def create_tank(tank: schemas.TankCreate, db: Session = Depends(get_db)):
    # Assuming tank.product_id is provided in the request payload
    product_id = tank.product

    # Retrieve the Products instance based on the provided product_id
    db_product = db.query(models.Products).get(product_id)

    # Check if the product exists
    if not db_product:
        raise HTTPException(status_code=400, detail=f"Product with id {product_id} not found")

    # Create a new Tanks instance without passing product as a keyword argument
    db_tank = models.Tanks(
        Name=tank.Name,
        # Control_mode=tank.Control_mode,
        # Tank_controller=tank.Tank_controller,
        Controller_polling_address=tank.Controller_polling_address,
        Tank_index=tank.Tank_index,
        Capacity=tank.Capacity,
        # UOM=tank.UOM,
        # Shape=tank.Shape,
        # LL_Level=tank.LL_Level,
        # L_Level=tank.L_Level,
        # HH_Level=tank.HH_Level,
        # H_Level=tank.H_Level,
        # Reorder=tank.Reorder,
        # Leak=tank.Leak,
        Created_at=tank.Created_at,
        Status=tank.Status,
        # Offset=tank.Offset,
        # Po4=tank.Po4,
        # Display_unit=tank.Display_unit,
        # Density=tank.Density,
        Tank_height=tank.Tank_height,
        # Anomaly_period=tank.Anomaly_period,
        # Anomaly_volume=tank.Anomaly_volume,
        # Tank_Note=tank.Tank_Note,
        product=db_product  # Assign the product directly here, not as a keyword argument
    )

    # Add, commit, and refresh as you were doing before
    db.add(db_tank)
    db.commit()
    db.refresh(db_tank)
    
    # Return the converted tank dictionary
    return convert_model_to_dict(db_tank)



# Endpoint to update a tank by ID
@router.put("/tanks/{tank_id}")
def update_tank(tank_id: int, tank_update: schemas.TankUpdate, db: Session = Depends(get_db)):
    db_tank = db.query(models.Tanks).filter(models.Tanks.id == tank_id).first()

    if db_tank is None:
        raise HTTPException(status_code=404, detail="Tank not found")

    # Retrieve the Products instance based on the provided product_id
    db_product = db.query(models.Products).get(tank_update.Product)

    # Check if the product exists
    if not db_product:
        raise HTTPException(status_code=400, detail=f"Product with id {tank_update.Product} not found")

    # Update the tank's product association
    db_tank.product = db_product

    # Update other fields using Pydantic model
    for field, value in tank_update.dict(exclude_unset=True).items():
        setattr(db_tank, field, value)

    db.commit()
    db.refresh(db_tank)

    return convert_model_to_dict(db_tank)



# Endpoint to get a list of all tanks
@router.get("/tanks/")
def get_tanks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tanks = db.query(models.Tanks).offset(skip).limit(limit).all()
    return  [
                {
                    "Tank_id": tank.id,
                    "Name": tank.Name,
                    "Product_id": tank.product,
                    "Control_mode": tank.Control_mode,
                    "Tank_controller": tank.Tank_controller,
                    "Controller_polling_address": tank.Controller_polling_address,
                    "Tank_index": tank.Tank_index,
                    "Capacity": tank.Capacity,
                    "UOM": tank.UOM,
                    "Shape": tank.Shape,
                    "LL_Level": tank.LL_Level,
                    "L_Level": tank.L_Level,
                    "HH_Level": tank.HH_Level,
                    "H_Level": tank.H_Level,
                    "Reorder": tank.Reorder,
                    "Leak": tank.Leak,
                    "Created_at": tank.Created_at,
                    "Updated_at": tank.Updated_at,
                    "Deleted_at": tank.Deleted_at,
                    "Status": tank.Status,
                    "Offset": tank.Offset,
                    "Po4": tank.Po4,
                    "Display_unit":tank.Display_unit,
                    "Density":tank.Density,
                    "Tank_height": tank.Tank_height,
                    "Anomaly_period": tank.Anomaly_period,
                    "Anomaly_volume": tank.Anomaly_volume,
                    "Tank_Note": tank.Tank_Note
                    }
                for tank in tanks
            ]
    
# Endpoint to delete a tank by ID
@router.delete("/tanks/{tank_id}")
def delete_tank(tank_id: int, db: Session = Depends(get_db)):
    db_tank = db.query(models.Tanks).filter(models.Tanks.id == tank_id).first()
    if db_tank is None:
        raise HTTPException(status_code=404, detail="Tank not found")
    db.delete(db_tank)
    db.commit()
    return convert_model_to_dict(db_tank)

@router.get("/tanks_config/", response_model=List[schemas.TankBase])
def get_tanks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        tanks = db.query(models.Tanks).all()
        # Format the response
        tank_details = []
        for tank in tanks:
            tank_detail = {
                "Name": tank.Name,
                "Control_mode": tank.Control_mode,
                "Tank_controller": tank.Tank_controller,
                "Controller_polling_address": tank.Controller_polling_address,
                "Tank_index": tank.Tank_index,
                "Tank_capacity": tank.Capacity,
                "Tank_id": tank.id
            }
            tank_details.append(tank_detail)

        response = {
                "data": {
                    "tank_details": tank_details
                },
                "errors": "",
                "code": 200,
                "status": "success"
            }

        return JSONResponse(content=response)

    except Exception as e:
        # Handle exceptions as needed
        error_response = {
            "data": {},
            "errors": str(e),
            "code": 500,
            "status": "error"
        }
        return JSONResponse(content=error_response)
    
@router.post("/logout")
async def logout(current_user: schemas.TokenData = Depends(get_current_user)):
    print(current_user)
    return {"message": "Logout successful"}