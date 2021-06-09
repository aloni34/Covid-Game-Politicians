from Game_Board import *
from Game_Architest import *
# region Class : Game_Page

class Game_Page(object):

# region info
    """
    This Class responsible for summoning the classes which control how the page looks like + how the game works

    :param master: the 'father' of the page which responsible for making the page exist and connect the classes with it
    :type master: TK
    :param self.game_architest: an object which responsible for the graphic shape of the page
    :type self.game_architest: Game_Architest
    :param self.game_board: an objet which responsible for the logical gameplay + the board which is presented to player
    :type self.game_board: Game_Board

    :return: Nothing
    :rtype: None
    """

# endregion
# region Constructer
    def __init__(self, master):
        self.game_architest = Game_Architest(master)
        self.game_board = Game_Board(master, self.game_architest.get_items())
# endregion
# region Methods
    def get_game_architest(self):

        return self.game_architest

    def get_game_board(self):

        return self.game_board
    # endregion

# endregion