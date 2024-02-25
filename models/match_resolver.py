import numpy as np

class MatchResolver:
    @staticmethod
    def resolve(teams):
        """
        Menghitung probabilitas kemenangan untuk setiap tim dalam array tim.
        
        :param teams: Array dari objek Team.
        :return: Array dari probabilitas kemenangan untuk setiap tim.
        """
        probabilities = []
        for i in range(len(teams)):
            for j in range(i + 1, len(teams)):
                team1 = teams[i]
                team2 = teams[j]
                base_probability = team1.strength / (team1.strength + team2.strength) + 0.05  # Home advantage
                if team2.name in team1.bad_matchups:
                    base_probability -= 0.1
                probabilities.append(base_probability)
        return np.array(probabilities)