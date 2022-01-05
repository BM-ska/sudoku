from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, select
from sqlalchemy import create_engine
from sqlalchemy.orm import validates
from sqlalchemy.orm import sessionmaker
import re

Base = declarative_base()


class Sudoku(Base):
    __tablename__ = 'Sudoku'

    id = Column(Integer, primary_key=True)
    board = Column(String(81), nullable=False)
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


engine = create_engine('sqlite:///:memory:')  # , echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def print_all_sudoku():
    sesja = Session()

    for i in sesja.query(Sudoku).all():
        print(i.id, " ", i.board, " ", i.creator)

    sesja.close()


def add_sudoku(s, creator):  # add sudoku to table, convert array to string
    sudoku_string = ""
    sesja = Session()

    for i in s:
        for j in i:
            sudoku_string += str(j)

    new_sudoku = Sudoku(board=sudoku_string, creator=creator)
    sesja.add(new_sudoku)
    sesja.commit()

    sesja.close()


def return_array_sudoku(index):  # return sudoku witch id index, convert string to array
    sesja = Session()

    for i in sesja.query(Sudoku).filter(Sudoku.id == index).limit(1):
        sudoku_string = i.board

    sudoku_array = [[0 for x in range(9)] for y in range(9)]
    j = -1
    for l in range(len(sudoku_string)):

        i = l % 9
        if l % 9 == 0:
            j += 1

        sudoku_array[j][i] = int(sudoku_string[l])
    sesja.close()

    return sudoku_array


sudoku1 = [[0, 1, 0, 6, 0, 4, 3, 0, 7],
           [3, 5, 6, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 5, 3, 6, 9, 0],
           [0, 8, 3, 2, 6, 0, 4, 0, 9],
           [0, 0, 0, 0, 0, 0, 0, 0, 0],
           [4, 0, 5, 0, 7, 8, 2, 6, 0],
           [0, 4, 2, 5, 3, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 7, 2, 4],
           [7, 0, 9, 4, 0, 2, 0, 8, 0]]
sudoku2 = [[0, 1, 0, 0, 5, 6, 2, 7, 0],
           [0, 0, 0, 0, 8, 0, 0, 0, 9],
           [0, 7, 8, 0, 0, 3, 6, 0, 5],
           [0, 0, 0, 0, 0, 4, 5, 0, 1],
           [8, 5, 2, 0, 0, 0, 7, 3, 4],
           [6, 0, 1, 7, 0, 0, 0, 0, 0],
           [1, 0, 6, 4, 0, 0, 9, 5, 0],
           [3, 0, 0, 0, 6, 0, 0, 0, 0],
           [0, 2, 7, 3, 9, 0, 0, 8, 0]]

add_sudoku(sudoku1, "default")
add_sudoku(sudoku2, "default")

