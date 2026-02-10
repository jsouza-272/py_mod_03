def achievement_analytics(*players: set):
    print("=== Achievement Analytics ===\n")
    achievement = set.union(*players)
    print(f"All unique achievements: {achievement}")
    print(f"Total unique achievements: {len(achievement)}")
    print(f"\nCommon to all players: {set.intersection(*players)}")
    d1 = players[0].difference(players[1], players[2])
    d2 = players[1].difference(players[0], players[2])
    d3 = players[2].difference(players[0], players[1])
    print(f"Rare achievements (1 player): {set.union(d1, d2, d3)}\n")
    print(f"Alice vs Bob common: {set.intersection(players[0], players[1])}")
    print(f"Alice unique: {players[0].difference(players[1])}")
    print(f"Bob unique: {players[1].difference(players[0])}")


if __name__ == "__main__":
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}
    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")
    achievement_analytics(alice, bob, charlie)
