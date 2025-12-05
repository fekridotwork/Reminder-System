import logging
from logging.handlers import RotatingFileHandler
import threading
import time
from datetime import datetime
from models.DailyRoutineReminder import DailyRoutineReminder
from manager.file_manager import load_data, save_data


class ReminderManager:
    JSON_PATH = "data/reminders.json"
    LOG_PATH = "data/reminder.log"

    def __init__(self):
        self.reminders = load_data(self.JSON_PATH)
        self.scheduler_thread = None

        handler = RotatingFileHandler(
            self.LOG_PATH,
            maxBytes=100_000,  # 100 KB
            backupCount=3
        )

        logging.basicConfig(
            level=logging.INFO,
            handlers=[handler],
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

    def start_scheduler(self, interval_seconds: int = 5):

        if self.scheduler_thread is not None:
            return
        logging.info("Scheduler started.")

        def run():
            while True:
                now = datetime.now().strftime("%H:%M")
                executed = False

                for r in self.reminders:
                    if r.time == now:

                        # Daily repeating reminders never marked as done
                        if isinstance(r, DailyRoutineReminder) and r.daily_repeat:
                            logging.info(f"[Scheduler] Auto-executing DAILY reminder {r.rem_id} at {now}")
                            print("\a", end="")
                            r.remind()
                            executed = True

                        # One-time reminders
                        elif not r.done:
                            logging.info(f"[Scheduler] Auto-executing reminder {r.rem_id} at {now}")
                            print("\a", end="")
                            r.remind()
                            r.done = True
                            executed = True

                if executed:
                    save_data(self.JSON_PATH, self.reminders)

                time.sleep(interval_seconds)

        self.scheduler_thread = threading.Thread(target=run, daemon=True)
        self.scheduler_thread.start()

    def add_reminder(self, reminder):
        self.reminders.append(reminder)
        save_data(self.JSON_PATH, self.reminders)
        logging.info(f"Added reminder {reminder.rem_id} ({reminder.title})")

    def remove_reminder(self, rem_id):
        for rem in self.reminders:
            if rem.rem_id == rem_id:
                self.reminders.remove(rem)
                save_data(self.JSON_PATH, self.reminders)
                logging.warning(f"Removed reminder {rem_id}")
                return True
        logging.error(f"Tried to remove non-existing reminder {rem_id}")
        return False
    def list_reminders(self):
        if not self.reminders:
            print("\nNo reminders found.")
            return

        print("\n--- Reminders ---")
        sorted_list = sorted(self.reminders, key=lambda r: r.rem_id)

        for r in sorted_list:
            r_type = type(r).__name__
            print(f"[{r.rem_id}] {r.title} at {r.time}")

    def group_reminders(self):
        groups = {}

        for reminder in self.reminders:
            type_name = type(reminder).__name__

            if type_name not in groups:
                groups[type_name] = []

            groups[type_name].append(reminder)

        return groups

    def execute_all(self):
        for r in self.reminders:
            logging.info(f"Executing reminder {r.rem_id}")
            print("\a", end="")
            r.remind()

    def search_reminder(self, rem_id):
        for r in self.reminders:
            if r.rem_id == rem_id:
                return r
        return None