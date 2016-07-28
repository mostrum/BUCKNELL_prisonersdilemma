####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random

team_name = 'UFOs' # Only 10 chars displayed.
strategy_name = 'Poker players'
strategy_description = 'Odds based on previous outcomes'

listBC = ['b', 'c']
compare = 0
cl = 'b'    
            
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    compare = 0
    listBC = ['b', 'c']
    cl = 'b'
    if len(my_history) == 1:
        listBC = ['b', 'c']    
        cl = random.choice(listBC)
        print cl
        #return cl
        
    elif len(my_history) == 2:
        listBC = ['b', 'c']    
        cl = random.choice(listBC)
        print cl
        #return cl
        compare = my_score
    
    else:
        if my_score >= compare:
            listBC += cl
        else:
            if cl == 'b':
                listBC += 'c'
            else:
                listBC += 'b'
        cl = random.choice(listBC)
        #return cl
    #return listBC
    compare = my_score
    print listBC
    return cl
    

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    listBC = ['b', 'c']
    compare = 0
    cl = 'b'

    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbbcccbb',
              their_history='cccbbbcc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             