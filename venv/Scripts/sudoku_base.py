
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, select
from sqlalchemy import create_engine
from sqlalchemy.orm import validates
from sqlalchemy.orm import sessionmaker
import re

Base = declarative_base()

class Sudoku(Base):
    __tablename__ = 'Sudoku'

    id = Column(Integer, primary_key = True)
    board = Column(String(81), nullable = False)
    creator = Column(String)

    # @validates('board')
    # def validate_board(self, key, value):
    #     # pattern = '^[\d]{3}+$'
    #
    #     # assert value != '^[\d]{3}+$'
    #     # return value
    #
    #     if re.match( '^[\d]{3}+$', value):
    #         print("\n111111111111111111111111111111111111111111")
    #         return value
    #     return None


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sesja = Session()

s = Sudoku(board = "123", creator = "user")
s2 = Sudoku(board = "12345", creator = "user")
sesja.add_all([s, s2])
sesja.commit()

for i in sesja.query(Sudoku).all():
    print(i.board + i.creator)

sesja.rollback()
sesja.close()