from game import Game
from agents.human_agent import HumanAgent
from agents.random_agent import RandomAgent


def main():
    agent1 = HumanAgent(color='red', player_id=1)
    agent2 = RandomAgent(color='black', player_id=2)

    game = Game(agent1, agent2)

    while not game.is_over:
        if not game.do_turn():
            continue


if __name__ == "__main__":
    main()
