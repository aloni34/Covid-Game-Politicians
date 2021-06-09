from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk
from Log_Board import *
from Barrier import *
from Meizags import *
from player import Player
from Constant_Values import *
import random
import math
# region Class : Game_Board

class Game_Board(object):

    # region info
    """
        This Class responsible for the gameplay on the board (in logical and graphical way)

        :param master: the 'father' of the page which responsible for making the page exist and connect the class with it
        :type master: TK
        :param items: a tuple which contains references for the input buttons [1] and the log board [0]
        :type items: tuple(Log_Board, list of buttons)
        :param self.log_board: contains a reference for the log board
        :type self.log_board: Log_Board
        :param self.icon_size: contains the size of the the icons on the board
        :type self.icon_size: int
        :param self.Image_name: contains the names of the images of meizags and barriers we want to retrieve
        :type self.Image_name: list
        :param self.Image_player_name: contains the names of the images of the players we want to retrieve
        :type self.Image_player_name: list
        :param self.active_players: contains the amount of active players we want on the game (default 3)
        :type self.active_players: int
        :param self.position: pointer which helps to track which player is playing at each move
        :type self.position: int
        :param self.list_of_labels_board: list containing labels which build the board the game take action in and presented to the user
        :type self.list_of_labels_board: list
        :param self.list_of_logic_board: list containing references to different Classes and zeros which help to determind which object is located, where there is empty place and allows functions to work
        :type self.list_of_logic_board: list
        :param self.list_of_players: list containing reference for the players. by using the self.active_players pointer on the list we can access each player in a specific order
        :type self.list_of_players: list
        :param self.list_of_Images: list containing names of images we will want to import and use on the board
        :type self.list_of_Images: list
        :param self.list_of_player_Images: list containing names of player images we will want to import and use on the board. Note that we use specific list for players becuase of the pointer which is Synchronized by the index of the list
        :type self.list_of_player_Images: list
        :param self.board_shape: the frame of the gameboard
        :type self.board_shape: Frame

        :return: Nothing
        :rtype: None
    """

    # endregion
    # region Constructer
    def __init__(self, master, items):
        # region info
        '''
            Constructs the Class and make all the default values for all the different variables

        '''
        # endregion
        # region Input Controls
        # Connects references for buttons and keybinds to help function callbacks work
        # region Commands
        items[1][0].config(command = self.OnLeft)
        items[1][1].config(command=self.OnRight)
        items[1][2].config(command=self.OnUp)
        items[1][3].config(command=self.OnDown)
        items[1][4].config(command=self.RestartGame)

        # endregion
        # region Binding
        # region Movement
        # region Keybinds
        master.bind('<a>', lambda e: self.OnLeft())
        master.bind('<Left>', lambda e: self.OnLeft())

        master.bind('<d>', lambda e: self.OnRight())
        master.bind('<Right>', lambda e: self.OnRight())

        master.bind('<w>', lambda e: self.OnUp())
        master.bind('<Up>', lambda e: self.OnUp())

        master.bind('<s>', lambda e: self.OnDown())
        master.bind('<Down>', lambda e: self.OnDown())
        # endregion
        # endregion
        # region Other
        master.bind('<r>', lambda e: self.RestartGame())
        # endregion
        # endregion
        # endregion
        # region Constants Variables
        # Stay the same
        self.log_board = items[0]
        self.icon_size = 50
        self.Image_name = ['barrier.png', 'demonstration_of_protest.jpg', 'applicator.png', 'Arrangement.jpg']
        self.Image_player_name = ['bibiking.jpg', 'miri_regev.jpg', 'Gamzo.jpg']

        # endregion
        # region Variables
        # The variables get default values and change according to the game
        self.active_players = 3
        self.position = 0

        self.list_of_labels_board = [] # 100 in total
        self.list_of_logic_board = [] # 0 - Empty place,
        self.list_of_players = [] # 3 in the start
        self.list_of_Images = [] # all Images
        self.list_of_player_Images = [] # Player images for comfortable reasons
        # endregion
        # region View
        # region Board
        # Constructs the center frame where the board will be placed in

        self.board_shape = ttk.Frame(master)
        self.board_shape.config(style = 'My.TFrame')
        #self.board_shape.grid(row = 10, columnspan = 10, padx = '10', pady = '10')
        self.board_shape.place(relx = 0.33, rely = 0.15, relwidth = 0.33, relheight = 0.587)
        self.board_shape.config(padding=(30, 15))

        # endregion
        # endregion
        # region Image Creator
        # making images based on a path and name of an image, using the image lists
        for i in self.Image_name:

            path =  main_path + "\\" + i
            image = Image.open(path)
            image = image.resize((self.icon_size, self.icon_size), Image.ANTIALIAS)
            logo = ImageTk.PhotoImage(image)
            self.list_of_Images.append(logo)

        for i in self.Image_player_name:

            path = main_path + "\\" + i
            image = Image.open(path)
            image = image.resize((self.icon_size, self.icon_size), Image.ANTIALIAS)
            logo = ImageTk.PhotoImage(image)
            self.list_of_player_Images.append(logo)


        # endregion
        # region Label creator
        # constructs the squares / labels on the page where the user will see the game and give default values for the logic board (zeros = empty place)
        for i in range(10):

            sub_list1 = []
            sub_list2 = []

            for j in range(10):

                label = ttk.Label(self.board_shape, text="", foreground="Yellow", anchor=CENTER, font=('Helvetica', 10, 'bold'), relief=RIDGE)
                label.place(relx = j * 0.1, rely = i * 0.1, relwidth = 0.095, relheight = 0.095)
                sub_list1.append(label)
                sub_list2.append(0)

            self.list_of_labels_board.append(sub_list1)
            self.list_of_logic_board.append(sub_list2)

        # endregion
        # region Spawners
        # This place responsible for making the other objects and Synchronize them between the logic board and the label board

        for i in range(3): # Barrier Spawner

            x, y = self.Empty_location_creator()
            self.list_of_logic_board[y][x] = Barrier(x, y)
            self.list_of_labels_board[y][x].config(image = self.list_of_Images[0])

        for i in range(2): # Sign Spawner

            x, y = self.Empty_location_creator()
            self.list_of_logic_board[y][x] = Demonstration_Sign(x, y)
            self.list_of_labels_board[y][x].config(image=self.list_of_Images[1])

        for i in range(2): # applicator Spawner

            x, y = self.Empty_location_creator()
            self.list_of_logic_board[y][x] = Applicator(x, y)
            self.list_of_labels_board[y][x].config(image=self.list_of_Images[2])

        for i in range(2): # Arrangement Spawner

            x, y = self.Empty_location_creator()
            self.list_of_logic_board[y][x] = Arrangement(x, y)
            self.list_of_labels_board[y][x].config(image=self.list_of_Images[3])

        for i in range(self.active_players): # Player Spawner

            x, y = self.Empty_location_creator()
            self.list_of_logic_board[y][x] = Player(x, y, i)
            self.list_of_labels_board[y][x].config(image=self.list_of_player_Images[i])
            self.list_of_players.append(self.list_of_logic_board[y][x])
        # endregion

    # endregion
    # region Restart Game
    def RestartGame(self):
        # region info
        '''
        This function restarts the game and creates a new game, using the same logic as the constructer
        Same parameters as in the constructer
        :return: Nothing
        :rtype: None
        '''
        # endregion
        # region variables
        self.active_players = 3
        self.position = 0
        #self.list_of_labels_board = []
        #self.list_of_logic_board = []  # 0 - Empty place,
        self.list_of_players = []
        # endregion
        # region Label & Logic list Reset
        # Resets the logic and graphic lists
        for i in range(10):

            #sub_list1 = []
            #sub_list2 = []

            for j in range(10):

                self.list_of_labels_board[i][j]["image"] = ""
                self.list_of_logic_board[i][j] = 0
                #label = ttk.Label(self.board_shape, text="", foreground="Yellow", anchor=CENTER, font=('Helvetica', 10, 'bold'), relief=RIDGE)
                #label.place(relx=j * 0.1, rely=i * 0.1, relwidth=0.095, relheight=0.095)
                #sub_list1.append(label)
                #sub_list2.append(0)
            #self.list_of_labels_board.append(sub_list1)
            #self.list_of_logic_board.append(sub_list2)

        # endregion
        # region Spawners
        for i in range(3):  # Barrier Spawner

            x, y = self.Empty_location_creator()
            self.list_of_logic_board[y][x] = Barrier(x, y)
            self.list_of_labels_board[y][x].config(image=self.list_of_Images[0])

        for i in range(2):  # Sign Spawner

            x, y = self.Empty_location_creator()
            self.list_of_logic_board[y][x] = Demonstration_Sign(x, y)
            self.list_of_labels_board[y][x].config(image=self.list_of_Images[1])

        for i in range(2):  # applicator Spawner

            x, y = self.Empty_location_creator()
            self.list_of_logic_board[y][x] = Applicator(x, y)
            self.list_of_labels_board[y][x].config(image=self.list_of_Images[2])

        for i in range(2):  # Arrangement Spawner

            x, y = self.Empty_location_creator()
            self.list_of_logic_board[y][x] = Arrangement(x, y)
            self.list_of_labels_board[y][x].config(image=self.list_of_Images[3])

        for i in range(self.active_players):  # Player Spawner

            x, y = self.Empty_location_creator()
            self.list_of_logic_board[y][x] = Player(x, y, i)
            self.list_of_labels_board[y][x].config(image=self.list_of_player_Images[i])
            self.list_of_players.append(self.list_of_logic_board[y][x])

        self.log_board.Reset_log()
        # endregion
    # endregion
    # region Position Creator

    def Empty_location_creator(self):
        # region info
        """
        The functions returns a valid place on the logic board where something new can be spawned

        :param x: the x position on the board
        :type x: int
        :param y: the y position on the board
        :type y: int

        :return: x, y
        :rtype: tuple
        """

        # endregion


        x = random.randrange(0, 10)
        y = random.randrange(0, 10)

        while self.list_of_logic_board[y][x] != 0:

            x = random.randrange(0, 10)
            y = random.randrange(0, 10)


        return x, y

    # endregion
    # region Valid Place on board
    def is_in_board(self, x, y):
        # region info
        """
        The functions returns if the (x, y) position is on the board

        :param x: the x position on the board
        :type x: int
        :param y: the y position on the board
        :type y: int

        :return: True / False
        :rtype: bool
        """

        # endregion
        if x > 9 or y > 9 or x < 0 or y < 0:
            return False
        return True
    # endregion
    # region Empty Place on board
    def is_empty(self, x, y):
        # region info
        """
        The functions returns if the place on the board is empty, based on (x, y) position

        :param x: the x position on the board
        :type x: int
        :param y: the y position on the board
        :type y: int

        :return: True / False
        :rtype: bool
        """

        # endregion
        if self.list_of_logic_board[y][x] == 0:
            return True
        return False
    # endregion
    # region Check if it is entity
    def is_Entity(self, x, y, entity):
        # region info
        """
        The functions returns if it is an entity in the (x, y) position

        :param x: the x position on the board
        :type x: int
        :param y: the y position on the board
        :type y: int
        :param entity: an object
        :type entity: object

        :return: True / False
        :rtype: bool
        """

        # endregion
        if isinstance(self.list_of_logic_board[y][x], entity):
            return True
        return False
    # endregion
    # region Events

    def EventManager(self, a = 0, b = 0, c = 0, d = 0):

        # region info

        """
               The functions is an event manager which play the game when the key is pressed.
               first we choose the corrent player active, get his x, y position and check if the place he want to move to is empty.
               In this case left. If it is empty he will move. If there is Meizag over there the player will take it and will move over there.
               If there is another player they will fight and the one who won will move to the defeated player. the defated player is being removed from the game.
               After that the log board get a message to tell the user. The 'physical' movement is controlled by another function, UpdateMovement() for comfortable reasons.

               This functions works on the left side of the player

            # Specific new Paramters for this function

               :param a: movement by how much in the board (default 0) - X axis
               :type a: int
               :param b: movement by how much in the board (default 0) - Y axis
               :type b: int
               :param c: Advanced movement required variable (default 0) - X axis
               :type c: int
               :param d: Advanced movement required variable (default 0) - Y axis
               :type d: int
               :param x: the x position on the board
               :type x: int
               :param y: the y position on the board
               :type y: int
               :param player: the specific player we are going to work with in this case
               :type player: Player


               :return: nothing
               :rtype: None

        """
        # endregion

        player = self.list_of_players[self.position % self.active_players]

        # Gets the (x, y) position of the player

        x = player.getX()
        y = player.getY()

        # checks if the place is on the board, if not a message will appear on the board and the player move will not count (he still has the possibilty to move other ways)

        if self.is_in_board(x + a, y + b):

            # check if the place is empty

            if self.is_empty(x + a, y + b):
                self.Update_Movement(player, x, y, c, d)

            # check if the place is full by a type of Meizag and if so doing the correct changes and notify the user about the change

            elif self.is_Entity(x + a, y + b, Meizag):

                self.log_board.Update_log("Player " + str(player.get_position() + 1) + " grabed: " + (str(type(self.list_of_logic_board[y + b][x + a])).split('.')[1][:-2]))
                player.addMeizag(self.list_of_logic_board[y + b][x + a])
                self.Update_Movement(player, x, y, c, d)

            # check if the place is full by a Player and if so doing the correct changes and notify the user about the change (check who won in the fight, remove the failed player, move the winner to the position of the failed player)
            # If there is a draw they will stay in the same place and the correct player will have his turn

            elif self.is_Entity(x + a, y + b, Player):

                Who_won = self.list_of_players[self.position].Stronger(self.list_of_logic_board[y + b][x + a])
                Remove_player = self.list_of_logic_board[y + b][x + a]
                position1 = player.get_position()
                position2 = Remove_player.get_position()
                self.WonCase(Who_won, position1, position2, Remove_player, player, x, y, c, d)

            else:
                self.log_board.Update_log(
                    "Player " + str(player.get_position() + 1) + " failed to move\nReason: Invalid Place")
        else:
            self.log_board.Update_log(
                "Player " + str(player.get_position() + 1) + " failed to move\nReason: Invalid Place")

    def OnLeft(self):
        # region info

        """
               This function call EventManager() to play according to the event with specific variables entered

               :return: nothing
               :rtype: None

        """
        # endregion
        self.EventManager(-1, 0, -1)

    def OnRight(self):
        # region info

        """
               Same as Onleft(), but work on the right side
        """
        # endregion
        self.EventManager(1, 0, 1)

    def OnUp(self):
        # region info

        """
               Same as Onleft(), but work on the up side
        """
        # endregion
        self.EventManager(0, -1, -1, 1)

    def OnDown(self):
        # region info

        """
               Same as Onleft(), but work on the down side
        """
        # endregion
        self.EventManager(0, 1, 1, 1)

    # endregion
    # region Logic + Graphic Movement
    def Update_Movement(self, player, x, y, k, m = 0): # m = 0 (X axis Movement), m = 1 (Y axis Movement)
        # region info

        """
               The function responisbles for the 'Physical' movement of the player.
               It checks if we work on x or y axis by m (0 = x axis, 1 = y axis). Afterwards we remove the player from his position,
               insert the player in the new location and delete the object which was there. This takes place on the logic board. After we update the label board
               and set the new position for the player and move the pointer for the next player to play. if the player pointer is bigger than the total players we reset it to zeros ro reset the turns.

               This functions works on the left side of the player

            # Specific new Paramters for this function

               :param x: the x position on the board
               :type x: int
               :param y: the y position on the board
               :type y: int
               :param k: how many steps to move from a certain point of the player
               :type k: int
               :param m: allow to know if to work with the x axis or the y axis
               :type m: int
               :param player: the specific player we are going to work with in this case
               :type player: Player


               :return: nothing
               :rtype: None

        """
        # endregion
        if m == 0: # X axis movement

            # Remove the player from the logic list
            self.list_of_logic_board[y].remove(player)

            # Insert the player in the other index in the logic list

            self.list_of_logic_board[y].insert(x + k, player)

            # Reset the outdated logic index to 0 for finding empty places

            self.list_of_logic_board[y][x] = 0

            # Update the graphic list and destory the outdated label

            self.list_of_labels_board[y][x + k].config(image=self.list_of_player_Images[player.get_position()])
            self.list_of_labels_board[y][x]["image"] = ''
            player.setX(x + k)
            self.position += 1


        elif m == 1: # Y axis movement

            # Same as in the X axis

            self.list_of_logic_board[y].remove(player)
            self.list_of_logic_board[y].insert(x, 0)
            del self.list_of_logic_board[y + k][x]
            self.list_of_logic_board[y + k].insert(x, player)
            self.list_of_logic_board[y][x] = 0
            self.list_of_labels_board[y + k][x].config(image=self.list_of_player_Images[player.get_position()])
            self.list_of_labels_board[y][x]["image"] = ''
            player.setY(y + k)
            self.position += 1

        # Important for utilizing the correct player turn (reached the highest index)

        if self.position == self.active_players:
            self.position = 0
    # endregion
    # region Collision Between 2 players
    def WonCase(self, Who_won, position1, position2, Remove_player, player, x, y,  k = 0, m = 0):
        # region info

        """
               The functions responisble for collision between two players.
               It checks if we work on x or y axis by m (0 = x axis, 1 = y axis). Afterwards we check who won by the Who_won parameter (0 = Draw, 1 = Player won, 2 = Remove_player)
               If no one won nothing will change. If the one who attacked won, Player, he will move to the other player position, remove him from the game and take all of his Meizags.
               Works the same if the other player won. After someone of them won and the change have been made the total player counter will decrese by one. The next player to play is the next one
               and not the same player. In the same time we update the log to notify the user of the changes.

               This functions works on the left side of the player

            # Specific new Paramters for this function

               :param x: the x position on the board
               :type x: int
               :param y: the y position on the board
               :type y: int
               :param k: how many steps to move from a certain point of the player
               :type k: int
               :param m: allow to know if to work with the x axis or the y axis
               :type m: int
               :param player: the specific player we are going to work with in this case
               :type player: Player
               :param Remove_player: the specific player we fight
               :type Remove_player: Player
               :param Who_won: allow to know if player won or lost or it is a draw
               :type Who_won: int
               :param position1: position of player
               :type position1: int
               :param position2: position of Remove_player
               :type position2: int


               :return: nothing
               :rtype: None

        """
    # endregion
        if Who_won == 1:  # Player Won

            # Remove the player from the list of active players

            self.list_of_players.remove(Remove_player)

            # Important for utilizing the correct player turn

            if position1 < position2:

                self.position = position1

            else:

                self.position = position1 - 1

            # reduce the total active players

            self.active_players -= 1

            # Physical movement

            self.Update_Movement(player, x, y, k, m)

            # Log update notes

            self.log_board.Update_log("Player " + str(position1 + 1) + " won player " + str(position2 + 1) + "!")
            self.WonTheGame(position1 + 1)

        elif Who_won == 2:  # Other Won

            self.list_of_players.remove(player)

            # Same as the first big if but in the case the other player won

            if position1 < position2:

                self.position = position2 - 1

            else:

                self.position = position2

            self.active_players -= 1

            if m == 1:

                self.Update_Movement(Remove_player, x, y + k, -k, m)
            else:

                self.Update_Movement(Remove_player, x + k, y, -k, m)

            self.log_board.Update_log("Player " + str(Remove_player.get_position() + 1) + " won player " + str(player.get_position() + 1) + "!")
            self.WonTheGame(position2 + 1)

        # Draw Case

        elif Who_won == 0 and self.active_players == 2:
            self.log_board.Update_log("It is a Draw!")
    # endregion
    # region WonCase

    def WonTheGame(self, say):
        # region info
        '''
        This function notify the player if the game is ended and who won the game

        :param say: Contains the player who won the game
        :type say: int

        :return: nothing
        :rtype: None

        '''
        # endregion
        if self.active_players == 1:
            self.log_board.Update_log("Player " + str(say) + " won the game!")

    # endregion

# endregion