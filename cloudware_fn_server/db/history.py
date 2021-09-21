from db.base import BaseMixedIn, Base
from sqlalchemy import Column, BigInteger, String
from sqlalchemy.orm import sessionmaker


class CWHistoryRecord(Base, BaseMixedIn):
    __tablename__ = 'cw_history_record'
    seq_id = Column(BigInteger)
    content = Column(String)
    user_id = Column(String)
    device_id = Column(String)


if __name__ == '__main__':
    from db.base import engine

    SessionFactory = sessionmaker(bind=engine)
    session = SessionFactory()
    record = CWHistoryRecord()
    record.content = "asd"
    session.add(record)
    session.commit()
