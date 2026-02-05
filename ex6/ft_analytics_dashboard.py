class Player:
    def __init__(self, name: str, score: int, achievement: set,
                 active: bool, regions: list[str]):
        self.name = name
        self.score = score
        self.active = active
        self.achievement = achievement
        self.regions = regions

    def factory(template: list[tuple]):
        players = []
        for name, score, achievement, active, regions in template:
            players.append(Player(name, score, achievement, active, regions))
        return players


def list_comprehension(players: list[Player]):
    print(f"High scores (>2000): {[player.name for player in players
                                   if player.score > 2000]}")
    print(f"Scores doubled: {[player.score * 2 for player in players]}")
    print(f"Active players: {[player.name for player in players
                              if player.active]}")


def dict_comprehension(players: list[Player]):
    p_score = {player.name: player.score for player in players
               if player.active}
    scores = {'high': len([player.name for player in players
                           if player.score > 2000]),
              'medium': len([player.name for player in players
                             if player.score < 2000
                             and player.score > 1000]),
              'low': len([player.name for player in players
                          if player.score <= 1000])}
    achievements = {player.name: len(player.achievement)
                    for player in players if player.active}
    print("Player scores:", p_score)
    print("Score categories:", scores)
    print("Achievement counts:", achievements)


def set_comprehension(players: list[Player]):
    list_players = set(player.name for player in players)
    achievements = [player.achievement for player in players]
    regions = set(region for player in players
                  for region in player.regions)
    i = 0
    unique_achievements = set()
    while i < len(achievements) - 1:
        unique_achievements = unique_achievements.union(
            achievements[0] - achievements[len(achievements) - 1])
        unique_achievements = unique_achievements.union(
            achievements[i] - achievements[0])
        unique_achievements = unique_achievements.union(
            achievements[i] - achievements[len(achievements) - 1])
        i += 1
    print("Unique players:", list_players)
    print("Unique achievements:", unique_achievements)
    print("Active regions:", regions)


def combined(players: list[Player]):
    total_players = len(players)
    total_unique_achievements = set(acvmt for player in players
                                    for acvmt in player.achievement)
    average = sum(player.score for player in players) / len(players)
    top_performer = max(players, key=lambda player: player.score)
    print("Total players:", total_players)
    print("Total unique achievements:", len(total_unique_achievements))
    print("Average score:", average)
    print(f"Top performer: {top_performer.name} \
({top_performer.score} points, \
{len(top_performer.achievement)} achievements)")


if __name__ == "__main__":
    players_template = [('alice', 2300, {'level_10',
                         'treasure_hunter', 'speed_demon', 'perfectionist',
                        'collector'},
                         True, ["north", "east"]),
                        ('bob', 1800, {'speed_demon', 'boss_slayer',
                         'collector'}, True, ["central"]),
                        ('charlie', 2150, {'collector', 'treasure_hunter',
                         'perfectionist', 'speed_demon', 'first_kill'},
                         True, ["central", "east"]),
                        ('diana', 2050, {'collector', 'treasure_hunter',
                         'perfectionist', 'speed_demon'}, False, ["north"])]
    players = Player.factory(players_template)
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    list_comprehension(players)
    print("\n=== Dict Comprehension Examples ===")
    dict_comprehension(players)
    print("\n=== Set Comprehension Examples ===")
    set_comprehension(players)
    print("\n=== Combined Analysis ===")
    combined(players)
