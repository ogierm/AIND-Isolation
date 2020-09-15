from isolation import Board
from sample_players import HumanPlayer, RandomPlayer, GreedyPlayer

player1 = RandomPlayer()
player2 = HumanPlayer()

game = Board(player1, player2)

winner, history, outcome = game.play(time_limit=99999999)

print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
print(game.to_string())
print("Move history:\n{!s}".format(history))
