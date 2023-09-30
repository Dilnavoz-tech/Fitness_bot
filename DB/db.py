from sqlalchemy import create_engine, Column, Integer, BIGINT, Boolean, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.sql.functions import current_date

engine = create_engine("postgresql+psycopg2://postgres:1@pg/postgres")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BIGINT, nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(30))
    username = Column(String(50))
    join_at = Column(String(50))


Base.metadata.create_all(engine)
