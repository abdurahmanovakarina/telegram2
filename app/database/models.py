from sqlalchemy import create_engine, BigInteger, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column
from typing import Optional

engine = create_engine(url='sqlite:///db.sqlite3', echo=True)

Session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__= 'user'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(25))
    gender: Mapped[Optional[str]]


class Horoscope(Base):
    __tablename__ = 'horoscope'
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    zz: Mapped[str] = mapped_column(String(25))
    today: Mapped[str]
    tomorrow: Mapped[str]
    month: Mapped[str]
    year: Mapped[str]


async def start_db():
    Base.metadata.create_all(bind=engine)
