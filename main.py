from models.team import Team
from models.simulator_manager import SimulatorManager

def main():
    # Membuat tim
    team1 = Team(name="Tim A", strength=75, bad_matchups=["Tim C"])
    team2 = Team(name="Tim B", strength=70, bad_matchups=["Tim A"])
    team3 = Team(name="Tim C", strength=65, bad_matchups=["Tim B"])
    team4 = Team(name="Tim D", strength=100, bad_matchups=["Tim A"])

    # Daftar semua tim
    teams = [team1, team2, team3, team4]

    # Jumlah simulasi yang akan dijalankan
    num_simulations = 100000

    # Inisialisasi dan menjalankan Simulator Manager
    simulator_manager = SimulatorManager(teams, num_simulations)
    simulator_manager.run()

if __name__ == "__main__":
    main()