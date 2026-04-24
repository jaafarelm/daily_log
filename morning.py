from daily_log import Identity, Shift, Sleep, Morning as MorningData, DailyLog
import os
import pandas as pd


class MorningRunner:
    def __init__(self):
        pass

    def check_file_exists(self):
        if os.path.exists("daily_log.csv"):
            return 1
        return 0

    def create_daily_log(self):
        headers = [
            "date",
            "day_type",
            "shift_start_time",
            "shift_end_time",
            "shift_hours",
            "sleep_start_time",
            "wake_time",
            "sleep_hours",
            "front_a_task",
            "front_b_task",
            "front_c_task",
            "planned_hours_total",
            "planned_main_activity",
            "minimum_day_target",
            "weekly_objective_reference",
            "midday_current_activity",
            "midday_hours_done",
            "midday_on_track",
            "midday_adjustment",
            "actual_hours_total",
            "actual_main_activity",
            "time_stamp",
            "front_a_done",
            "front_b_done",
            "front_c_done",
            "target_completed",
            "failure_reason",
            "main_output_of_day",
            "tomorrow_first_task",
            "note",
        ]

        if not self.check_file_exists():
            df = pd.DataFrame(columns=headers)
            df.to_csv("daily_log.csv", index=False)

    def new_row(self):
        print("Would you please answer the following questions:\n")

        id1 = Identity(
            date=input("enter the date of today (dd/mm/yyyy): \n:").strip(),
            day_type=input("enter the day type of today (shift / non_shift): \n:").strip()
        )

        if id1.day_type == "shift":
            shift1 = Shift(
                start=input("enter the start of the shift of today: \n:").strip(),
                end=input("enter the end of the shift of today: \n:").strip()
            )
        elif (id1.day_type == "non_shift"):
            shift1 = Shift(
                start = None,
                end = None
            )
        else:
            print("Invalid day type.")
            return None

        sleep1 = Sleep(
            start=input("enter the start of your sleep: \n:").strip(),
            end=input("enter the end / wake time of your sleep: \n:").strip()
        )

        morning1 = MorningData(
            time_stamp=input("enter time_stamp(HH:MM) \n:").strip(),
            front_a_task=input("enter front A task: \n:").strip(),
            front_b_task=input("enter front B task: \n:").strip(),
            front_c_task=input("enter front C task: \n:").strip(),
            planned_hours_total=float(input("enter planned hours total: \n:").strip()),
            main_activity=input("enter the main activity of today: \n:").strip(),
            minimum_day_target=input("enter the minimum day target: \n:").strip(),
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
            "front_a_task": daily1.morning.front_a_task,
            "front_b_task": daily1.morning.front_b_task,
            "front_c_task": daily1.morning.front_c_task,
            "planned_hours_total": daily1.morning.planned_hours_total,
            "planned_main_activity": daily1.morning.main_activity,
            "minimum_day_target": daily1.morning.minimum_day_target,
            "weekly_objective_reference": daily1.morning.weekly_objective_reference,
            "midday_current_activity": None,
            "midday_hours_done": None,
            "midday_on_track": None,
            "midday_adjustment": None,
            "actual_hours_total": None,
            "actual_main_activity": None,
            "time_stamp": None,
            "front_a_done": None,
            "front_b_done": None,
            "front_c_done": None,
            "target_completed": None,
            "failure_reason": None,
            "main_output_of_day": None,
            "tomorrow_first_task": None,
            "note": None
        }

        df = pd.DataFrame([row_data])
        df.to_csv(
            "daily_log.csv",
            mode="a",
            header=not os.path.exists("daily_log.csv"),
            index=False
        )

        return daily1

    def run(self):
        self.create_daily_log()
        return self.new_row()


if __name__ == "__main__":
    app = MorningRunner()
    app.run()