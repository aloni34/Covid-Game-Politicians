from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk
from Log_Board import *
from Constant_Values import *
# region Class : Game_Architest

class Game_Architest(object):

# region info
    """
        This Class responsible the graphical shap of the page

        :param master: the 'father' of the page which responsible for making the page exist and connect the classes with it
        :type master: TK
        :param self.image_list_name: a list which contains the names of images we will want to convert to work with
        :type self.image_list_name: list
        :param self.image_size: a list which contains the sizes of the images in the same index order as the above list
        :type self.image_size: list
        :param self.image_list: a list which contains images which helps other function to work with and print these images to the page
        :type self.image_list: list
        :param self.log_board: a log which display messages for the users who play the game
        :type self.log_board: Log_Board
        :param self.controlButtons: a list which contains all the buttons which allow inputs from the user to be understood
        :type self.controlButtons: list
        :param self.s1: a style which allow easy styles to be called
        :type self.s1: Style
        :param self.s2: same as above
        :type self.s2: Style


        :param self.frame1: a frame which controls a separated place on the page (in this case the 'Ceiling')
        :type self.frame1: ttk.Frame
        :param self.frame1_2: same as above (in this case the 'Lower Ceiling')
        :type self.frame1_2: ttk.Frame
        :param self.frame2: same as above (in this case the 'Left side')
        :type self.frame2: ttk.Frame
        :param self.frame3: same as above (in this case the 'Right Frame')
        :type self.frame3: ttk.Frame
        :param self.frame4: same as above (in this case the 'Bottom')
        :type self.frame4: ttk.Frame

        :param self.label1: a label which will be localized in a place on the page (in this case in the 'Ceiling')
        :type self.label1: ttk.Label

        :param self.canvas1: a canvas which will be localized in a place on the page  (in this case in the 'Ceiling')
        :type self.canvas1: ttk.Canvas
        :param self.canvas2: same as above (in this case in the 'Ceiling')
        :type self.canvas2: ttk.Canvas
        :param self.canvas3: same as above (in this case in the 'Left')
        :type self.canvas3: ttk.Canvas
        :param self.canvas4: same as above (in this case in the 'Left')
        :type self.canvas4: ttk.Canvas

        :param self.control_button1: a button which will call function in the game by pressing on it
        :type self.control_button1: ttk.Button
        :param self.control_button2: same as above
        :type self.control_button2: ttk.Button
        :param self.control_button3: same as above
        :type self.control_button3: ttk.Button
        :param self.control_button4: same as above
        :type self.control_button4: ttk.Button
        :param self.control_button5: same as above
        :type self.control_button5: ttk.Button


        :return: Nothing
        :rtype: None
    """
# endregion
# region Constructer
    def __init__(self, master):

        # region Image Lists

        self.image_list_name = ['israel_flag.jpg', 'stop_covid19.jpg', 'healthcare1.png', 'left_sign.png', 'right_sign.png', 'up_sign.png', 'down_sign.png', 'Restart.png']
        self.image_size = [[422, 122], [int(page_width*0.208) , int(page_height*0.28)], [int(page_width*0.208) , int(page_height*0.28)], [100, 60], [100, 60], [100, 60], [100, 60], [100, 45]]
        self.image_list = []

        # endregion
        # region Styles

        self.s1 = Style()
        self.s1.configure('My.TFrame', anchor= CENTER, background = page_color)
        self.s2 = Style()
        self.s1.configure('My_center.TFrame', anchor=CENTER, background='alice blue')

        # endregion
        # region Image Convertor
        # make images from the path and names
        for i in range(len(self.image_list_name)):
            self.image = Image.open(main_path + '\\' + self.image_list_name[i])
            self.image = self.image.resize((self.image_size[i][0], self.image_size[i][1]), Image.ANTIALIAS)
            self.logo1 = ImageTk.PhotoImage(self.image)
            self.image_list.append((self.logo1))

        # endregion
        # region Upper Frame

        self.frame1 = ttk.Frame(master)
        self.frame1.config(style='My.TFrame')
        self.frame1.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)
        self.frame1.config(padding=(30, 15))

        self.label1 = ttk.Label(self.frame1, text = "Fight The COVID-19", foreground="black", anchor= CENTER, font= ('Helvetica', 24, 'bold'), relief = RIDGE)
        self.label1.place(relx = 0.5, rely = 0.5, anchor='center', relwidth = 0.4, relheight = 0.8)

        self.canvas1 = Canvas(self.frame1)
        self.canvas1.pack()
        self.canvas1.place(relx = 0.02, rely = 0, relwidth = 0.22, relheight = 1.8)
        self.canvas1.create_image(200, 48, image = self.image_list[0])

        self.canvas2 = Canvas(self.frame1)
        self.canvas2.pack()
        self.canvas2.place(relx = 0.76, rely = 0, relwidth = 0.22, relheight = 1.8)
        self.canvas2.create_image(200, 48, image= self.image_list[0])



        # endregion  # Upper Frame (Title)
        # region Upper 2 Frame
        self.frame1_2 = ttk.Frame(master)
        self.frame1_2.config(style='My.TFrame')
        self.frame1_2.place(relx= 0.1, rely=0.1, relwidth=1, relheight=0.07)
        self.frame1_2.config(padding=(30, 15))
        self.control_button5 = ttk.Button(self.frame1_2, text='',  image = self.image_list[7], compound = CENTER) # image = self.image_list[7]

        self.control_button5.place(relx=0.12, rely=0.1, relwidth=0.1, relheight=1)
        # endregion
        # region Left Frame

        self.frame2 = ttk.Frame(master)
        self.frame2.config(style='My.TFrame')
        self.frame2.place(relx = 0.02, rely = 0.18, relwidth = 0.208, relheight = 0.6)
        self.frame2.config(padding=(30, 15))

        self.canvas3 = Canvas(self.frame2)
        self.canvas3.pack()
        self.canvas3.place(relx = 0, rely = 0)
        self.canvas3.create_image(175, 130, image = self.image_list[1])

        self.canvas4 = Canvas(self.frame2)
        self.canvas4.pack()
        self.canvas4.place(relx=0, rely=0.5)
        self.canvas4.create_image(175, 130, image = self.image_list[2])

        # endregion
        # region Right Frame

        self.frame3 = ttk.Frame(master)
        self.frame3.place(relx = 0.755, rely = 0.14, relwidth=0.208, relheight=0.6)
        self.frame3.config(padding=(30, 15))
        self.log_board = Log_Board(self.frame3)



        # endregion
        # region Down Frame
        self.frame4 = ttk.Frame(master, style='My.TFrame')
        self.frame4.place(relx=0.32, rely=0.75, relwidth=0.35, relheight=0.2)
        self.frame4.config(padding=(30, 15))

        self.control_button4 = ttk.Button(self.frame4, text='Down', image = self.image_list[6])
        self.control_button4.place(relx=0.32, rely=0.65, relwidth=0.25, relheight=0.4)

        self.control_button3 = ttk.Button(self.frame4, text='Up', image = self.image_list[5])
        self.control_button3.place(relx=0.32, rely=0, relwidth=0.25, relheight=0.4)

        self.control_button1 = ttk.Button(self.frame4, text='Left', image = self.image_list[3])
        self.control_button1.place(relx=0.075, rely=0.32, relwidth=0.25, relheight=0.4)

        self.control_button2 = ttk.Button(self.frame4, text='Right', image = self.image_list[4])
        self.control_button2.place(relx=0.565, rely=0.32, relwidth=0.25, relheight=0.4)

        self.controlButtons = [self.control_button1, self.control_button2, self.control_button3, self.control_button4, self.control_button5]



        # endregion

# endregion
# region Methods

    def get_items(self):
        return self.log_board, self.controlButtons
    # endregion

# endregion