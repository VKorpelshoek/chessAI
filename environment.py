import chess
import chess.engine

def stockfish_evaluation(board, time_limit = 0.00001):
    result = engine.analyse(board, chess.engine.Limit(time=time_limit))
    print(result)
    return result['score']

engine = chess.engine.SimpleEngine.popen_uci("/Users/vnc/Desktop/chessAI/stockfish")

board = chess.Board()

while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.00001))
    
    evaluation = stockfish_evaluation(board)
    print(evaluation.relative, end=' ')

    if(evaluation.turn == True):
        print("WHITE\n")
    else:
        print("BLACK\n")

    print(board)
    print("\n\n")
    board.push(result.move)

#print(board.Outcome.result())
engine.quit()