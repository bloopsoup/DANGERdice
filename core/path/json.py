import json


def save_json(data: dict, file_name: str):
    """Saves data as a JSON file to FILE_NAME."""
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def load_json(file_name: str) -> dict:
    """Loads data from JSON file FILE_NAME. If it doesn't exist, return an empty dictionary."""
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}