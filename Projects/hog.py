"""CS 61A Presents The Game of Hog."""
from unittest import result
from numpy import average
from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
FIRST_101_DIGITS_OF_PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome. 
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    sum, numRolls = 0, num_rolls
    numberOne =False
    while(numRolls > 0):
        randomNumber = dice() #zero argument function: dice is a function name that means six_sided
        if (randomNumber == 1):
            numberOne = True # not return at once because we need get all dice() result
        else:
            sum += randomNumber
        numRolls -= 1;
    if (numberOne):
        return 1
    else:
        return sum 


def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    pi = FIRST_101_DIGITS_OF_PI # which have 101 digits

    # Trim pi to only (score + 1) digit(s): so weird, why score + 1 rather score itself
    cycleIndex = 100 - score
    while (cycleIndex > 0):
        pi = pi // 10
        cycleIndex -= 1
    return pi % 10 + 3


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    if (num_rolls == 0):
        score = free_bacon(opponent_score)
    else:
        score = roll_dice(num_rolls, dice)
    return score


def extra_turn(player_score, opponent_score):
    """Return whether the player gets an extra turn."""
    return (pig_pass(player_score, opponent_score) or
            swine_align(player_score, opponent_score))


def swine_align(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Swine Align.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    """
    def gcd(x, y):
        if (y == 0):
            return x
        else:
            return gcd(y, x % y)
    
    if (player_score == 0 or opponent_score == 0):
        return False
    gcd = gcd(player_score, opponent_score)
    if (gcd >= 10):
        return True
    else:
        return False


def pig_pass(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Pig Pass.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    """
    difference = opponent_score - player_score
    if (difference > 0 and difference < 3):
        return True
    else:
        return False


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1."""
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


#######################
# Phase 2: Commentary #
#######################


def say_scores(score0, score1):
    # say_scores returns itself, meaning that the same commentary function will be called each turn.
    """A commentary function that announces the score for each player."""
    print("Player 0 now has", score0, "and Player 1 now has", score1)
    return say_scores


def announce_lead_changes(last_leader=None):
    """Return a commentary function that announces lead changes.
    """
    def say(score0, score1):
        if score0 > score1:
            leader = 0
        elif score1 > score0:
            leader = 1
        else:
            leader = None
        if leader != None and leader != last_leader:
            print('Player', leader, 'takes the lead by', abs(score0 - score1))
        return announce_lead_changes(leader)
    return say


def both(f, g):
    """Return a commentary function that says what f says, then what g says.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest
    """
    def say(score0, score1):
        return both(f(score0, score1), g(score0, score1))
    return say


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=both(say_scores, announce_lead_changes())):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    def change_player(who, playerscore, opponent):
        if extra_turn(playerscore, opponent) == True:
            return who
        else:
            return other(who)
    while (score0 < goal or score1 < goal):
        if (who == 0):
            num_rolls_0 = strategy0(score0, score1)
            score0 += take_turn(num_rolls_0, score1, dice)
            # a commentary function is called at the end of each turn
            say = say(score0, score1) # 问题的关键就是，需要把返回的函数保存为一个新的函数，名称与之前的相同
            who = change_player(who, score0, score1)
            if score0 >= goal:
                return score0, score1
            
        else:
            num_rolls_1 = strategy1(score1, score0)
            score1 += take_turn(num_rolls_1, score0, dice)
            say = say(score0, score1)
            who = change_player(who, score1, score0)
            if score1 >= goal:
                return score0, score1


def announce_highest(who, last_score=0, running_high=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    NOTE: the following game is not possible under the rules, it's just
    an example for the sake of the doctest

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(12, 0)
    >>> f2 = f1(12, 9)
    9 point(s)! The most yet for Player 1
    >>> f3 = f2(20, 9)
    >>> f4 = f3(20, 30)
    21 point(s)! The most yet for Player 1
    >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
    >>> f6 = f5(21, 47)
    >>> f7 = f6(21, 77)
    30 point(s)! The most yet for Player 1
    """
    # 这里我真的觉得很奇怪，测试数据没有给出score，判错了也不知道为啥
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # python的函数中和全局同名的变量，如果你有修改变量的值就会变成局部变量，对该变量的引用自然就会出现没定义这样的错误了。
    def say(score0, score1): # 只要是function里面有print的，最好用一个say function定义
        score = score0 if who == 0 else score1
        gain, last_score_update = score - last_score, score
        # 注意local变量, 这里如果定义为一个新的score, 会认为是一个新的score0
    
        if (gain > running_high):
            print(gain, "point(s)! The most yet for Player", who)
            running_high_update = gain
        else:
            running_high_update = running_high
            # 这一步不能省略，如果省略就会出现调用了runnning_high_update，但是这个变量却没有声明
        return announce_highest(who, last_score_update, running_high_update)
    return say

#######################
# Phase 3: Strategies #
#######################


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def make_averaged(original_function, trials_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    """
    # 技巧：*arg的使用, Instead of listing formal parameters for a function, you can write *args. 
    # To call another function using exactly those arguments, you call it again with *args.
    def average(*arg):
        sum = 0
        count = trials_count
        while (count > 0):
            result = original_function(*arg) # 不需要全部列出formal parameters
            sum += result
            count -= 1 # C++和python处理循环次数的习惯不同
        return sum / trials_count
    return average


def max_scoring_num_rolls(dice=six_sided, trials_count=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over TRIALS_COUNT times.
    Assume that the dice always return positive outcomes.

    """
    average_roll = make_averaged(roll_dice) # origin function
    # average_roll是一个function: average, 需要进一步传入参数，也就是roll_dice的参数
    n, high_score, high_dice = 1, 0, 0  # high_dice先announce
    while (n <= 10):
        score = average_roll(n, dice)
        if (score > high_score):
            high_score, high_dice = score, n
        n += 1
    return high_dice


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)

    if True:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if True:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True:  # Change to True to test extra_turn_strategy
        print('extra_turn_strategy win rate:', average_win_rate(extra_turn_strategy))

    if False:  # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"



def bacon_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice if that gives at least CUTOFF points, and
    rolls NUM_ROLLS otherwise.
    """
    score0roll = free_bacon(opponent_score)
    if (score0roll >= cutoff):
        return 0
    else:
        return num_rolls


def extra_turn_strategy(score, opponent_score, cutoff=8, num_rolls=6):
    """This strategy rolls 0 dice when it triggers an extra turn. It also
    rolls 0 dice if it gives at least CUTOFF points and does not give an extra turn.
    Otherwise, it rolls NUM_ROLLS.
    """
    bacon_point = free_bacon(opponent_score)
    with_free_bacon = score + free_bacon(opponent_score)
    if (bacon_point >= cutoff or extra_turn(with_free_bacon, opponent_score)):
        return 0
    else:
        return num_rolls

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Replace this statement
    # END PROBLEM 12

##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()