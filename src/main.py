import grpc
import grpc_tools
import screen_controller as screen
import gui.menu as menu

#This is a comment.

'''
Entry point of program. Dictionary is created that switches between different screens.
menu.py returns a value.
1 = Player vs Player
2 = Player vs CPU

@author John Harris
'''
if __name__ == '__main__':
    screen_dict = {'start': menu.StartMenu}
    val = screen_dict.get('start').start('')
    print(val)
