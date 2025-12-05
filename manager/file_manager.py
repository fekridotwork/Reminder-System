import json
import logging

from models.SimpleReminder import SimpleReminder
from models.MeetingReminder import MeetingReminder
from models.DailyRoutineReminder import DailyRoutineReminder


def from_dict(obj):
    rem_type = obj["type"]

    if rem_type == "simple":
        return SimpleReminder(obj["title"], obj["time"], obj["rem_id"])

    elif rem_type == "meeting":
        return MeetingReminder(obj["title"], obj["time"], obj["rem_id"], obj["participants"])

    elif rem_type == "daily":
        return DailyRoutineReminder(obj["title"], obj["time"], obj["rem_id"], obj["daily_repeat"])

    else:
        logging.error("Unknown reminder type in JSON")
        raise ValueError("Unknown reminder type in JSON")



def to_dict(reminder):
    return reminder.to_dict()


def load_data(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [from_dict(item) for item in data]
    except Exception:
        return []


def save_data(path, reminders):
    with open(path, "w", encoding="utf-8") as f:
        json.dump([to_dict(r) for r in reminders], f, indent=4)
