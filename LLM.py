from openai import OpenAI
client = OpenAI()

import pandas as pd
import json
import os
from time import localtime, strftime


class LogAdvisor:
    def __init__(self):
        pass

    def load_csv_content(self):
        df = pd.read_csv("daily_log.csv")
        if len(df) <= 7:
            return df.to_dict(orient="records")
        else:
            return df.tail(7).to_dict(orient="records")

    def load_analysis_content(self):
        if os.path.exists("analysis_log.csv"):
            df = pd.read_csv("analysis_log.csv")
            if len(df) <= 7:
                return df.to_dict(orient="records")
            else:
                return df.tail(7).to_dict(orient="records")
        else:
            headers = [
                "date",
                "mode",
                "created_at",
                "question"
                "raw_response"
            ]
            df = pd.DataFrame(columns=headers)
            return df.to_dict(orient="records")

    def creating_response(self, content):
        response = client.responses.create(
            model="gpt-5.5",
            input=content
        )
        return response.output_text

    def prepare_context(self):
        data = self.load_csv_content()
        analysis = self.load_analysis_content()

        if not analysis:
            report = "there is no report recorded from the past, therefore you can give your own opinion instead of relying on actual data for now"
        else:
            report = analysis

        data_text = json.dumps(data, indent=2)
        report_text = json.dumps(report, indent=2)
        return data_text, report_text

    def get_advice(self, day_time):

        data_text, report_text = self.prepare_context()

        if day_time == "morning":
            content = (
                "You are advising a user on how to run today well.\n"
                "Read the data carefully and answer briefly and practically.\n"
                "Return only 3 bullet points:\n"
                "1. short reading of the situation\n"
                "2. best first move for today\n"
                "3. one warning to avoid\n\n"
                f"Log data:\n{data_text}\n\n"
                f"Latest report:\n{report_text}"
            )

        elif day_time == "midday":
            content = (
                "You are advising a user in the middle of the day.\n"
                "Read the data carefully and answer briefly and practically.\n"
                "Return only 3 bullet points:\n"
                "1. what is likely going wrong\n"
                "2. the smallest correction to make now\n"
                "3. what should be prioritized for the rest of the day\n\n"
                f"Log data:\n{data_text}\n\n"
                f"Latest report:\n{report_text}"
            )

        elif day_time == "night":
            content = (
                "You are analyzing the user's day at night.\n"
                "Read the data carefully and answer briefly and practically.\n"
                "Return only 4 bullet points:\n"
                "1. what went right\n"
                "2. what went wrong\n"
                "3. the most likely reason\n"
                "4. the first task for tomorrow\n\n"
                f"Log data:\n{data_text}\n\n"
                f"Latest report:\n{report_text}"
            )

        else:
            raise ValueError("day_time must be 'morning', 'midday', or 'night'")

        response_text = self.creating_response(content)
        self.save_analysis(day_time, response_text)
        return response_text

    def save_analysis(self, day_time, response_text, question):
        df_name = "analysis_log.csv"
        row = {
            "date": strftime("%d/%m/%Y", localtime()),
            "mode": day_time,
            "created_at": strftime("%H:%M", localtime()),
            "question": question,
            "raw_response": response_text
        }

        if os.path.exists(df_name):
            df = pd.read_csv(df_name)
            new_row = pd.DataFrame([row])
            df = pd.concat([df, new_row], ignore_index=True)
        else:
            df = pd.DataFrame([row])

        df.to_csv(df_name, index=False)

    def free_question(self, question):
        data_text, report_text = self.prepare_context()

        content = (
            "You are a strict execution advisor.\n"
            "Read the user's daily log data and previous analysis.\n"
            "Answer the user's question with only practical advice.\n"
            "Return exactly 3 bullet points:\n"
            "1. direct answer\n"
            "2. best next action\n"
            "3. main warning\n\n"
            f"User question:\n{question}\n\n"
            f"Daily log data:\n{data_text}\n\n"
            f"Previous analysis:\n{report_text}"
        )

        response_text = self.creating_response(content)
        self.save_analysis("free_advice", response_text, question)
        return response_text