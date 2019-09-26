import helper
from board import *
import sys
from car import *


class Game:
    """
    This class runs the  a version of the game "rush hour" using the impliments of car and board
    """
    DEST = (3, 7)
    SYNTAX_MSG = "Invalid syntax, enter with this pattern: car_name-comma-direction with no spaces,lets try again"
    WHAT_TO_DO_MSG = "Please enter the name of the car you wanna move with and the direction you wanna move\n\n"
    WRONG_NAMES_MSG = "Invalid car name or direction, lets try again"
    ILLEGAL_MOVE = "You can't move to that way with the chosen car , lets try again"
    WIN_MSG = "Congrats!,You won the game."

    POSSIBLE_NAMES = ['Y', 'B', 'O', 'W', 'G', 'R']
    POSSIBLE_MOVES = ['u', 'd', 'r', 'l']
    POSSIBLE_ORIENTATION = [0, 1]

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """

        self.__current_board = board

    def __single_turn(self):
        """

        The function runs one round of the game :

        """
        current_board = self.__current_board

        what_to_do = input(Game.WHAT_TO_DO_MSG)

        if len(what_to_do) != 3 or what_to_do[1] != ",":
            # Checks cases when the user put wrong syntax or order
            print(Game.SYNTAX_MSG)
            return
        elif what_to_do[0] not in Game.POSSIBLE_NAMES:
            # Checks cases when the user put wrong names
            print(Game.WRONG_NAMES_MSG)
            return
        elif what_to_do[2] not in Game.POSSIBLE_MOVES:
            # Checks cases when the user put wrong names
            print(Game.WRONG_NAMES_MSG)
            return

        elif not current_board.move_car(what_to_do[0], what_to_do[2]):
            # Checks cases when the move is illegal
            print(Game.ILLEGAL_MOVE)
            return

        print(current_board)

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(self.__current_board)
        while self.__current_board.cell_content(self.DEST) == None:
            self.__single_turn()

        print(Game.WIN_MSG)
        return None


def load_cars(filename, board):
    """This function loads  cars configuration from an external file to an empty board"""
    CONFI = helper.load_json(filename)
    game_cars = []
    for i in range(len(CONFI)):
        game_cars.append((list(CONFI.keys())[i], list(CONFI.values())[i]))

    for car in game_cars:
        if car[0] in Game.POSSIBLE_NAMES and 2 <= car[1][0] <= 4 and car[1][2] in Game.POSSIBLE_ORIENTATION:
            for j in range(3):
                fit_car = Car(car[0], car[1][0], tuple(car[1][1]), car[1][2])
                if Game.DEST in fit_car.car_coordinates():
                    continue

                board.add_car(fit_car)
    return board


def main():
    """This function is the main function who runs all the other in the right order"""
    board = Board()
    loaded_board = load_cars(sys.argv[1], board)
    new_game = Game(loaded_board)
    Game.play(new_game)


if __name__ == "__main__":
    main()
