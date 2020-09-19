from isolation import Board
from sample_players import RandomPlayer, HumanPlayer, GreedyPlayer, open_move_score, center_score, improved_score, null_score
from game_agent import MinimaxPlayer, AlphaBetaPlayer

player1 = MinimaxPlayer(search_depth=2, score_fn=improved_score)
player2 = AlphaBetaPlayer(search_depth=3, score_fn=improved_score, limit_depth=True)

game = Board(player1, player2)

winner, history, outcome = game.play(time_limit=99999999)

print("\nWinner: {}\nOutcome: {}".format("Player 1" if winner == player1 else "Player 2", outcome))
print(game.to_string())
print("Move history:\n{!s}".format(history))
