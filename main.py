import logging
from models.DailyRoutineReminder import DailyRoutineReminder
from models.MeetingReminder import MeetingReminder
from models.SimpleReminder import SimpleReminder
from manager.ReminderManager import ReminderManager
from id_generator import id_gen
import dateparser

def get_data(msg):
    while True:
        data = input(msg).strip()
        if data :
            return data
        else:
            print("\nThis input can not be empty. --> Try again")
            logging.error("Empty input received from user.")

def parse_time(text):
    data = dateparser.parse(text)
    if not data:
        print("\nCould not understand time. Please try again.")
        logging.error("Could not understand time input received from user.")
        return None

    return data.strftime("%H:%M")

def main():

    manager = ReminderManager()
    manager.start_scheduler()

    while True:
        print("\n--- Reminder Manager ---")
        print("1) Add reminder")
        print("2) Remove reminder")
        print("3) List reminders")
        print("4) Execute all reminders")
        print("5) Reminder grouping")
        print("6) Finding a reminder by id")
        print("7) Exit")
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            print("\nChoose reminder type:")
            print("  1) Simple")
            print("  2) Meeting")
            print("  3) Daily Routine")
            rem_type = input("\nType of reminder: ").strip()

            rem_title = get_data("\nPlease enter the reminder title: ")
            while True:
                raw_time = get_data("\nEnter time (natural language allowed): ")
                rem_time = parse_time(raw_time)
                if rem_time:
                    break

            rem_id = next(id_gen)

            if rem_type == "1":
                reminder = SimpleReminder(rem_title, rem_time, rem_id)
            elif rem_type == "2":
                participants = input("\nPlease enter the name of the participants: ").split()
                reminder = MeetingReminder(rem_title, rem_time, rem_id, participants=participants)
            elif rem_type == "3":
                while True:
                    repeat = input("\nDo you want a daily repeat(y/n)? ")
                    if repeat == "y":
                        reminder = DailyRoutineReminder(rem_title, rem_time, rem_id)
                        break
                    elif repeat == "n":
                        reminder = DailyRoutineReminder(rem_title, rem_time, rem_id, False)
                        break
                    else:
                        print("\nInvalid option --> Try again")
                        continue
            else:
                print("\nInvalid option --> Try again")
                logging.error(f"Invalid menu option entered.")
                continue

            manager.add_reminder(reminder)
            print("\nReminder added!")

        elif choice == "2":
            r_id = int(get_data("\nID to remove: "))
            if manager.remove_reminder(r_id):
                print("\nRemoved successfully.")
            else:
                print("\nReminder not found.")
                logging.error(f"Reminder not found.")

        elif choice == "3":
            manager.list_reminders()

        elif choice == "4":
            manager.execute_all()

        elif choice == "5":
            groups = manager.group_reminders()
            for gname, items in groups.items():
                print(f"\n{gname}:")
                for r in items:
                    print(f"  - [{r.rem_id}] {r.title}")
        elif choice == "6":
            r_id = int(get_data("\nEnter ID: "))
            r = manager.search_reminder(r_id)
            print(r)

        elif choice == "7":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option --> Try again")
            logging.error(f"Invalid menu option entered.")

if __name__ == "__main__":
    main()