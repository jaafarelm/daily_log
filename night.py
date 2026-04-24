from daily_log import Night
import pandas as pd
import os

class NightRunner:
    def __init__(self):
        pass

    def check_file_exists(self):
        if os.path.exists("daily_log.csv"):
            return 1
        return 0

    def check_row_exists(self):
        date = input("Would you please enter the date of today(dd/mm/yyyy): ").strip()
        flag = 0
        row_index = None

        if self.check_file_exists() == 1:
            df = pd.read_csv("daily_log.csv")

            for idx, row in enumerate(df["date"]):
                if str(row).strip() == date:
                    flag = 1
                    row_index = idx
                    break

        return flag, date, row_index

    def night_row(self):
        print("Would you please answer the following questions:\n")

        if self.check_file_exists() == 0:
            print("daily_log.csv file not found")
            return None

        flag, date, row_index = self.check_row_exists()

        if flag == 0:
            print(f"No row found for date {date}")
            return None

        target_completed_value = input("Was the target completed? (yes / no): \n").strip()

        failure_reason_value = None
        if target_completed_value.lower() == "no":
            failure_reason_value = input("What is the failure reason?: \n").strip()

        night1 = Night(
            time_stamp=input("The exact time we are filling this data(HH:MM): \n").strip(),
            actual_hours_total=float(input("Enter actual hours total of today: \n").strip()),
            actual_main_activity=input("Enter the actual main activity of today: \n").strip(),
            front_a_done=input("Was Front A done? (yes / no): \n").strip(),
            front_b_done=input("Was Front B done? (yes / no): \n").strip(),
            front_c_done=input("Was Front C done? (yes / no): \n").strip(),
            target_completed=target_completed_value,
            failure_reason=failure_reason_value,
            main_output_of_day=input("What was the main output of the day?: \n").strip(),
            tomorrow_first_task=input("What is tomorrow's first task?: \n").strip(),
            note=input("Any note for today? (optional): \n").strip() or None,
        )

        df = pd.read_csv("daily_log.csv")

        df.loc[row_index, "actual_hours_total"] = night1.actual_hours_total
        df.loc[row_index, "actual_main_activity"] = night1.actual_main_activity
        df.loc[row_index, "front_a_done"] = night1.front_a_done
        df.loc[row_index, "front_b_done"] = night1.front_b_done
        df.loc[row_index, "front_c_done"] = night1.front_c_done
        df.loc[row_index, "target_completed"] = night1.target_completed
        df.loc[row_index, "failure_reason"] = night1.failure_reason
        df.loc[row_index, "main_output_of_day"] = night1.main_output_of_day
        df.loc[row_index, "tomorrow_first_task"] = night1.tomorrow_first_task
        df.loc[row_index, "note"] = night1.note

        df.to_csv("daily_log.csv", index=False)

        return night1