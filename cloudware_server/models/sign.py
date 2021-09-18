from sqlalchemy import Column, Integer, String, Text, Date, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy import create_engine
from cloudware_server.common.db.base import Base, BaseMixedIn


class PFSignReord(Base, BaseMixedIn):
    __tablename__ = 'pf_sign_record'