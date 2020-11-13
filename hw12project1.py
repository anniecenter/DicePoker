# File Name:     hw12project1.py
# Programmer:    Annie Center
# Date:          Nov. 18, 2019
#
# Problem Statement:  Modify the Dice Poker program from this chapter to include any or all of the following features:
# a) Splash Screen. When the program first fires up, have it print a short introductory message about the program and
# buttons for "Let's Play'' and "Exit." The main interface shouldn't appear unless the user selects "Let's Play."
# b) Add a "Help" button that pops up another window displaying the rules of the game (the payoffs table is the most
# important part).
# c) Add a high score feature. The program should keep track of the 10 best scores. When a user quits with a good enough
# score, he/she is invited to type in a name for the list. The list should be printed in the splash screen when the
# program first runs. The high-scores list will have to be stored in a file so that it persists between program
# invocations.
#
# Overall Plan:
# 1.

from graphics import GraphWin
from graphics import Point
from graphics import Text
from button import Button
from poker_app import PokerApp
from graphics_interface import GraphicsInterface
from scoreboard import Scoreboard


def main():
    win = GraphWin("Dice Poker", 600, 400)
    win.setBackground("green3")
    banner = Text(Point(300, 30), "Python Poker Parlor")
    banner.setSize(24)
    banner.setFill("yellow2")
    banner.setStyle("bold")
    banner.draw(win)
    letsPlayBtn = Button(win, Point(300, 300), 400, 40, "Let's Play!")
    letsPlayBtn.activate()
    exitBtn = Button(win, Point(300, 350), 400, 40, "Exit")
    exitBtn.activate()
    showHighScores(win)

    while True:
        p = win.getMouse()

        if letsPlayBtn.clicked(p):
            win.close()
            inter = GraphicsInterface()
            app = PokerApp(inter)
            app.run()
            break

        if exitBtn.clicked(p):
            win.close()
            break


def showHighScores(win):
    scoreboard = Scoreboard()

    location = 70
    for hs in scoreboard.top10:
        text = hs.toString()
        hsText = Text(Point(300, location), text)
        hsText.setSize(12)
        hsText.setFill("yellow2")
        hsText.setStyle("bold")
        hsText.draw(win)
        location = location + 20


main()
