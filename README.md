# Daily Log CLI App

A Python command-line application for structured daily execution tracking, built around three daily checkpoints:

- Morning check: plan the day
- Midday check: review and adjust the day
- Night check: close the day and record the outcome

The app also includes an LLM advisory layer that reads the user's logged data and provides short, practical advice based on the current context.

## Purpose

This project was built to solve a real execution problem: maintaining discipline, clarity, and progress while balancing work, study, job applications, side projects, and personal constraints.

The goal is not simply to create a diary. The goal is to create a structured execution system that captures reality, tracks progress, and uses LLM-based reflection to support better decisions.

## Current Features

- Morning planning workflow
- Midday progress update workflow
- Night review workflow
- One-row-per-day structure in `daily_log.csv`
- Same-day updates for midday and night entries
- Automatic date and timestamp handling
- Input validation for key fields
- Shift and non-shift day support
- Sleep and shift duration calculation
- OpenAI-powered advice mode
- Free-question LLM advice mode
- Separate `analysis_log.csv` for storing AI-generated reflections
- Shared utility functions for repeated logic

## Project Structure

```text
daily_log.py      # Data models, CSV constants, and schema definitions
main.py           # Main CLI entry point and menu routing
morning.py        # Morning planning workflow
midday.py         # Midday progress update workflow
night.py          # Night review workflow
LLM.py            # LLM advisory layer
utils.py          # Shared helper functions
requirements.txt  # Project dependencies