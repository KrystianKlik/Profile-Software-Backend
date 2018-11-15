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
        return f"Your points: {self.name}"

    def counting_scores(self):

        self.scrabble_scores()

        with open("dictionary.txt", 'r') as file:
            data = file.readlines()

        listOfWords = []
        # Cleaning data
        for line in data:
            # Deleting all whitespaces in word
            cleanLine = line.rstrip()
            if cleanLine is not '':
                # Deleting tabulation
                if '\t' in cleanLine:
                    cleanLine = cleanLine.replace('\t', '')

                listOfWords.append(cleanLine)
                lengthListOfWords = len(listOfWords)

        arrayOfScore = []
        total_score = 0

        for line in range(lengthListOfWords):
            for word in range(len(listOfWords[line])):
                for letter, score in self.LETTER_SCORES.items():
                    if listOfWords[line][word].upper() == letter:
                        total_score += score

            arrayOfScore.append(total_score)
            total_score = 0

        dictionary = dict(zip(listOfWords, arrayOfScore))

        return dictionary


    def biggestValue(self, counting_scores):
        v=list(counting_scores.values())
        k=list(counting_scores.keys())
        maxValues = [i for i, x in enumerate(v) if x == max(v)]
        for count in maxValues:
            print(f'The biggest value is {k[count]} with {max(v)} points')

    def findPoints(self, counting_scores, score):
        lengthOfDict = len(counting_scores)
        v=list(counting_scores.values())
        k=list(counting_scores.keys())
        for i in range(lengthOfDict):
            if int(score) == v[i]:
                print(f'Word: {k[i]}')


parser = argparse.ArgumentParser()
parser.add_argument('type', help="If it's a file with extension .txt write [txt] on prompt write word [prompt]")
parser.add_argument('source', help="Type text in prompt or name of .txt file, note to make it easier file must be in the same folder as script")
args = parser.parse_args()

name = args.source

if args.type == "prompt":
    print(Prompt(name))
    instance = Prompt(name)
    instance.counting_scores()


elif args.type == "txt" and args.source == "dictionary":
        instance = Text(name)
        counting_scores_function = instance.counting_scores()
        instance.biggestValue(counting_scores_function)

elif args.type == "txt":
    try:
        print(Text(name))
        instance = Text(name)
        counting_scores_function = instance.counting_scores()
        instance.findPoints(counting_scores_function, name)
    except:
        print('You need to give a proper number or check if you wrote word dictionary correctly')


else:
    print("Wrong value if you don't know how to handle this check [--help]")
