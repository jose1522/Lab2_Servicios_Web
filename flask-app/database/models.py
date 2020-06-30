from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Index, Integer, LargeBinary, Table, Unicode, text

from . import db

Base = db
Model = Base.Model
metadata = Base.metadata

class Branch(Model):
    __tablename__ = 'branch'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50), nullable=False)
    active = Column(Integer, index=True, server_default=text("((1))"))
