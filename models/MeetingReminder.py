from dataclasses import dataclass
from models.Reminder import Reminder


@dataclass
class MeetingReminder(Reminder):
    participants: list

    # overriding abstractmethod
    def remind(self) -> None:
        print(f"Meeting Reminder: {self.title}")
        print("Participants:")
        for p in self.participants:
            print(f"  - {p}")

    # overriding abstractmethod
    def to_dict(self):
        return {
            "type": "meeting",
            "title": self.title,
            "time": self.time,
            "rem_id": self.rem_id,
            "participants": self.participants
        }