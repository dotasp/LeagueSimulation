import random
from .team import Team
from .match_resolver import MatchResolver

class League:
    def __init__(self, teams):
        self.teams = teams
        self.standings = {team: 0 for team in teams}

    def play_match(self, team1, team2):
        probabilities = MatchResolver.resolve([team1, team2])
        outcome = random.random()
        
        # Asumsikan probabilitas pertama untuk team1
        if outcome < probabilities[0]:
            self.standings[team1] += 3  # Team1 menang
        elif outcome < probabilities[0] + 0.1:  # Range untuk draw
            self.standings[team1] += 1
            self.standings[team2] += 1
        else:
            self.standings[team2] += 3  # Team2 menang

    def calculate_standings(self):
        return sorted(self.standings.items(), key=lambda x: x[1], reverse=True)

    def play_season(self):
        for i in range(len(self.teams)):
            for j in range(i + 1, len(self.teams)):
                # Tim i sebagai home, Tim j sebagai away
                self.play_match(self.teams[i], self.teams[j])
                # Kemudian, Tim j sebagai home, Tim i sebagai away
                self.play_match(self.teams[j], self.teams[i])

    def get_standings(self):
        return self.calculate_standings()