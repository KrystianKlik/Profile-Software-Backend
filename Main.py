import sys

class Command:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Your word is: {self.name}"

    def counting_scores(self):

        SCRABBLES_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                            (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

        LETTER_SCORES = {letter: score for score, letters in SCRABBLES_SCORES
                         for letter in letters.split()}

        list_name = list(self.name)

        total_score = 0
        for i in range(len(list_name)):
            for letter, score in LETTER_SCORES.items():
                if list_name[i].upper() == letter:
                    total_score = total_score + score
        return print(total_score)

name = sys.argv[1]

print(Command(name))
instance = Command(name)
instance.counting_scores()