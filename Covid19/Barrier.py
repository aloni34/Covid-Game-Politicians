from point import Point
# region Class : Barrier

class Barrier(Point):

# region info
    """
        This Class of a barrier which prevent movement on the board

        :param x: the x position on the board game
        :type x: int
        :param y: the y position on the board game
        :type y: int
        :param super: the point (position) of the player
        :type super: Point
        :return: Nothing
        :rtype: None
    """

    # endregion
# region Constructer
    def __init__(self, x = 0, y = 0):
        super().__init__(x, y)
    # endregion
# region Methods
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def setY(self):
        return self.y
    # endregion

# endregion
