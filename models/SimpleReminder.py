from dataclasses import dataclass
from models.Reminder import Reminder


@dataclass
class SimpleReminder(Reminder):

    #overriding abstract method
    def remind(self) -> None:
        print(f"It's time to : {self.title}")

    #overriding abstract method
    def to_dict(self):
        return {
            "type": "simple",
            "title": self.title,
            "time": self.time,
            "rem_id": self.rem_id
        }
