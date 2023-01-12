def locate_cards(cards, query):
    pos = 0
    while pos < len(cards):
        if cards[pos] == query:
            return pos
        else:
            pos += 1
        if (pos == len(cards)):
            return -1


# tests = {'input': {'cards': [13, 11, 10, 7, 4, 1, 0], 'query': 7}, 'output': 3}
card = [2, 4, 5, 6, 7, 9]
query = 5
print(locate_cards(card, query))
