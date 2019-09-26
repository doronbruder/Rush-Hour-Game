from car import *


class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """
    SIZE = 7
    TARGET = (3, 7)

    def __init__(self):
        """This function construct a new Board object"""

        self.__cars_on_board = []
        self.__matrix = self._fill()

    def _fill(self):
        """This function fills an empty matrix to represent a board"""

        matrix = [[] for i in range(Board.SIZE)]

        for col in range(Board.SIZE):
            for row in range(Board.SIZE + 1):
                if row == 7:
                    matrix[col].append("*")
                else:
                    matrix[col].append("_")

        matrix[Board.TARGET[0]][Board.TARGET[1]] = "|_|"

        return matrix

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        visual = ""
        board = self.__matrix
        for col in range(Board.SIZE):
            visual += "   ".join(board[col]) + "\n\n"

        return visual

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cells_lst = []
        for x in range(Board.SIZE):
            for y in range(Board.SIZE):
                cells_lst.append((x, y))
        cells_lst.append(self.TARGET)
        return cells_lst

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves
        """
        directions = ['l', 'r', 'u', 'd']
        legal_moves = []

        for car in self.__cars_on_board:
            for direction in directions:
                must_emptycoors = car.movement_requirements(direction)
                for coor in must_emptycoors:
                    if not self.cell_content(coor) == None:
                        continue
                    tup = (car.get_name(), direction, "can move " + direction)
                    legal_moves.append(tup)

        return legal_moves

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return Board.TARGET

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) B,rof the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        board = self.__matrix
        if board[coordinate[0]][coordinate[1]] == "_":
            # If the place on board is represented by "_" it will be considered empty
            return None
        elif board[coordinate[0]][coordinate[1]] == "|_|":
            #  If the place on board is represented by "|_|" it will be considered empty
            # Since the target point is not on board
            return None
        return board[coordinate[0]][coordinate[1]]

    def _have_valid_place_for(self, car):
        """This function checks if a desired place to move is valid for a given car """

        cell_list = self.cell_list()
        for coor in car.car_coordinates():
            # Check if all the coordinates of a given car are on board
            if not coor in cell_list:
                return False
            elif self.cell_content(coor) != None:
                # Check if all the coordinates of a given car are empty
                return False

        return True

    def add_car(self, car):

        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        for someecar in self.__cars_on_board:
            # Make sure there is no another car with the same name in the list
            if car.get_name() == someecar.get_name():
                return False

        if self._place_car(car):
            self.__cars_on_board.append(car)
            return True

        return False

    def _place_car(self, car):
        """This function place car in another place in the board
        :param car: car object of car to place
        :return: True upon success. False if failed"""


        if self._have_valid_place_for(car):
            for coor in car.car_coordinates():
                # Change all the places in the matrix that need to be changed
                x, y = coor[0], coor[1]
                self.__matrix[x][y] = car.get_name()
            return True
        return False

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        board = self.__matrix
        for car in self.__cars_on_board:
            if car.get_name() == name:

                for coor in car.movement_requirements(movekey):
                    # Make sure all the must be empty places are empty, and are inside board
                    if not coor in self.cell_list():
                        return False

                for possible_move in self.possible_moves():
                    # Check if the car and movekey are in the possible moves list (are possible)
                    car_name, direction = possible_move[0], possible_move[1]
                    if (car_name, direction) == (name, movekey):
                        self._update_matrix(board, car, movekey)
                        return True
        return False

    def _update_matrix(self, board, car, movekey):
        """This function updated the matrix with the new cars
        :param name: name of the car to move
        :param movekey: Key of move in car to activate"""
        for coor in car.car_coordinates():
            board[coor[0]][coor[1]] = "_"
        car.move(movekey)
        self._place_car(car)
