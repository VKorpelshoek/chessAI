import numpy as np
import matplotlib.pyplot as plt
import chess
import chess.engine

board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci("/Users/vnc/Desktop/chessAI/stockfish")

def reward(boardCopy):
    result = engine.analyse(boardCopy, chess.engine.Limit(time=0.1))['score']
    
    stringResult = str(result.relative)

    returnVal = 0
    if(stringResult.startswith('+')):
        returnVal =  int(stringResult[1:])/100
    elif(stringResult.startswith('-')):
        returnVal =  int(stringResult)/100
    elif(stringResult.startswith('#+')):
        returnVal =  int(35000 - 100*int(stringResult[2:]))/100
    elif(stringResult.startswith('#-')):
        returnVal =  ((35000 - 100*int(stringResult[2:]))*-1)/100
    return returnVal

def reset(board,engine):
    board.reset()

def actionSpaceSample():
    return np.random.choice(list(board.legal_moves))

def maxAction(Q, newBoard):
    actions = list(newBoard.legal_moves)
    
    values = np.array([Q[newBoard,a] for a in actions])
    action = np.argmax(values)
    return actions[action]

if __name__ == '__main__':
    
    # model hyperparameters
    ALPHA = 0.1
    GAMMA = 1.0
    EPS = 1.0

    Q = {}

    numGames = 50000
    totalRewards = np.zeros(numGames)
    for i in range(numGames):
        if i % 10 == 0:
            print('starting game ', i)
        done = False
        epRewards = 0
        
        while not done:
            rand = np.random.random()
            action = maxAction(Q,board) if rand < (1-EPS) else actionSpaceSample()
            observation_ = board
            observation_.push(action)
            done = board.is_game_over()
            reward = reward(observation_)
            print(reward)
            print(board)
            epRewards += int(reward)
            
            action_ = maxAction(Q, observation_)
            Q[board,action] = Q[board,action] + ALPHA*(reward + GAMMA*Q[observation_,action_] - Q[board,action])
            board = observation_

            #other player move
            board.push(actionSpaceSample)
        if EPS - 2 / numGames > 0:
            EPS -= 2 / numGames
        else:
            EPS = 0
        totalRewards[i] = epRewards
        reset(board,engine)

    plt.plot(totalRewards)
    plt.show()