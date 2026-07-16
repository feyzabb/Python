import random


def gen_player_achievements(achievement_pool):
    player_set = set()
    num_of_achievements = random.randint(5, len(achievement_pool))

    while len(player_set) < num_of_achievements:
        random_achievement = random.choice(achievement_pool)
        player_set = set.union(player_set, set([random_achievement]))

    return player_set


def main():
    print("=== Achievement Tracker System ===")

    all_possible_achievements = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Hidden Path Finder",
    ]

    alice_achievements = gen_player_achievements(all_possible_achievements)
    bob_achievements = gen_player_achievements(all_possible_achievements)
    charlie_achievements = gen_player_achievements(all_possible_achievements)
    dylan_achievements = gen_player_achievements(all_possible_achievements)

    print(f"Player Alice: {alice_achievements}")
    print(f"Player Bob: {bob_achievements}")
    print(f"Player Charlie: {charlie_achievements}")
    print(f"Player Dylan: {dylan_achievements}")

    all_distinct = set.union(
        alice_achievements,
        bob_achievements,
        charlie_achievements,
        dylan_achievements
    )

    print(f"All distinct achievements: {all_distinct}")

    common_achievements = set.intersection(
        alice_achievements,
        bob_achievements,
        charlie_achievements,
        dylan_achievements
    )

    print(f"Common achievements: {common_achievements}")

    others_for_alice = set.union(
        bob_achievements,
        charlie_achievements,
        dylan_achievements
    )
    print(f"Only Alice has:"
          f"{set.difference(alice_achievements, others_for_alice)}")

    others_for_bob = set.union(
        alice_achievements,
        charlie_achievements,
        dylan_achievements
    )
    print(f"Only Bob has: {set.difference(bob_achievements, others_for_bob)}")

    others_for_charlie = set.union(
        alice_achievements,
        bob_achievements,
        dylan_achievements
    )
    print(f"Only Charlie has:"
          f"{set.difference(charlie_achievements, others_for_charlie)}")

    others_for_dylan = set.union(
        alice_achievements,
        bob_achievements,
        charlie_achievements
    )
    print(f"Only Dylan has:"
          f"{set.difference(dylan_achievements, others_for_dylan)}")

    full_pool_set = set(all_possible_achievements)

    print(f"Alice is missing:"
          f"{set.difference(full_pool_set, alice_achievements)}")
    print(f"Bob is missing:"
          f"{set.difference(full_pool_set, bob_achievements)}")
    print(f"Charlie is missing:"
          f"{set.difference(full_pool_set, charlie_achievements)}")
    print(f"Dylan is missing:"
          f"{set.difference(full_pool_set, dylan_achievements)}")


if __name__ == "__main__":
    main()
