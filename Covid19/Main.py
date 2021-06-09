# region imports
from Game_Page import *
from Constant_Values import *
# endregion
# region Functions
def Play_Game():

    root = Tk()
    root.title("Alpha")
    root.geometry(str(page_width)+"x"+str(page_height))
    root.resizable(0, 0)
    root['bg'] = page_color
    Game = Game_Page(root)







    root.mainloop()

# endregion
# region Main
def Main():
    Play_Game()

# endregion


if __name__ == "__main__":
    Main()