import datetime
from pydantic import BaseModel, Field

class BookingCreate(BaseModel):
    user_id: int
    room_id: int
    book_num: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime

class BookingUpdate(BaseModel):
    user_id: int = Field(nullable=True)
    room_id: int = Field(nullable=True)
    book_num: int = Field(nullable=True)
    start_datetime: datetime.datetime = Field(nullable=True)
    end_datetime: datetime.datetime = Field(nullable=True)

class Booking(BookingCreate):
    booking_id: int

    class Config:
        orm_mode=True

class UserCreate(BaseModel):
    username: str = Field(max_length=12)

class UserUpdate(BaseModel):
    username: str = Field(max_length=12, nullable=True)

class User(UserCreate):
    user_id: int

    class Config:
        orm_mode=True

class RoomCreate(BaseModel):
    room_name: str = Field(max_length=12)
    capacity: int

class RoomUpdate(BaseModel):
    room_name: str = Field(max_length=12, nullable=True)
    capacity: int = Field(nullable=True)

class Room(RoomCreate):
    room_id: int

    class Config:
        orm_mode=True
