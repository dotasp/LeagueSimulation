class Team:
    def __init__(self, name, strength, bad_matchups=None):
        self.name = name
        self.strength = strength  # Kekuatan tim (0-100)
        self.bad_matchups = bad_matchups if bad_matchups is not None else []
    
    def __repr__(self):
        return f"Team({self.name}, Strength: {self.strength}, Bad Matchups: {self.bad_matchups})"
