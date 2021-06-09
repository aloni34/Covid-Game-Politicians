# region Class : Point

class Point(object):

# region info
    """
        This Class responsible for position of objects on the board game

        :param x: the x position on the board game
        :type x: int
        :param y: the y position on the board game
        :type y: int

        :return: Nothing
        :rtype: None
    """

    # endregion
# region Constructer
    def __init__(self, x = 0, y = 0):

        self.x = x
        self.y = y
    # endregion
# region Methods
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):

        return "X: " + str(self.x) + ", Y: " + str(self.y)
    # endregion

# endregion