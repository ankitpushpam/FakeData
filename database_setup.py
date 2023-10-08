# database_setup.py
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import uuid
from faker import Faker

def setup_database_and_generate_data():
    engine = create_engine('sqlite:///fake_data.db')
    session = scoped_session(sessionmaker(bind=engine))
    Base = declarative_base()

    fake = Faker()

    class User(Base):
        __tablename__ = "user_table"
        user_uuid = Column(String, primary_key=True)
        firstName = Column(String(50))
        lastName = Column(String(50))
        age = Column(Integer)
        order_uuid = Column(String(50))
        address = Column(String(100))

        orders = relationship('Order', back_populates='user')

    class Order(Base):
        __tablename__ = "order_table"
        order_uuid = Column(String, primary_key=True)
        user_uuid = Column(String(50), ForeignKey('user_table.user_uuid'))
        order_time = Column(String(50))
        shipping_address = Column(String(200))
        billing_address = Column(String(100))
        product_id = Column(String(50))

        user = relationship('User', back_populates='orders')

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    num_of_records = 10  # Change this to the desired number of records

    for _ in range(num_of_records):
        # Create fake data and add to the session
        user = User(
            user_uuid=str(uuid.uuid4()),
            firstName=fake.first_name(),
            lastName=fake.last_name(),
            age=fake.random_int(min=18, max=65),
            order_uuid=str(uuid.uuid4()),
            address=fake.address(),
        )
        order = Order(
            order_uuid=str(uuid.uuid4()),
            user_uuid=user.user_uuid,
            order_time=fake.date_time_this_decade(),
            shipping_address=fake.address(),
            billing_address=fake.address(),
            product_id=str(uuid.uuid4()),  # Modified this line to generate a UUID string
        )
        session.add(user)
        session.add(order)

    session.commit()
    session.close()

if __name__ == "__main__":
    setup_database_and_generate_data()
