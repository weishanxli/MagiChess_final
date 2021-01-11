# Testing module for 328p_inteface.py integration

#  WARNING: TEST WILL NOT WORK WITHOUT MODIFICATION TO GAMESTATE. CONSTRUCTOR MUST SUPPORT NONE FOR GAMEQUEUE
import importlib
from Engine.gameState import GameState as gs
#from Engine.x328p_interface import *
interface = importlib.import_module('.x328p_interface.x328p_interface', 'Engine')

currentGamestate = gs()  # Instantiate test gamestate
move = 'd2d4'

interface.make_physical_move(currentGamestate, move)
