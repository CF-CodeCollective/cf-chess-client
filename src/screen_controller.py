import gui.menu as menu

class ScreenController:

    def create_screens(self):
        print("creating screens")
        screen_dict = {'start': menu.StartMenu}