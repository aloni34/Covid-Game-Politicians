from point import Point
from Meizags import *
# region Class : Player

class Player(Point):
# region info
    """
        This Class player which will be player by the users on the board

        :param x: the x position on the board game
        :type x: int
        :param y: the y position on the board game
        :type y: int
        :param self.position: the position on the list of players which allow the program control properly the flow of players (who play first, second, etc...)
        :type self.position: int
        :param self.list_of_Meizags: a list of Meizags which will be the 'card' which will help to determine if in an encounter between two player the player won or lost
        :type self.list_of_Meizags: list
        :param super: the point (position) of the player
        :type super: Point
        :return: Nothing
        :rtype: None
    """

    # endregion
# region Constructer
    def __init__(self, x = 0, y = 0, position = 0):
        super().__init__(x, y)
        self.list_of_Meizags = []
        self.position = position
    # endregion
# region Methods
    def addMeizag(self, Meizag):
        self.list_of_Meizags.append(Meizag)

    def add_list_of_Meizags(self, list_meizags):
        for i in range(len(list_meizags)):
            self.list_of_Meizags.append(i)

    def get_list_of_Meizag(self):
        return self.list_of_Meizags

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position


    def Stronger(self, Player):
        # region info
        """
            This function returns which player won. 0 = Draw, 1 = self won, 2 = Player won

            :param Player: the other player we check
            :type Player: Player
            :param helper: empty list for checking
            :type helper: list

            :return: the chosen word and the amount of words in the file
            :rtype: tuple(int, str)
        """
        # endregion
        other_list_of_Meizags = Player.get_list_of_Meizag()
        helper = []


        if self.list_of_Meizags == helper and other_list_of_Meizags != helper:
            return 2
        if self.list_of_Meizags != helper and other_list_of_Meizags == helper:
            return 1
        if self.list_of_Meizags == helper and other_list_of_Meizags == helper:
            return 0


        len_other = len(other_list_of_Meizags)
        len_mine = len(self.list_of_Meizags)

        for i in range((min(len_other, len_mine))):

            other = other_list_of_Meizags[i]
            mine = self.list_of_Meizags[i]

            if (isinstance(mine, Demonstration_Sign) and isinstance(other, Arrangement)) or (isinstance(mine, Arrangement) and isinstance(other, Applicator)) or (isinstance(mine, Applicator) and isinstance(other, Demonstration_Sign)):
                return 1
            if (isinstance(other, Demonstration_Sign) and isinstance(mine, Arrangement)) or (isinstance(other, Arrangement) and isinstance(mine, Applicator)) or (isinstance(other, Applicator) and isinstance(mine, Demonstration_Sign)):
                return 2

        if len_other < len_mine:
            return 1
        if len_other > len_mine:
            return 2
        return 0

    def __str__(self):
        return super().__str__()
    # endregion

# endregion