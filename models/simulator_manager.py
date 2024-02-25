from .league import League
from .team import Team

class SimulatorManager:
    def __init__(self, teams, num_simulations):
        """
        Inisialisasi Simulator Manager dengan tim dan jumlah simulasi.
        
        :param teams: Daftar objek Team yang berpartisipasi dalam liga.
        :param num_simulations: Jumlah simulasi yang akan dijalankan.
        """
        self.teams = teams
        self.num_simulations = num_simulations
        self.simulation_results = []

    def run_simulation(self):
        """
        Menjalankan simulasi liga untuk jumlah yang ditentukan dan mengumpulkan hasil.
        """
        for _ in range(self.num_simulations):
            league = League(self.teams)
            league.play_season()
            standings = league.get_standings()
            self.simulation_results.append(standings)

    def analyze_results(self):
        """
        Menganalisis dan mencetak hasil simulasi, seperti frekuensi kemenangan atau distribusi peringkat.
        """
        # Contoh sederhana: hitung dan cetak frekuensi kemenangan untuk setiap tim
        win_counts = {team.name: 0 for team in self.teams}
        for result in self.simulation_results:
            winner = result[0][0]  # Tim dengan skor tertinggi dalam simulasi
            win_counts[winner.name] += 1

        # Cetak frekuensi kemenangan
        print("Frekuensi Kemenangan Tim:")
        for team, wins in win_counts.items():
            print(f"{team}: {wins}/{self.num_simulations} simulasi")

    def run(self):
        """
        Menjalankan seluruh proses simulasi dan analisis.
        """
        self.run_simulation()
        self.analyze_results()