from random import shuffle

#تابع ایجاد دست 
def deal(numhands , n = 5):
    deck = [r+s for r in "23456789TJQKA" for s in "SHDC"]
    shuffle(deck)
    return(list(deck[n*i : n*(i+1)] for i in range(numhands)))



# تابع RANK
def card_ranks(hand):
    return sorted(['--23456789TJQKA'.index(r) for r,s in hand ],reverse = True)



#تابع دست STRAIGHT
def straight(ranks):
    return(max(ranks)-min(ranks) == 4) and len(set(ranks)) == len(ranks)


#تابع KIND
def kind(n,ranks):
    for r in ranks:
        if ranks.count(r) == n:
           return r
        return None   

#jتابع flush
def flush(hand):
    suits = [s for r,s in hand]
    return len (set(suits)) == 1
h = ['TH','2H','7H','QH','4H']
flush(h)



#تابعtwo_pair
def two_pair(ranks):
    pair = kind(2,ranks)
    low_pair = kind(2,list(reversed (ranks)))
    if low_pair != pair:
        return pair,low_pair
    else:    
        return None




def hand_rank(hand):
     ranks = card_ranks(hand)
     if straight(ranks) and flush(hand):
          return 8 , max(ranks)
     elif kind(4,ranks):
          return 7 , kind(4, ranks)
     elif kind(3, ranks) and kind(2, ranks):
          return 6 , kind(3, ranks)  
     elif flush(hand):
          return 5 , max(ranks)
     elif straight(ranks):
          return 4 , max(ranks)
     elif kind (3, ranks):
          return 3 , kind(3, ranks)
     elif two_pair(ranks):
          return 2 , two_pair(ranks)
     elif kind(2, ranks):
          return 1, kind(2, ranks)
     else:
          return 0, ranks


def poker(hands):
    return max(hands,key = hand_rank)    

hands = deal(10)
for hand in hands:
    print(hand, hand_rank(hand))
    winner = poker(hands)
print(winner, hand_rank(winner))






      