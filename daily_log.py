from dataclasses import dataclass
from typing import Optional


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