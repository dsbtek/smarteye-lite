from fastapi import APIRouter, Depends, HTTPException, Request, Response
from typing import List
from sqlalchemy.orm import Session
from . import schemas, models, database
# from fastapi.routing import APIRoute
router = APIRouter()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new user

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get a user by ID
@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#Create tank logs with tempfrom fastapi import HTTPException

@router.post("/tank-logs-temp/")
async def create_or_update_temp_tank_logs(request: Request, db: Session = Depends(get_db)):
    try:
        tank_data = await request.json()
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid JSON data in the request body")
    if not isinstance(tank_data, list):
        raise HTTPException(status_code=400, detail="Input should be a list")
    # tank_data = tank_log_temp.tank_data
    if len(tank_data) != 13:
        raise HTTPException(status_code=400, detail="Invalid payload format. Expected a list of 13 items.")
    
    local_id, date_time, multicont_polling_address, tank_index, temp_1, temp_2, temp_3, temp_4, temp_5, avg_temp, vol, tcv, tank_id = tank_data
    existing_latest_tank_log = db.query(models.TankTemperature).filter(models.TankTemperature.tank_id == tank_id).first()
    try:
        if existing_latest_tank_log:
            # Update the existing LatestTankLogTemp
            update_data = {
                models.TankTemperature.date_time: date_time,
                models.TankTemperature.multicont_polling_address: multicont_polling_address,
                models.TankTemperature.tank_index: tank_index,
                models.TankTemperature.temp_1: temp_1,
                models.TankTemperature.temp_2: temp_2,
                models.TankTemperature.temp_3: temp_3,
                models.TankTemperature.temp_4: temp_4,
                models.TankTemperature.temp_5: temp_5,
                models.TankTemperature.avg_temp: avg_temp,
                models.TankTemperature.tcv: tcv,
                models.TankTemperature.local_id: local_id,
                models.TankTemperature.vol: vol
            }
            db.query(models.TankTemperature).filter(models.TankTemperature.tank_id == tank_id).update(update_data)
        else:
            # Create a new LatestTankLogTemp
            db_latest_tank_log_temp = models.TankTemperature(
                local_id=local_id,
                date_time=date_time,
                multicont_polling_address=multicont_polling_address,
                tank_index=tank_index,
                temp_1=temp_1,
                temp_2=temp_2,
                temp_3=temp_3,
                temp_4=temp_4,
                temp_5=temp_5,
                avg_temp=avg_temp,
                tcv=tcv,
                tank_id=tank_id,
                vol=vol,
            )
            db.add(db_latest_tank_log_temp)
        
        db.commit()
        # db.refresh()
        return "Record Inserted/Updated Successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/tank-logs-temp/")
def get_all_temp_tank_logs(db: Session = Depends(get_db)):
    temp_tank_logs = db.query(models.TankTemperature).all()
    return temp_tank_logs

# Get tank logs by ID
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
        # Define variables based on each request body content
        tank_name = "Tank" + " " + str(tank_log_data.tank_index)
        volume = tank_log_data.pv
        height = tank_log_data.sv
        temperature = tank_log_data.temperature
        water = tank_log_data.water
        product = "AGO"
        fill = (tank_log_data.pv / 1) * 100
        tank_id = tank_log_data.tank_id

        # Check if the tank_id already exists in LatestTankLog
        existing_latest_tank_log = db.query(models.LatestTankLog).filter(models.LatestTankLog.tank_id == tank_id).first()

        if existing_latest_tank_log:
            # Update the existing LatestTankLog with the variables defined above
            try:
                db.query(models.LatestTankLog).filter(models.LatestTankLog.tank_id == tank_id).update({
                    models.LatestTankLog.tank_name: tank_name,
                    models.LatestTankLog.volume: volume,
                    models.LatestTankLog.product: product,
                    models.LatestTankLog.fill: fill
                })
            except:
                continue
        else:
            # Create a new LatestTankLog with the variables defined above
            try:
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
            except:
                continue

        # Create a new TankLogs entry for each tank log data
        db_tank_log = models.TankLogs(**tank_log_data.dict())
        db.add(db_tank_log)

    db.commit()
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