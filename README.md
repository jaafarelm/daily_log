# Daily Log CLI App

A Python command-line app for planning, tracking, and reviewing a day through three stages:

- **Morning** → define the day
- **Midday** → update progress
- **Night** → record the final outcome

The app stores everything in a single CSV file and updates the same row for the same date throughout the day.

## Why I Built It

I built this project for three reasons:

1. To create a personal operating system for my daily execution
2. To rebuild my Python and software-engineering fluency through a real project
3. To create a base system that can later grow into analytics, LLM-assisted reflection, and smarter decision support

This is not just a logging app. It is the beginning of a structured execution system.

## Current Features

- Morning check:
  - creates a new row for the day
  - records day type, shift/sleep details, and Front A / B / C tasks
- Midday check:
  - updates the existing row for the same date
  - records current activity, hours done, on-track status, and adjustment
- Night check:
  - updates the existing row for the same date
  - records final output, completion status, and next task
- CSV-based persistence
- Input validation for key fields
- Shift / non-shift branching
- One-row-per-day lifecycle

## Project Structure

```text
daily_log.py   # data classes / domain models
morning.py     # morning workflow
midday.py      # midday update workflow
night.py       # night close workflow
main.py        # main entry point
daily_log.csv  # generated log file