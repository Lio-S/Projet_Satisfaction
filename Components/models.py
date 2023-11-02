from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Genders(Base):
    __tablename__ = 'gender_tbl'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    gender = Column(String(6))

class Customer_types(Base):
    __tablename__ = 'customer_type_tbl'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_type = Column(String(20))

class Type_of_travel(Base):
    __tablename__ = 'type_of_travel_tbl'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type_of_travel = Column(String(14))

class Classes(Base):
    __tablename__ = 'classes_tbl'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    classes = Column(String(8))

class Satisfaction(Base):
    __tablename__ = 'satisfaction_tbl'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    satisfaction = Column(String(25))

class Traveler(Base):
    __tablename__ = 'traveler_tbl'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer)
    gender_id = Column(Integer, ForeignKey('gender_tbl.id'))
    customer_type_id = Column(Integer, ForeignKey('customer_type_tbl.id'))
    age = Column(Integer)
    type_of_travel_id = Column(Integer, ForeignKey('type_of_travel_tbl.id'))
    class_id = Column(Integer, ForeignKey('classes_tbl.id'))
    flight_distance = Column(Integer)
    inflight_wifi_service = Column(Integer)
    departure_arrival_time_convenient = Column(Integer)
    ease_of_online_booking = Column(Integer)
    gate_location = Column(Integer)
    food_and_drink = Column(Integer)
    online_boarding = Column(Integer)
    seat_comfort = Column(Integer)
    inflight_entertainment = Column(Integer)
    on_board_service = Column(Integer)
    leg_room_service = Column(Integer)
    baggage_handling = Column(Integer)
    checkin_service = Column(Integer)
    inflight_service = Column(Integer)
    cleanliness = Column(Integer)
    departure_delay_in_minutes = Column(Integer)
    arrival_delay_in_minutes = Column(Integer)
    satisfaction_id = Column(Integer, ForeignKey('satisfaction_tbl.id'))
    gender = relationship("Genders")
    customer_type = relationship("Customer_types")
    type_of_travel = relationship("Type_of_travel")
    classes = relationship("Classes")
    satisfaction = relationship("Satisfaction")
