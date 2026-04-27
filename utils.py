from time import localtime, strftime
from daily_log import Identity, Shift, Sleep, Morning as MorningData, DailyLog, CSV_FILE, CSV_HEADERS
import os
import pandas as pd
from time import localtime, strftime
from datetime import datetime, timedelta


class Utils:
    def __init__(self):
        pass

    def current_date(self):
        return strftime("%d/%m/%Y", localtime())

    def current_time(self):
        return strftime("%H:%M", localtime())

    def check_file_exists(self):
        return os.path.exists(CSV_FILE)
    
    def create_daily_log(self):
        if not self.check_file_exists():
            df = pd.DataFrame(columns=CSV_HEADERS)
            df.to_csv(CSV_FILE, index=False)
    
    def get_non_empty_input(self, prompt):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("This field cannot be empty.")

    
    def get_choice_input(self, prompt, allowed_values):
        while True:
            value = input(prompt).strip().lower()
            if value in allowed_values:
                return value
            print(f"Invalid input. Allowed values: {', '.join(allowed_values)}")

    

    def get_float_input(self, prompt):
        while True:
            value = input(prompt).strip()
            try:
                return float(value)
            except ValueError:
                print("Please enter a valid number, for example 6 or 6.5")

    
    def get_time_input(self, prompt):
        while True:
            value = input(prompt).strip()
            try:
                datetime.strptime(value, "%H:%M")
                return value
            except ValueError:
                print("Use time format HH:MM")
    


    def calculate_hours(self, start_time, end_time):
        if start_time is None or end_time is None:
            return None

        start_dt = datetime.strptime(start_time, "%H:%M")
        end_dt = datetime.strptime(end_time, "%H:%M")

        if end_dt < start_dt:
            end_dt += timedelta(days=1)

        diff = end_dt - start_dt
        return round(diff.total_seconds() / 3600, 2)