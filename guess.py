class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = set()
        self.numTries = 0
        self.currentStatus = '-' * len(word)


    '''def display(self):
        print('Current: ' + self.currentStatus)
        print('Tries: ' + str(self.numTries))'''


    def guess(self, character):
        self.guessedChars |= {character}
        if character not in self.secretWord:
            self.numTries += 1
            return False
        else:
            currentStatus = ''
            for c in self.secretWord:
                if c in self.guessedChars:
                    currentStatus += c
                else:
                    currentStatus += '_'
            self.currentStatus = currentStatus

            return self.currentStatus == self.secretWord
    def displayCurrent(self):
        return self.currentStatus
    
    def displayGuessed(self):
        return self.displayGuessed
        
        
