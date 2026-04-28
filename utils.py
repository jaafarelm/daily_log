import os
import pandas as pd
from time import localtime, strftime
from datetime import datetime, timedelta

from daily_log import CSV_FILE, CSV_HEADERS


def current_date():
    return strftime("%d/%m/%Y", localtime())


def current_time():
    return strftime("%H:%M", localtime())


def check_file_exists():
    return os.path.exists(CSV_FILE)


def create_daily_log():
    if not check_file_exists():
        df = pd.DataFrame(columns=CSV_HEADERS)
        df.to_csv(CSV_FILE, index=False)


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_choice_input(prompt, allowed_values):
    while True:
        value = input(prompt).strip().lower()
        if value in allowed_values:
            return value
        print(f"Invalid input. Allowed values: {', '.join(allowed_values)}")


def get_float_input(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number, for example 6 or 6.5")


def get_time_input(prompt):
    while True:
        value = input(prompt).strip()
        try:
            datetime.strptime(value, "%H:%M")
            return value
        except ValueError:
            print("Use time format HH:MM")


def calculate_hours(start_time, end_time):
    if start_time is None or end_time is None:
        return None

    start_dt = datetime.strptime(start_time, "%H:%M")
    end_dt = datetime.strptime(end_time, "%H:%M")

    if end_dt < start_dt:
        end_dt += timedelta(days=1)

    diff = end_dt - start_dt
    return round(diff.total_seconds() / 3600, 2)

def view_tasks():
    df = pd.read_csv("daily_log.csv")
    if df.empty:
        print("No daily log rows found.")
        return

    row = df.iloc[-1]

    print("\n=== TODAY'S TASKS ===")
    print(f"Date: {row['date']}")
    print(f"Front A: {row['front_a_task']}")
    print(f"Front B: {row['front_b_task']}")
    print(f"Front C: {row['front_c_task']}")
    print(f"Main activity: {row['planned_main_activity']}")
    print(f"Minimum target: {row['minimum_day_target']}")
    print(f"Planned hours: {row['planned_hours_total']}")