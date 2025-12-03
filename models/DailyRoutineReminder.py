from dataclasses import dataclass
from models.Reminder import Reminder


@dataclass
class DailyRoutineReminder(Reminder):
    daily_repeat : bool = True

    #overriding abstractmethod
    def remind(self) -> None:
        print(f"Daily Routine Reminder : {self.title}")