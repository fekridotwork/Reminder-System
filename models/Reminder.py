from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Reminder(ABC):
    title: str
    time: str
    rem_id: int

    @abstractmethod
    def remind(self) -> None:
        #Polymorphic implementation
        raise NotImplementedError

    @abstractmethod
    def to_dict(self) -> dict:
        pass