from dataclasses import dataclass
from typing import Optional


CSV_FILE = "daily_log.csv"

CSV_HEADERS = [
    "date",
    "day_type",
    "shift_start_time",
    "shift_end_time",
    "shift_hours",
    "sleep_start_time",
    "wake_time",
    "sleep_hours",
    "morning_time_stamp",
    "front_a_task",
    "front_b_task",
    "front_c_task",
    "planned_hours_total",
    "planned_main_activity",
    "minimum_day_target",
    "weekly_objective_reference",
    "midday_time_stamp",
    "midday_current_activity",
    "midday_hours_done",
    "midday_on_track",
    "midday_adjustment",
    "night_time_stamp",
    "actual_hours_total",
    "actual_main_activity",
    "front_a_done",
    "front_b_done",
    "front_c_done",
    "target_completed",
    "failure_reason",
    "main_output_of_day",
    "tomorrow_first_task",
    "note",
]


@dataclass
class Identity:
    date: str
    day_type: str


@dataclass
class Shift:
    start: Optional[str] = None
    end: Optional[str] = None
    hours: Optional[float] = None


@dataclass
class Sleep:
    start: Optional[str] = None
    end: Optional[str] = None
    hours: Optional[float] = None


@dataclass
class Morning:
    time_stamp: str
    front_a_task: str
    front_b_task: str
    front_c_task: str
    planned_hours_total: float
    main_activity: str
    minimum_day_target: str
    weekly_objective_reference: Optional[str] = None


@dataclass
class Midday:
    time_stamp: Optional[str] = None
    current_activity: Optional[str] = None
    hours_done: Optional[float] = None
    on_track: Optional[str] = None
    adjustment: Optional[str] = None


@dataclass
class Night:
    time_stamp: Optional[str] = None
    actual_hours_total: Optional[float] = None
    actual_main_activity: Optional[str] = None
    front_a_done: Optional[str] = None
    front_b_done: Optional[str] = None
    front_c_done: Optional[str] = None
    target_completed: Optional[str] = None
    failure_reason: Optional[str] = None
    main_output_of_day: Optional[str] = None
    tomorrow_first_task: Optional[str] = None
    note: Optional[str] = None


@dataclass
class DailyLog:
    identity: Identity
    shift: Shift
    sleep: Sleep
    morning: Morning
    midday: Optional[Midday] = None
    night: Optional[Night] = None