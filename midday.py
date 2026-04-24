from daily_log import Midday
import pandas as pd
import os


class MiddayRunner:
    def __init__(self):
        pass

    def check_file_exists(self):
        if os.path.exists("daily_log.csv"):
            return 1
        return 0

    def check_row_exist(self):
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

    def midday_row(self):
        print("Would you please answer the following questions:\n")

        if self.check_file_exists() == 0:
            print("daily_log.csv file not found")
            return None

        flag, date, row_index = self.check_row_exist()

        if flag == 0:
            print(f"No row found for date {date}")
            return None

        midday1 = Midday(
            time_stamp=input("The exact time we are filling this data(HH:MM): \n").strip(),
            current_activity=input("Would you please enter the current activity: \n").strip(),
            hours_done=float(input("How many hours have been done so far?: \n").strip()),
            on_track=input("Are we on track: \n").strip(),
            adjustment=input("Any adjustment for today?: \n").strip() or None,
        )

        df = pd.read_csv("daily_log.csv")

        df.loc[row_index, "time_stamp"] = midday1.time_stamp
        df.loc[row_index, "midday_current_activity"] = midday1.current_activity
        df.loc[row_index, "midday_hours_done"] = midday1.hours_done
        df.loc[row_index, "midday_on_track"] = midday1.on_track
        df.loc[row_index, "midday_adjustment"] = midday1.adjustment

        df.to_csv("daily_log.csv", index=False)

        return midday1