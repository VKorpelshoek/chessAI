import numpy as np
import matplotlib.pyplot as plt
import chess
import chess.engine

board = chess.Board()

def reset()
    board.reset()

def actionSpaceSample():
    return np.random.choice(board.legal_moves)

def maxAction(Q, board, actions):
    values = np.array([Q[board,a] for a in actions])
    action = np.argmax(values)
    return actions[action]

if __name__ == '__main__':
    
    # model hyperparameters
    ALPHA = 0.1
    GAMMA = 1.0
    EPS = 1.0

    Q = {}
    for board in stateSpacePlus:
        for action in possibleActions:
            Q[board, action] = 0

    numGames = 50000
    totalRewards = np.zeros(numGames)
    for i in range(numGames):
        if i % 10 == 0:
            print('starting game ', i)
        done = False
        epRewards = 0
        reset()
        while not done:
            rand = np.random.random()
            possibleActions = board.legal_moves
            action = maxAction(Q,observation, possibleActions) if rand < (1-EPS) else actionSpaceSample()
            observation_, reward, done, info = step(action)
            epRewards += reward

            action_ = maxAction(Q, observation_, possibleActions)
            Q[observation,action] = Q[observation,action] + ALPHA*(reward + GAMMA*Q[observation_,action_] - Q[observation,action])
            observation = observation_
        if EPS - 2 / numGames > 0:
            EPS -= 2 / numGames
        else:
            EPS = 0
        totalRewards[i] = epRewards

    plt.plot(totalRewards)
    plt.show()