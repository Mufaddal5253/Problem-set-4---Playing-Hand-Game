# MIT edx Course
# Problem set 4
# Problem 1 - Word Scores


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    # 1. Word Scores
    return (len(word) * sum(SCRABBLE_LETTER_VALUES[x] for x in word)) + (50 if len(word) == n else 0)

# Test implementation
def getFrequencyDict(aStr):
    return dict((letter, aStr.count(letter)) for letter in aStr)

# Problem 2 - Dealing With Hands  



def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    return dict((a, b - word.count(a))for a, b in hand.items())


# Problem 3 - Valid Words


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    return word in wordList and all(hand.get(a,0) >= b for a, b in getFrequencyDict(word).items())


# Problem 4 - Hand Length


def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    return sum(x for x in hand.values())


# Problem 5 - Playing a Hand


def playHand(hand, wordList, n):
    totalScore = 0
    output = 'Run out of letters.'
    while calculateHandlen(hand) > 0:
        displayHand(hand)
        word = input('Enter word,or a "." to indicate that you are finished: ' ).lower()
        if word == '.':
            output = "GoodBye!"
            break
        else:
            if not isValidWord(word, hand, wordList):
                print('Invalid word, please try again.')
            else:
                score = getWordScore(word, n)
                totalScore += score
                print('"{0:s}" earned {1:d} points. Total: {2:d}.'.format(word,score, totalScore))
                hand = updateHand(hand, word)
    print('{0:s} Total Score: {1:d} points.'.format(output, totalScore))
    

# Problem 6 - PLaying a Game


def playGame(wordList):
    hand = False
    while True:
        user = input('Enter n to play a new hand, r to reply the hand, and e to end game: ').lower()
        if user not in 'nre':
            print('Invalid command.')
        else:
            if user == 'r' and not hand:
                print("You have not played a hand yet. Please play a new hand first!")
            elif user == 'n':
                hand = dealHand(HAND_SIZE)
                playHand(hand.copy(), wordList, HAND_SIZE)
            elif user == 'r' and hand:
                playHand(hand.copy(), wordList, HAND_SIZE)
            else:
                break
            print("")


# Problem 7 - You and Your Computer



def playGame(wordList):
    while True:
        user_input = str(input('Enter n to deal a new hand, r to replay the last hand, or e to end game: '))
        if user_input == 'e':
            break
        elif user_input == 'n':
            while True:
                play_mode = str(input('Enter u to have yourself play, c to have the computer play: '))
                if play_mode == 'u':
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    break
                elif play_mode == 'c':
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print('Invalid command.')            
        elif user_input == 'r':
            try:
                hand
                play_mode = str(input('Enter u to have yourself play, c to have the computer play: '))
                if play_mode == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                elif play_mode == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                else:
                    print('Invalid command.')
            except:
                print('You have not played a hand yet. Please play a new hand first!')
        else:
            print('Invalid command.')
