import chess
import chess.engine

def stockfish_evaluation(board, time_limit = 0.00001):
    result = engine.analyse(board, chess.engine.Limit(time=time_limit))['score']
    
    stringResult = str(result.relative)
    if(stringResult.startswith('+')):
        return int(stringResult[1:])/100
    elif(stringResult.startswith('-')):
        return int(stringResult)/100
    elif(stringResult.startswith('#+')):
        return int(35000 - 100*int(stringResult[2:]))/100
    elif(stringResult.startswith('#-')):
        return ((35000 - 100*int(stringResult[2:]))*-1)/100

engine = chess.engine.SimpleEngine.popen_uci("/Users/vnc/Desktop/chessAI/stockfish")

board = chess.Board()

while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.00001))
    
    evaluation = stockfish_evaluation(board)
    print(evaluation)

    print(board)
    print("\n\n")
    board.push(result.move)

#print(board.Outcome.result())
engine.quit()