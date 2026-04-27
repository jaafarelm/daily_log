from daily_log import Identity, Shift, Sleep, Morning as MorningData, DailyLog, CSV_FILE, CSV_HEADERS
import os
import pandas as pd
from time import localtime, strftime
from datetime import datetime, timedelta
from utils import current_date, current_time, check_file_exists, get_non_empty_input, get_choice_input, get_float_input, get_time_input, calculate_hours

class MorningRunner:
    def __init__(self):
        pass

    def check_row_exists(self, date_value):
        if not check_file_exists():
            return False

        df = pd.read_csv(CSV_FILE)
        return any(str(row).strip() == date_value for row in df["date"])

    def new_row(self):
        print("Would you please answer the following questions:\n")

        today_date = current_date()

        if self.check_row_exists(today_date):
            print(f"A row for {today_date} already exists.")
            return None

        id1 = Identity(
            date=today_date,
            day_type=get_choice_input("enter the day type of today (shift / non_shift): \n:", ["shift", "non_shift"])
        )

        if id1.day_type == "shift":
            shift_start = get_time_input("enter the start of the shift of today (HH:MM): \n:")
            shift_end = get_time_input("enter the end of the shift of today (HH:MM): \n:")
            shift1 = Shift(
                start=shift_start,
                end=shift_end,
                hours=calculate_hours(shift_start, shift_end)
            )
        else:
            shift1 = Shift(
                start=None,
                end=None,
                hours=None
            )

        sleep_start = get_time_input("enter the start of your sleep (HH:MM): \n:")
        wake_time = get_time_input("enter the end / wake time of your sleep (HH:MM): \n:")
        sleep1 = Sleep(
            start=sleep_start,
            end=wake_time,
            hours=calculate_hours(sleep_start, wake_time)
        )

        morning1 = MorningData(
            time_stamp=current_time(),
            front_a_task=get_non_empty_input("enter front A task: \n:"),
            front_b_task=get_non_empty_input("enter front B task: \n:"),
            front_c_task=get_non_empty_input("enter front C task: \n:"),
            planned_hours_total=get_float_input("enter planned hours total: \n:"),
            main_activity=get_non_empty_input("enter the main activity of today: \n:"),
            minimum_day_target=get_non_empty_input("enter the minimum day target: \n:"),
            weekly_objective_reference=input("enter weekly objective reference (optional): \n:").strip() or None
        )

        daily1 = DailyLog(
            identity=id1,
            shift=shift1,
            sleep=sleep1,
            morning=morning1
        )

        row_data = {
            "date": daily1.identity.date,
            "day_type": daily1.identity.day_type,
            "shift_start_time": daily1.shift.start,
            "shift_end_time": daily1.shift.end,
            "shift_hours": daily1.shift.hours,
            "sleep_start_time": daily1.sleep.start,
            "wake_time": daily1.sleep.end,
            "sleep_hours": daily1.sleep.hours,
            "morning_time_stamp": daily1.morning.time_stamp,
            "front_a_task": daily1.morning.front_a_task,
            "front_b_task": daily1.morning.front_b_task,
            "front_c_task": daily1.morning.front_c_task,
            "planned_hours_total": daily1.morning.planned_hours_total,
            "planned_main_activity": daily1.morning.main_activity,
            "minimum_day_target": daily1.morning.minimum_day_target,
            "weekly_objective_reference": daily1.morning.weekly_objective_reference,
            "midday_time_stamp": None,
            "midday_current_activity": None,
            "midday_hours_done": None,
            "midday_on_track": None,
            "midday_adjustment": None,
            "night_time_stamp": None,
            "actual_hours_total": None,
            "actual_main_activity": None,
            "front_a_done": None,
            "front_b_done": None,
            "front_c_done": None,
            "target_completed": None,
            "failure_reason": None,
            "main_output_of_day": None,
            "tomorrow_first_task": None,
            "note": None,
        }

        df = pd.DataFrame([row_data])
        df.to_csv(
            CSV_FILE,
            mode="a",
            header=not os.path.exists(CSV_FILE),
            index=False
        )

        return daily1