from point import Point
# region Class : Meizag

class Meizag(Point):

# region info
    """
            This Class of meizag (father of other types of Meizags)

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

# endregion
# region Class : Applicator

class Applicator(Meizag):

# region info
    """
            This Class of type of Meizag

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
    def __init__(self, x = 0,  y = 0):
        super().__init__(x, y)
    # endregion
# region Methods
    def __str__(self):
        return super().__str__() + " Applicator"
    # endregion

# endregion
# region Class : Arrangement

class Arrangement(Meizag):

# region info
    """
            This Class of type of Meizag

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
    def __init__(self, x = 0,  y = 0):
        super().__init__(x, y)
    # endregion
# region Methods
    def __str__(self):
        return super().__str__() + " Arrangement"
    # endregion

# endregion
# region Class : Demonstration_Sign

class Demonstration_Sign(Meizag):

# region info
    """
            This Class of type of Meizag

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
    def __init__(self, x = 0,  y = 0):
        super().__init__(x, y)
    # endregion
# region Methods
    def __str__(self):
        return super().__str__() + " Demonstration_Sign"
    # endregion

# endregion