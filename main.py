import logging
from models.DailyRoutineReminder import DailyRoutineReminder
from models.MeetingReminder import MeetingReminder
from models.SimpleReminder import SimpleReminder
from manager.ReminderManager import ReminderManager

def get_data(msg):
    while True:
        data = input(msg).strip()
        if data :
            return data
        else:
            print("This input can not be empty. --> Try again")
            logging.error("Empty input received from user.")

def id_generator():
    current = 0
    while True:
        current += 1
        yield current


id_gen = id_generator()

def main():

    manager = ReminderManager()

    while True:
        print("\n--- Reminder Manager ---")
        print("1) Add reminder")
        print("2) Remove reminder")
        print("3) List reminders")
        print("4) Execute all reminders")
        print("5) Reminder grouping")
        print("6) Finding a reminder by id")
        print("7) Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\nChoose reminder type:")
            print("  1) Simple")
            print("  2) Meeting")
            print("  3) Daily Routine")
            rem_type = input("Type of reminder: ").strip()

            rem_title = get_data("Please enter the reminder title: ")
            rem_time = get_data("Please enter the reminder time: ")

            rem_id = next(id_gen)

            if rem_type == "1":
                reminder = SimpleReminder(rem_title, rem_time, rem_id)
            elif rem_type == "2":
                participants = input("Please enter the name of the participants: ").split()
                reminder = MeetingReminder(rem_title, rem_time, rem_id, participants)
            elif rem_type == "3":
                while True:
                    repeat = input("Do you want a daily repeat? (y/n)")
                    if repeat == "y":
                        reminder = DailyRoutineReminder(rem_title, rem_time, rem_id)
                        break
                    elif repeat == "n":
                        reminder = DailyRoutineReminder(rem_title, rem_time, rem_id, False)
                        break
                    else:
                        print("Invalid option --> Try again")
                        continue
            else:
                continue

            manager.add_reminder(reminder)
            print("Reminder added!")

        elif choice == "2":
            r_id = int(get_data("ID to remove: "))
            if manager.remove_reminder(r_id):
                print("Removed successfully.")
            else:
                print("Reminder not found.")

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
            r_id = int(get_data("Enter ID: "))
            r = manager.search_reminder(r_id)
            if r:
                print(r)
                r.remind()
            else:
                print("Not found.")

        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option --> Try again")

if __name__ == "__main__":
    main()