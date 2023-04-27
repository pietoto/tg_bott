import datetime

import sqlalchemy

from .db_session import SqlAlchemyBase


class Product(SqlAlchemyBase):
    __tablename__ = 'products'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(100),
                             nullable=False)
    about = sqlalchemy.Column(sqlalchemy.String(100),
                              nullable=False)
    price = sqlalchemy.Column(sqlalchemy.Integer,
                              nullable=False)

    def __repr__(self):
        return f'Запись: {self.name}'
