# File Name:     high_score.py
# Programmer:    Annie Center
# Date:          Nov. 18, 2019


class HighScore:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def toString(self):
        return str(self.name) + " " + str(self.score)
