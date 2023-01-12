def test_location(card, query, mid):
    mid_num = card[mid]
    if()



def locate_cards(cards, query):
    low, high = 0, len(cards)
    while low <= high:
        mid = (low+high)//2
        mid_num = cards[mid]
        result = test_location(card, query, mid)
        if (mid_num == query):
            return mid
        elif result == 'left':
            high = mid - 1
        else:
            low = mid + 1
    return -1


card = [9, 8, 7, 5, 3, 1]
query = 5
print(locate_cards(card, query))
