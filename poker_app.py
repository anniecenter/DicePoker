# File Name:     poker_app.py
# Programmer:    Annie Center
# Date:          Nov. 18, 2019

from dice import Dice
from scoreboard import Scoreboard
from graphics import GraphWin
from graphics import Text
from graphics import Point
from graphics import Entry
from button import Button


class PokerApp:
    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface

    def run(self):
        while self.money >= 10 and self.interface.wantToPlay():
            self.playRound()
        scoreboard = Scoreboard()
        for score in scoreboard.top10:
            if self.money > int(score.score):
                win2 = GraphWin("Dice Poker", 600, 400)
                win2.setBackground("green3")
                banner = Text(Point(300, 30), "New High Score!\nPlease enter your name:")
                banner.setSize(24)
                banner.setFill("yellow2")
                banner.setStyle("bold")
                banner.draw(win2)
                textbox = Entry(Point(300, 150), 30)
                textbox.draw(win2)
                enter_btn = Button(win2, Point(300, 200), 60, 30, "Enter")
                enter_btn.activate()
                p = win2.getMouse()
                playerName = str(textbox.getText())
                if enter_btn.clicked(p):
                    scoreboard.addScore(playerName, self.money)
                    scoreboard.sortScores()
                    scoreboard.saveScores()
                    break
        self.interface.close()

    def playRound(self):
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money = self.money + score
        self.interface.setMoney(self.money)

    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()
