import json

JSON_PATH = "data/reminders.json"

def max_id():

    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not data:
                return 0

            return max(item.get("rem_id", 0) for item in data)

    except Exception:
        return 0
def id_generator():
    current = max_id()
    while True:
        current += 1
        yield current

id_gen = id_generator()
