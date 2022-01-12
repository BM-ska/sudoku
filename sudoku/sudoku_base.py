from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, ForeignKey, String, DateTime, select
from sqlalchemy import create_engine, func
from sqlalchemy.orm import validates
from sqlalchemy.orm import sessionmaker
import re

Base = declarative_base()


class Sudoku(Base):
    __tablename__ = 'Sudoku'

    id = Column(Integer, primary_key=True)
    board = Column(String(81), nullable=False)
    creator = Column(String)


engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


def print_all_sudoku():
    sesja = Session()

    for i in sesja.query(Sudoku).all():
        print(i.id, " ", i.board, " ", i.creator)

    sesja.close()


def convert_sudoku_to_string(s):
    # convert array to string
    sudoku_string = ""

    for i in s:
        for j in i:
            sudoku_string += str(j)

    return sudoku_string


def add_sudoku(s, creator):
    # add sudoku to table

    sudoku_string = convert_sudoku_to_string(s)

    if not (bool(re.match(r'^\d{81}$', sudoku_string))):
        raise ValueError("sudoku format not corrected")

    sesja = Session()

    new_sudoku = Sudoku(board=sudoku_string, creator=creator)
    sesja.add(new_sudoku)
    sesja.commit()

    sesja.close()


def select_index(index):
    # return sudoku witch id index
    sesja = Session()
    sudoku_string = ""
    for i in sesja.query(Sudoku).filter(Sudoku.id == index).limit(1):
        sudoku_string = i.board

    sesja.close()
    return sudoku_string


def return_array_sudoku(index):
    #  convert string to array

    if (type(index) != int):
        raise ValueError("index must be of type int ")

    if (index > get_number_of_sudoku()):
        raise ValueError("id outside the base")

    s_string = select_index(index)
    sudoku_array = [[0 for x in range(9)] for y in range(9)]
    j = -1
    for l in range(len(s_string)):

        i = l % 9
        if l % 9 == 0:
            j += 1

        sudoku_array[j][i] = int(s_string[l])

    return sudoku_array


def get_number_of_sudoku():
    # return returns the number of sudoku in the database

    sesja = Session()
    number = sesja.query(func.count(Sudoku.id)).scalar()
    sesja.close()

    return number


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
