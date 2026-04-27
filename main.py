from morning import MorningRunner
from midday import MiddayRunner
from night import NightRunner
from LLM import LogAdvisor
from utils import Utils

class MainApp:
    def __init__(self):
        self.morning_runner = MorningRunner()
        self.midday_runner = MiddayRunner()
        self.night_runner = NightRunner()
        self.log_advisor = LogAdvisor()
        self.utils = Utils()

    def menu(self):
        print("\n=== DAILY LOG APP ===")
        print("1. Morning check")
        print("2. Midday check")
        print("3. Night check")
        print("4. Get advice")
        print("5. Free advice")
        print("6. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.utils.create_daily_log()
                self.morning_runner.new_row()

            elif choice == "2":
                self.midday_runner.midday_row()

            elif choice == "3":
                self.night_runner.night_row()

            elif choice == "4":
                day_time = input("Which advice do you want? (morning / midday / night): ").strip().lower()
                advice = self.log_advisor.get_advice(day_time)
                print("\n=== ADVICE ===")
                print(advice)

            elif choice == "5":
                question = input("What is your question?\n").strip()
                print("\n=== FREE ADVICE ===")
                print(self.log_advisor.free_question(question))

            elif choice == "6":
                print("Exiting app.")
                break

            else:
                print("Invalid choice. Please choose 1, 2, 3, 4, 5, or 6.")


if __name__ == "__main__":
    app = MainApp()
    app.run()