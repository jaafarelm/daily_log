from daily_log import Night, CSV_FILE
import pandas as pd
import os
from time import localtime, strftime
from utils import current_date, current_time, check_file_exists, get_non_empty_input, get_choice_input, get_float_input


class NightRunner:
    def __init__(self):
        pass

    def check_row_exists(self):
        date = current_date()
        flag = 0
        row_index = None

        if check_file_exists():
            df = pd.read_csv(CSV_FILE)

            for idx, row in enumerate(df["date"]):
                if str(row).strip() == date:
                    flag = 1
                    row_index = idx
                    break

        return flag, date, row_index


    def night_row(self):
        print("Would you please answer the following questions:\n")

        if not check_file_exists():
            print("daily_log.csv file not found")
            return None

        flag, date, row_index = self.check_row_exists()

        if flag == 0:
            print(f"No row found for date {date}")
            return None

        target_completed_value = get_choice_input("Was the target completed? (yes / no): \n", ["yes", "no"])

        failure_reason_value = None
        if target_completed_value == "no":
            failure_reason_value = get_non_empty_input("What is the failure reason?: \n")

        night1 = Night(
            time_stamp=current_time(),
            actual_hours_total=get_float_input("Enter actual hours total of today: \n"),
            actual_main_activity=get_non_empty_input("Enter the actual main activity of today: \n"),
            front_a_done=get_choice_input("Was Front A done? (yes / no): \n", ["yes", "no"]),
            front_b_done=get_choice_input("Was Front B done? (yes / no): \n", ["yes", "no"]),
            front_c_done=get_choice_input("Was Front C done? (yes / no): \n", ["yes", "no"]),
            target_completed=target_completed_value,
            failure_reason=failure_reason_value,
            main_output_of_day=get_non_empty_input("What was the main output of the day?: \n"),
            tomorrow_first_task=get_non_empty_input("What is tomorrow's first task?: \n"),
            note=input("Any note for today? (optional): \n").strip() or None,
        )

        df = pd.read_csv(CSV_FILE)

        df.loc[row_index, "night_time_stamp"] = night1.time_stamp
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

        df.to_csv(CSV_FILE, index=False)

        return night1