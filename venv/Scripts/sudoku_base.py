
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

s = Sudoku(board = "123456789888", creator = "user")
s2 = Sudoku(board = "12345", creator = "user")
sesja.add_all([s, s2])
sesja.commit()

for i in sesja.query(Sudoku).all():
   print(i.board + i.creator)

# for i in sesja.query(Sudoku).filter(Sudoku.id == 1):
#     print(i.board + i.creator)

#sesja.rollback()
sesja.close()

def add_sudoku(s, creator): # add sudoku to table, convert array to string
    sudoku_string = ""


def return_sudoku(index): # return sudoku witch id index, convert string to array
    sesja = Session()

    for i in sesja.query(Sudoku).filter(Sudoku.id == index).limit(1):
        sudoku_string = i.board

    sudoku_array = [[0 for x in range(9)] for y in range(9)]
    j = -1
    for l in range (len(sudoku_string)):

        i = l % 9
        if l % 9 == 0:
            j += 1

        sudoku_array[j][i] = int(sudoku_string[l])
    sesja.close()

    return sudoku_array

return_sudoku(1)