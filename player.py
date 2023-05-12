# Player class
class Player():   
    def __init__(self,name):
        self.name = name
        self.deck = []

    def players(self):
        return self.name, self.deck
