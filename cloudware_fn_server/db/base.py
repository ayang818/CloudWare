from sqlalchemy import Column, Integer, TIMESTAMP, text, func
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class BaseMixedIn(object):
    id = Column(Integer, primary_key=True, comment='id')
    create_time = Column(TIMESTAMP, server_default=func.now(), comment='创建时间')
    update_time = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                         comment='更新时间')


def create_all():
    engine = create_engine(
        "mysql+pymysql://root:123@localhost:3306/pf_base?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )
    Base.metadata.create_all(engine)


# TODO 改密码
engine = create_engine(
    "mysql+pymysql://root:cloudware1004210191@110.42.140.209:3306/cloudware_base?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

SessionFactory = sessionmaker(bind=engine)
session = SessionFactory()


def get_session():
    global session
    return session

# from sqlalchemy import Column, BigInteger, String

# class CWHistoryRecord(Base, BaseMixedIn):
#     __tablename__ = 'cw_history_record'
#     seq_id = Column(BigInteger)
#     content = Column(String)
#     user_id = Column(String)
#     device_id = Column(String)
#
#
# if __name__ == '__main__':
#     session = get_session()
#     res = session.query(CWHistoryRecord).filter(CWHistoryRecord.user_id=="yugiofuaysdgfoaijdbhf", CWHistoryRecord.seq_id>=2376451892736).all()
#     print(res[0].__dict__)

# record = CWHistoryRecord()
# record.seq_id = 2376451892736
# record.content = "hdf798y711fdsa24d213r"
# record.user_id = "yugiofuaysdgfoaijdbhf"
# record.device_id = "asdgkuyguiy"
# session.add(record)
# session.commit()
