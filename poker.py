import random

#arrays para as cartas
hand = []
table = []

#arrays para os naipes
handSuits = []
tableSuits = []

#arrays para os números
handNumerals = []
tableNumerals = []

#dicts que convertem os números para os naipes e cartas altas
numeralDict = { 11: "Jack", 12: "Queen", 13: "King", 14: "Ace" }
suitDict = { 1: "Clubs", 2: "Spades", 3: "Hearts", 4: "Diamonds" }


#converte os números e retorna o nome da carta
def getCardName(x, y):
    if x <= 10:
        numeral = str(x)
    else:
        numeral = numeralDict[x]
    suit = suitDict[y]

    return numeral+" of "+suit

#randomiza e distribui as cartas
def getCards(arr, x):
    for i in range(x):
        card = []
    
        numeral = random.randint(2, 14)
        card.append(numeral)

        suit = random.randint(1, 4)
        card.append(suit)

        arr.append(card)

#conta quantas vezes cada naipe se repete
def getSuitCount(arr, suitArr):
    suitCount = []

    for cards in arr:
        suitArr.append(cards[1])
    for i in range(1, 5):
        suitCount.append(suitArr.count(i))

    return suitCount

#conta quantas vezes cada número se repete
def getNumeralCount(arr, numeralArr):
    numeralCount = []

    for cards in arr:
        numeralArr.append(cards[0])
    for i in range(2, 15):
        numeralCount.append(numeralArr.count(i))

    return numeralCount

#pares
def isPair():
    pairs = 0
    for i in range(13):
        if handNumeralCount[i] != 0:
            if handNumeralCount[i] + tableNumeralCount[i] == 2:
                pairs += 1

    return pairs
                
#trinca
def isThreeOfAKind():
    for i in range(13):
        if handNumeralCount[i] != 0:
            if handNumeralCount[i] + tableNumeralCount[i] == 3:
                return True

#flush
def isFlush():
    for i in range(4):
        if handSuitCount[i] != 0:
            if handSuitCount[i] + tableSuitCount[i] >= 5:
                return True
            
#quadra
def isFourOfAKind():
    for i in range(13):
        if handNumeralCount[i] != 0:
            if handNumeralCount[i] + tableNumeralCount[i] == 4:
                return True

#printa as cartas
def printCards():
    print("HAND")
    for card in hand:
        print(getCardName(card[0], card[1]))
    print("")

    print("TABLE")
    for card in table:
        print(getCardName(card[0], card[1]))
    print("")

    pair = isPair()
    threeOfAKind = isThreeOfAKind()
    flush = isFlush()
    fourOfAKind = isFourOfAKind()

    if pair == 1 and not threeOfAKind:
        print("PAIR")
    if pair == 2:
        print("TWO PAIRS")
    if threeOfAKind and not pair:
        print("THREE OF A KIND")
    if pair and threeOfAKind:
        print("FULL HOUSE")
    if flush:
        print("FLUSH")
    if fourOfAKind:
        print("FOUR OF A KIND")
    


getCards(hand, 2)
getCards(table, 5)

tableSuitCount = getSuitCount(table, tableSuits)
handSuitCount = getSuitCount(hand, handSuits)
tableNumeralCount = getNumeralCount(table, tableNumerals)
handNumeralCount = getNumeralCount(hand, handNumerals)

printCards()