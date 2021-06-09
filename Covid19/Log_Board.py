from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk
# region Class : Log_Board

class Log_Board(object):

# region info
    """
        This Class responsible for displaying the users the flow of the game (valid locations, collisions, winning player, etc...)

        :param master: the 'father' of the page which responsible for making the page exist and connect the classes with it
        :type master: TK
        :param self.log: a list contating strings we want to display on the log
        :type self.log: list
        :param self.lines_amount: the amount of lines we will want our log to be
        :type self.lines_amount: int
        :param self.labels: a list of labels which display the output on the page
        :type self.labels: list

        :return: Nothing
        :rtype: None
    """
# endregion
# region Constructer
    def __init__(self, master):


        self.lines_amount = 10
        self.log = []
        self.labels = []

        # Reset Lines
        for i in range(self.lines_amount):
            self.log.append("")

        # Enter the welcome message
        self.log[self.lines_amount-1] = self.WelcomeMessage()

        for i in range(self.lines_amount):

            label = ttk.Label(master, text = self.log[i], foreground= "black", anchor = W, font=('Helvetica', int(120 / self.lines_amount), 'bold'))
            label.place(relx = 0, rely= i * (1 / self.lines_amount), relwidth= 1 , relheight = 0.95 / self.lines_amount)
            self.labels.append(label)
# endregion
# region Methods
    def Update_log(self, message):
        # region info
        '''
        This function update the log board and delete the latest message

        :param message: Contains the new message
        :type message: str

        :return: nothing
        :rtype: None

        '''
        # endregion

        # Update the new message if it is different from the last one and change the log view

        if message != self.log[self.lines_amount - 1]:
            # downward each note by 1
            for i in range(1, self.lines_amount):

                self.log[i - 1] = self.log[i]

            # add the new message
            self.log[self.lines_amount - 1] = message

            # downward the view in the log by 1

            for i in range(self.lines_amount):

                self.labels[i].config(text = self.log[i])


    def WelcomeMessage(self):

        return "Welcome to my game\nObjective: Save the world from Covid-19"

    def Reset_log(self):

        for i in range(0, self.lines_amount):
            self.log[i] = ""

        self.log[self.lines_amount-1] = self.WelcomeMessage()

        for i in range(self.lines_amount):
            self.labels[i].config(text=self.log[i])



    # endregion

# endregion