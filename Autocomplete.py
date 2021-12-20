import readline
from AutoCorrect import correction
from ChatBot import Converse


class MyCompleter(object):  # Custom completer

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options
                                if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        try:
            return self.matches[state]
        except IndexError:
            return None


Corpus = open('Corpus.txt', 'r')
words = []
for line in Corpus:
    words.append(str(line.split(" ")[0].lower()))
completer = MyCompleter(list(words))
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

while True:
    print("You -> ", end=" ")
    userInput = input()
    if userInput == "quit":
        print("JAC -> Bye bye!")
        break
    else:
        words = userInput.split(" ")
        for i in words:
            auto = correction(i.lower())
            if auto != i.lower():
                print("Did you mean: " + auto, end=" ")
                userInput = userInput.replace(i.lower(), auto)
        choice = input("(y/n)?")
        print("You ->", userInput)
        if choice == "y":
            Converse(userInput)

