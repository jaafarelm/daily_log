from daily_log import Midday, CSV_FILE
import pandas as pd
import os
from time import localtime, strftime
from utils import current_date, current_time, check_file_exists, get_non_empty_input, get_choice_input, get_float_input


class MiddayRunner:
    def __init__(self):
        pass

    def current_date(self):
        return strftime("%d/%m/%Y", localtime())

    def current_time(self):
        return strftime("%H:%M", localtime())

    def check_file_exists(self):
        return os.path.exists(CSV_FILE)

    def check_row_exists(self):
        date = self.current_date()
        flag = 0
        row_index = None

        if self.check_file_exists():
            df = pd.read_csv(CSV_FILE)

            for idx, row in enumerate(df["date"]):
                if str(row).strip() == date:
                    flag = 1
                    row_index = idx
                    break

        return flag, date, row_index

    def midday_row(self):
        print("Would you please answer the following questions:\n")

        if not self.check_file_exists():
            print("daily_log.csv file not found")
            return None

        flag, date, row_index = self.check_row_exists()

        if flag == 0:
            print(f"No row found for date {date}")
            return None

        midday1 = Midday(
            time_stamp=self.current_time(),
            current_activity=get_non_empty_input("Would you please enter the current activity: \n"),
            hours_done=get_float_input("How many hours have been done so far?: \n"),
            on_track=get_choice_input("Are we on track? (yes / no): \n", ["yes", "no"]),
            adjustment=input("Any adjustment for today?: \n").strip() or None,
        )

        df = pd.read_csv(CSV_FILE)

        df.loc[row_index, "midday_time_stamp"] = midday1.time_stamp
        df.loc[row_index, "midday_current_activity"] = midday1.current_activity
        df.loc[row_index, "midday_hours_done"] = midday1.hours_done
        df.loc[row_index, "midday_on_track"] = midday1.on_track
        df.loc[row_index, "midday_adjustment"] = midday1.adjustment

        df.to_csv(CSV_FILE, index=False)

        return midday1