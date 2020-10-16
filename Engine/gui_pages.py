"""
-------------------------------
IMPORTS
-------------------------------
"""
import tkinter as tk

from chessboard import chessboard
from lichess import lichessInterface_new as interface
from GUI import gui_widgets as widgets


"""
-------------------------------
PAGE CLASSES
-------------------------------
"""

class StartupPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        header = widgets.createLabel(self, text="MagiChess", font="times", fontsize=14, fontweight="bold")
        header.pack(padx=10, pady=10)
        
        #startup buttons
        signinButton = widgets.createButton(self, function=lambda: controller.show_frame(SigninPage),
                                           text="Sign in to LiChess.org")
        signinButton.pack()
        
        exitButton = widgets.createButton(self, function=exit,
                                          text="Exit")    
        exitButton.pack()


class SigninPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        header = widgets.createLabel(self, text="Sign in to LiChess", font="times", fontsize=14, fontweight="bold")
        header.pack(padx=10, pady=10)
        
        """ username/password entries
        usernameLabel = widgets.createLabel(self, text="Username", font="times", fontsize=11, fontweight="normal")
        usernameLabel.pack()
        usernameEntry = widgets.createEntry(self, bgcolor="beige")
        usernameEntry.pack()
        
        passwordLabel = widgets.createLabel(self, text="Password", font="times", fontsize=11, fontweight="normal")
        passwordLabel.pack()
        passwordEntry = widgets.createEntry(self, bgcolor="beige", show="*")
        passwordEntry.pack()
        """
        
        
        """ buttons """
        loginButton = widgets.createButton(self, function=lambda: self.submit(controller=controller, username="degugj"),
                                           text="Login as degugj", bgcolor="seashell3")
        loginButton.pack(pady=4)
        
        returnButton = widgets.createButton(self, function=lambda: controller.show_frame(StartupPage),
                                            text="Return", bgcolor="seashell3")
        returnButton.pack(pady=7)
        
    """ submit username/password for validation """
    def submit(self, controller, username, password=None):
        valid = 1
        
        """
        Send request to LiChess to validate username/password
        """

        #Call api funtion

        if valid:
            controller.show_frame(MainMenuPage, user=username)
            print(username)
        else:
            print("User not found. Invalid username/password")
        return
        

class MainMenuPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        
    def welcomeHeader(self, username):
        header = widgets.createLabel(self, text="Welcome to MagiChess, " + username, font="times", fontsize=14, fontweight="bold")
        header.pack(padx=10, pady=10)
        
    def menuButtons(self, controller):
        """ main menu options """
        playbotButton = widgets.createButton(self, function=lambda: controller.show_frame(PlayBotPage),
                                             text="Play Bot", bgcolor="sky blue")
        playbotButton.pack(pady=5)
        
        playrandButton = widgets.createButton(self, function=lambda: controller.show_frame(PlayRandomPage),
                                             text="Seek an Opponent", bgcolor="sky blue")
        playrandButton.pack(pady=5)
        
        playfriendButton = widgets.createButton(self, function=lambda: controller.show_frame(PlayFriendPage),
                                             text="Challenge a Friend", bgcolor="sky blue")
        playfriendButton.pack(pady=5)
        
        exitButton = widgets.createButton(self, function=exit,
                                             text="Exit MagiChess", bgcolor="seashell3")
        exitButton.pack(pady=5)
        
        
""" main menu pages """
class PlayBotPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        header = widgets.createLabel(self, text="Play a Bot", font="times", fontsize=14, fontweight="bold")
        header.pack(padx=10, pady=10)
        
        #return to main menu
        returnButton = widgets.createButton(self, function=lambda: controller.show_frame(MainMenuPage),
                                            text="Return to Main Menu", bgcolor="sky blue")
        returnButton.pack()
        
class PlayRandomPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        header = widgets.createLabel(self, text="Seeking Opponent...", font="times", fontsize=14, fontweight="bold")
        header.pack(padx=10, pady=10)
        
        #return to main menu
        returnButton = widgets.createButton(self, function=lambda: controller.show_frame(MainMenuPage),
                                            text="Return to Main Menu", bgcolor="sky blue")
        returnButton.pack()
        
    def seekOpponent(self):
        """
        send request to LiChess server to seek an opponent
        """
        
        return
        
class PlayFriendPage(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        header = widgets.createLabel(self, text="Search Opponent Name", font="times", fontsize=14, fontweight="bold")
        header.pack(padx=10, pady=10)
        
        #name input and search button
        usernameEntry = widgets.createEntry(self, bgcolor="beige")
        usernameEntry.pack()
        challengeButton = widgets.createButton(self, function=lambda: self.challenge(usernameEntry.get()), text="Challenge", bgcolor="sky blue")
        challengeButton.pack()
        
        
        #return to main menu
        returnButton = widgets.createButton(self, function=lambda: controller.show_frame(MainMenuPage),
                                            text="Return to Main Menu", bgcolor="sky blue")
        returnButton.pack()
        
    """ search LiChess server for username, and challenge """
    def challenge(self, username=""):
        
        if username == "":
            print("User not found")
        else: 
            
            # challenge user and set gameid
            gameid = interface.challenge_user(username)
            if not gameid:
                print("Unable to complete challenge")
            else:
                interface.change_gameid(gameid)

                """
                show_frame(), wait for opponent to respond to challenge, and change page to chess board
                """
        return
        
        
"""
-------------------------------
FUNCTIONS
-------------------------------
"""