# File Name:     scoreboard.py
# Programmer:    Annie Center
# Date:          Nov. 18, 2019

from high_score import HighScore


class Scoreboard:
    def __init__(self):
        scoreFile = open("high_scores")
        fileString = scoreFile.read()
        data = fileString.split()
        self.top10 = []

        hs0 = HighScore(data[0], data[1])
        hs1 = HighScore(data[2], data[3])
        hs2 = HighScore(data[4], data[5])
        hs3 = HighScore(data[6], data[7])
        hs4 = HighScore(data[8], data[9])
        hs5 = HighScore(data[10], data[11])
        hs6 = HighScore(data[12], data[13])
        hs7 = HighScore(data[14], data[15])
        hs8 = HighScore(data[16], data[17])
        hs9 = HighScore(data[18], data[19])

        self.top10.append(hs0)
        self.top10.append(hs1)
        self.top10.append(hs2)
        self.top10.append(hs3)
        self.top10.append(hs4)
        self.top10.append(hs5)
        self.top10.append(hs6)
        self.top10.append(hs7)
        self.top10.append(hs8)
        self.top10.append(hs9)

    def addScore(self, name, score):
        self.top10.append(HighScore(name, score))

    def sortScores(self):
        n = len(self.top10)

        for bottom in range(n - 1):
            mp = bottom
            for i in range(bottom + 1, n):
                if int(self.top10[i].score) > int(self.top10[mp].score):
                    mp = i

            self.top10[bottom], self.top10[mp] = self.top10[mp], self.top10[bottom]

    def saveScores(self):
        saveFile = open("high_scores", "w")
        for score in self.top10:
            print(score.toString(), file=saveFile)



