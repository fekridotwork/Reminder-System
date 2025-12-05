from dataclasses import dataclass, field
from models.Reminder import Reminder


@dataclass
class MeetingReminder(Reminder):
    participants: list = field(default_factory=list)

    # overriding abstractmethod
    def remind(self) -> None:
        print(f"\nMeeting Reminder: {self.title}")
        print("\nParticipants:")
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