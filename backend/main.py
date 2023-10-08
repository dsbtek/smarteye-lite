# from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
# from typing import List
from fastapi import FastAPI
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

# from app import crud, models, schemas
from app.database import create_tables
from app import crud, models
app = FastAPI()
# Allow requests from your Vue.js application's domain
origins = ["*"]  # Update with your Vue.js app's domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
create_tables()
app.include_router(crud.router)
app.mount("/", StaticFiles(directory="static",html=True), name="static")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)