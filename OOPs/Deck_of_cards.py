import random


class DeckOfCard:
    def __init__(self):
        self.card = {"Clubs": [], "Diamonds": [], "Hearts": [], "Spades": []}
        self.suit = ("Clubs", "Diamonds", "Hearts", "Spades")
        self.rank = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
        self.player1 = {"Clubs": [], "Diamonds": [], "Hearts": [], "Spades": []}
        self.player2 = {"Clubs": [], "Diamonds": [], "Hearts": [], "Spades": []}
        self.player3 = {"Clubs": [], "Diamonds": [], "Hearts": [], "Spades": []}
        self.player4 = {"Clubs": [], "Diamonds": [], "Hearts": [], "Spades": []}
        self.player = (self.player1, self.player2, self.player3, self.player4)

    def deck_of_card(self):
        count = 36
        while count > 0:
            random_suit = self.suit[random.randrange(0, 4, 1)]
            random_rank = self.rank[random.randrange(0, 13, 1)]
            temp = self.card[random_suit]
            flag = True
            for i in range(len(temp)):
                if temp[i] == random_rank:
                    flag = False
                    break
            if flag:
                self.card[random_suit].append(random_rank)
                count -= 1

    def deck_of_card_assign_to_players(self):
        """
        Assign 9 deck of card to each player
        """
        count = 0
        for i in self.suit:
            temp = self.card[i]
            for j in range(len(temp)):
                if count >= 4:
                    count = 0
                self.player[count][i].append(temp[j])
                count += 1

    def player_card_display(self):
        for i in range(len(self.player)):
            print("\n************Player ", i + 1, "**************")
            print("Clubs : ", self.player[i]["Clubs"])
            print("Diamonds : ", self.player[i]["Diamonds"])
            print("Hearts : ", self.player[i]["Hearts"])
            print("Spades : ", self.player[i]["Spades"])


DeckOfCard()
classobj = DeckOfCard()
classobj.deck_of_card()
classobj.deck_of_card_assign_to_players()
classobj.player_card_display()
