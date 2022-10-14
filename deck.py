import random
import copy


class Deck:
    def __init__(self) -> None:
        suite = ('S','H','D','C')
        value = ('2','3','4','5','6','7','8','9','10','J','Q','K','A')
        self.deck = []
        for st in suite:
            for val in value:
                cardVal = val + st
                self.deck.append(cardVal)
       

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self,n):
        if n >= len(self.deck):
            return self.deck
        deal_cards = [self.deck.pop() for _ in range(n)]
        return deal_cards
   
    def sort_by_suit(self):
        order = ['H','D','C','S']
        #sorted_list =  sorted(self.deck, key = lambda x : order.index(x[len(x)-1]))
        return self.deck.sort(key = lambda x : order.index(x[len(x)-1]))
        #return sorted_list
                
    def contains(self, card) -> bool:
        return card in self.deck
    
    def copy(self):
        new_deck = copy.deepcopy(self)
        return new_deck
    
    def get_cards(self):
        return tuple(self.deck)
    
    def __len__(self):
        return len(self.deck)

    

deck1 = Deck()
deck1.shuffle()
deck1.sort_by_suit()
#print(deck1.get_cards())
#print(deck1.deck)
for (i, card) in enumerate(deck1.get_cards()):
            suit = card[len(card)-1]
            if i < 13:
              # print(deck1.deck[i])
              pass
            elif i < 26:
               # print(deck1.deck[i])
               pass