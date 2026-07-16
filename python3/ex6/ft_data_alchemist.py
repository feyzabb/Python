import random


def ft_data_alchemist():
    print("=== Game Data Alchemist ===")
    print()

    players = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john",
               "kevin", "Liam"]

    print(f"Initial list of players: {players}")

    capitalized_players = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized_players}")

    already_capitalized = [name for name in players if name[0] >= "A"
                           and name[0] <= "Z"]
    print(f"New list of capitalized names only: {already_capitalized}")

    score_dict = {name: random.randint(0, 1000) for name in
                  capitalized_players}
    print(f"Score dict: {score_dict}")

    average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(average, 2)}")

    high_scores = {name: score for name, score in
                   score_dict.items() if score > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
