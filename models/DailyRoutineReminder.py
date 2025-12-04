from dataclasses import dataclass
from models.Reminder import Reminder


@dataclass
class DailyRoutineReminder(Reminder):
    daily_repeat : bool = True

    #overriding abstractmethod
    def remind(self) -> None:
        print(f"Daily Routine Reminder : {self.title}")

    # overriding abstractmethod
    def to_dict(self):
        return {
            "type": "daily",
            "title": self.title,
            "time": self.time,
            "rem_id": self.rem_id,
            "daily_repeat": self.daily_repeat
        }