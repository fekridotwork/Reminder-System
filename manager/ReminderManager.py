from manager.file_manager import load_data, save_data


class ReminderManager:
    JSON_PATH = "REMINDER-SYSTEM/data/reminders.json"
    LOG_PATH = "REMINDER-SYSTEM/data/reminders.log"

    def __init__(self):
        self.reminders = load_data(self.JSON_PATH)

    def add_reminder(self, reminder):
        self.reminders.append(reminder)
        save_data(self.JSON_PATH, self.reminders)
        # Log

    def remove_reminder(self, rem_id):
        for rem in self.reminders:
            if rem.rem_id == rem_id:
                self.reminders.remove(rem)
                save_data(self.JSON_PATH, self.reminders)
                # Log
                return True
        return False
    def list_reminders(self):
        for r in self.reminders:
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
            # log
            r.remind()

    def search_reminder(self, rem_id):
        for r in self.reminders:
            if r.rem_id == rem_id:
                return r
        return None