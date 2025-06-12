from game import Game
from agent import Agent


def main():
    agent1 = Agent(color='red', player_id=1)
    agent2 = Agent(color='black', player_id=2)

    game = Game(agent1, agent2)

    while not game.is_over:
        if not game.do_turn():
            continue


if __name__ == "__main__":
    main()
