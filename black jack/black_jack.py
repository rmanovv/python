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


def ask_for_bet(balance, min_bet):
    '''Ask the player to bet some amount'''
    
    assert min_bet >= balance, "Not enough balance"
    
    while True:
        say("How much would you want to wager this time?")
        try:
            bet = input('>>')
            bet = float(bet)

            if bet > balance:
                say("You don't have that kind of money on your account!")
            elif bet < 0:
                say("Negative bets not are allowed you... cheater!")
            elif bet < min_bet:
                say("Bet of must be above of {}".format(min_bet))
            else:
                balance -= bet
                say("Bet of %.2f accepted!" %bet)
                return bet, balance

        except ValueError:
            say("{} is not a valid bet! Please enter enter floating point number".format(bet))
            

if __name__ == '__main__':
    say_welcome()
    init_shoe()
