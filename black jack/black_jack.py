from random import shuffle


def say(message):
    print(message)


def say_welcome(player="Player"):
    say('Hello {} and Welcome to the Casino'.format(player))


def init_shoe(num_deck=1):
    # Generate shuffled list of cards from num_deck number of deck

    suits = ['s', 'h', 'd', 'c']
    rangs = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    cards = [x+y for x in rangs for y in suits] * num_deck

    assert len(cards) == num_deck * 52

    shuffle(cards)
    say('Shuffled {} cards into the dealer shoe. Good luck!'.format(cards))
    return cards

def drow_prompt():
    # ask the player whether to draw a card or not
    pass

def hand_score(hand):
    '''
    Calculate the score of hand
    '''

    score = 0
    aces = 0

    for card in hand:
        if card[0].isdigit():
            score += int(card[:-1])
        elif card[0] in ('J', 'Q', 'K'):
            score += 10
        elif card[0] == 'A':
            aces += 1
        else:
            assert False, 'WTF did you giv me!'

    score += max([aces - 1, 0]) * 1  # all aces after first one are counted as 1 points
    score += min([aces, 1]) * (1 if score >= 11 else 11)

    return score

if __name__ == '__main__':
    say_welcome()
    init_shoe()
