# Reminder-System
A Python-based reminder management system built as part of Maktab137 HW12.

This project is a simple Reminder Management System.  
It allows users to create and manage different types of reminders:

- SimpleReminder – a normal reminder with title & time  
- MeetingReminder – includes participants  
- DailyRoutineReminder – can repeat daily
All thses three reminder class inherit from reminder base class

Each reminder has a unique ID generated using a generator.  
All reminders are saved into a JSON file and reloaded when the program starts and we have a file manager for working with json file like save and load data and in those functions we used to_dict and from_dict functions and for to_dict we used to_dict abstractmethods in each reminder class.
Each reminder class also have remind abstractmethod for when we want to execute all reminders.
The system uses Rotating Log Files to record actions such as adding, removing, or executing reminders.

---

Features (v1.0.0)
- Add reminder (3 types)
- Remove reminder
- Execute all reminders (polymorphism)
- Find reminder by ID
- Group reminders by type
- JSON save/load
- Rotating log file (100 KB)
- Input validation (title/time cannot be empty)

---

How to Run :

python3 main.py

OUTPUT Example:
--- Reminder Manager ---
1) Add reminder
2) Remove reminder
3) List reminders
4) Execute all reminders
5) Reminder grouping
6) Finding a reminder by id
7) Exit
Choose an option: 1

Choose reminder type:
  1) Simple
  2) Meeting
  3) Daily Routine
Type of reminder: :2
Please enter the reminder title.Project Meeting
Please enter the reminder time: 14:00
Please enter the name of the participants: Ali Sara Hamid
Reminder added!

--- Reminder Manager ---
1) Add reminder
2) Remove reminder
3) List reminders
4) Execute all reminders
5) Reminder grouping
6) Finding a reminder by id
7) Exit
Choose an option: 7
Goodbye!

