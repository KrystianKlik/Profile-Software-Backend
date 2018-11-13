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
                print(listOfWords)

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

        print(dictionary)

        return dictionary

    def biggestValue(self, d):
        """ a) create a list of the dict's keys and values;
            b) return the key with the max value"""
        v=list(d.values())
        k=list(d.keys())
        word = k[v.index(max(v))]
        print(f'The biggest value is {word} with {max(v)}  points')

    def findPoints(directory, counting_scores, points):
        print (counting_scores)




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
    p = a.counting_scores()
    # a.findPoints(p, 10)
    a.biggestValue(p)

else:
    print("Wrong value if you don't know how to handle this check --help")
