from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

def get_bookings(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Booking).offset(skip).limit(limit).all()

def create_booking(db: Session, booking: schemas.Booking):
    # check duplication
    db_booked = db.query(models.Booking).filter(models.Booking.room_id == booking.room_id).filter(models.Booking.end_datetime > booking.start_datetime).filter(models.Booking.start_datetime < booking.end_datetime).all()

    if len(db_booked) == 0:
        db_booking = models.Booking(
            user_id=booking.user_id,
            room_id=booking.room_id,
            book_num=booking.book_num,
            start_datetime=booking.start_datetime,
            end_datetime=booking.end_datetime,
        )
        db.add(db_booking)
        db.commit()
        db.refresh(db_booking)
        return db_booking
    else:
        raise HTTPException(status_code=404, detail="reservation not available")

def update_booking(db: Session, booking_id: int, booking: schemas.Booking):
    db_booking = db.query(models.Booking).filter(models.Booking.booking_id == booking_id).first()
    if db_booking is None:
        return None

    db_booking['user_id'] = booking['user_id']
    db_booking['room_id'] = booking['room_id']
    db_booking['book_num'] = booking['book_num']
    db_booking['start_datetime'] = booking['start_datetime']
    db_booking['end_datetime'] = booking['end_datetime']

    db.update(db_booking)
    db.commit()
    return booking

def delete_booking(db: Session, booking_id: int):
    db.query(models.Booking).filter(models.Booking.booking_id == booking_id).delete()
    db.commit()
    return  {'message': 'booking_delete_success'}

# users
def get_users(db: Session, skip: int=0, limit: int=100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.User):
    db_user = models.User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: schemas.User):
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user is None:
        return None

    db_user = user['username']
    db.update(db_user)    
    db.commit()
    return db_user

def delete_user(db: Session, user_id: int):
    db.query(models.User).filter(models.User.user_id == user_id).delete()
    db.commit()
    return  {'message': 'user_delete_success'}

#room
def get_rooms(db: Session, skip: int=0, limit: int=100):
    return db.query(models.Room).offset(skip).limit(limit).all()

def create_room(db: Session, room: schemas.Room):
    db_room = models.Room(room_name=room.room_name, capacity=room.capacity)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def update_room(db: Session, room_id: int, room: schemas.Room):
    db_room = db.query(models.Room).filter(models.Room.room_id == room_id).first()
    if db_room is None:
        return None

    db_room['room_name'] = room['room_name']
    db_room['capacity'] = room['capacity']

    db.update(db_room)
    db.commit()
    return room

def delete_room(db: Session, room_id: int):
    db.query(models.Room).filter(models.Room.room_id == room_id).delete()
    db.commit()
    return  {'message': 'room_delete_success'}
