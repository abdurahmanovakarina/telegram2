from app.database.models import Session
from app.database.models import User, Horoscope
from sqlalchemy import select


def get_user(tg_id):
    with Session.begin() as session:
        user = session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            return False
        return user
    
    
def set_user(tg, name, gender):
    with Session.begin() as session:
        user = session.scalar(select(User).where(User.tg_id == tg))
        if not user:
            session.add(User(tg_id=tg, name=name, gender=gender))
            session.commit()
            return
        return


def set_horoscope(zz: str, today: str, tomorrow: str, month: str, year: str):
    with Session.begin() as session:
        session.add(Horoscope(zz=zz, today=today, tomorrow=tomorrow, month=month, year=year))
        session.commit()


def get_horoscope(zodiac):
    with Session.begin() as session:
        print(zodiac)
        result = session.execute(select(Horoscope.zz, Horoscope.today, Horoscope.tomorrow, Horoscope.month, Horoscope.year).where(Horoscope.zz == zodiac)).first()
        return result
