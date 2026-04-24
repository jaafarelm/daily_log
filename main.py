from morning import MorningRunner
from midday import MiddayRunner
from night import NightRunner


class MainApp:
    def __init__(self):
        self.morning_runner = MorningRunner()
        self.midday_runner = MiddayRunner()
        self.night_runner = NightRunner()

    def menu(self):
        print("\n=== DAILY LOG APP ===")
        print("1. Morning check")
        print("2. Midday check")
        print("3. Night check")
        print("4. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.morning_runner.create_daily_log()
                self.morning_runner.new_row()

            elif choice == "2":
                self.midday_runner.midday_row()

            elif choice == "3":
                self.night_runner.night_row()

            elif choice == "4":
                print("Exiting app.")
                break

            else:
                print("Invalid choice. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    app = MainApp()
    app.run()