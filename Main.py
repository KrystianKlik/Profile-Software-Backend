import argparse

class Prompt:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Your word is: {self.name}"

    def scrabble_scores(self):
        SCRABBLES_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                            (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]

        self.LETTER_SCORES = {letter: score for score, letters in SCRABBLES_SCORES
                         for letter in letters.split()}

    def counting_scores(self):
        self.scrabble_scores()
        list_name = list(self.name)

        total_score = 0
        for i in range(len(list_name)):
            for letter, score in self.LETTER_SCORES.items():
                if list_name[i].upper() == letter:
                    total_score = total_score + score
        return print(total_score)


class Text(Prompt):

    def __repr__(self):
        return f"You are using {self.name}.txt file"

    def counting_scores(self):


        self.scrabble_scores()

        with open(args.source + ".txt", 'r') as file:
            data = file.readlines()

        for line in data:
            words = line.split()

        arrayOfScore = []
        total_score = 0

        for line in range(len(words)):
            for word in range(len(words[line])):
                for letter, score in self.LETTER_SCORES.items():
                    if words[line][word].upper() == letter:
                        total_score += score
            arrayOfScore.append(total_score)
            total_score = 0

        dictionary = dict(zip(words, arrayOfScore))

        indexOfBiggestValue = arrayOfScore.index(max(arrayOfScore))
        print(f'The biggest value is: {words[indexOfBiggestValue]}')
        print(f'This is to check values: {dictionary}')


parser = argparse.ArgumentParser()
parser.add_argument('type', help="If it's a file with extension .txt write [txt] on prompt write word [prompt]")
parser.add_argument('source', help="Type text in prompt or name of .txt file, note to make it easier file must be in the same folder as script")
args = parser.parse_args()


name = args.source

if args.type == "prompt":
    print(Prompt(name))
    instance = Prompt(name)
    instance.counting_scores()

elif args.type == "txt":
    print(Text(name))
    a = Text(name)
    a.counting_scores()

else:
    print("Wrong value if you don't know how to handle this check --help")