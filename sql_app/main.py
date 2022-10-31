from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

# db作成
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def index():
    return {"message": "Success"}

# booking
@app.get("/bookings", response_model=List[schemas.Booking])
async def read_bookings(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    return crud.get_bookings(db, skip=skip, limit=limit)

@app.post("/bookings", response_model=schemas.Booking)
async def create_booking(booking: schemas.BookingCreate, db: Session=Depends(get_db)):
    return crud.create_booking(db=db, booking=booking)

@app.put("/bookings/{booking_id}", response_model=schemas.Booking)
async def update_booking(booking_id: int, booking: schemas.BookingUpdate, db: Session=Depends(get_db)):
    return crud.update_booking(db=db, booking_id=booking_id, booking=booking)

@app.delete("/bookings/{booking_id}", response_model=schemas.Booking)
async def update_booking(booking_id: int, db: Session=Depends(get_db)):
    return crud.update_booking(db=db, booking_id=booking_id)

#user
@app.get("/users", response_model=List[schemas.User])
async def read_users(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    return crud.get_users(db, skip=skip, limit=limit)

@app.post("/users", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session=Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.put("/users/{user_id}", response_model=schemas.User)
async def update_user(user_id: int, user: schemas.UserUpdate, db: Session=Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, user=user)

@app.delete("/users/{user_id}", response_model=schemas.User)
async def update_user(user_id: int, db: Session=Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id)

#room
@app.get("/rooms", response_model=List[schemas.Room])
async def read_rooms(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    return crud.get_rooms(db, skip=skip, limit=limit)

@app.post("/rooms", response_model=schemas.Room)
async def create_room(room: schemas.RoomCreate, db: Session=Depends(get_db)):
    return crud.create_room(db=db, room=room)

@app.put("/rooms/{room_id}", response_model=schemas.Room)
async def update_room(room_id: int, room: schemas.RoomUpdate, db: Session=Depends(get_db)):
    return crud.update_room(db=db, room_id=room_id, room=room)

@app.delete("/rooms/{room_id}", response_model=schemas.Room)
async def update_room(room_id: int, db: Session=Depends(get_db)):
    return crud.update_room(db=db, room_id=room_id)