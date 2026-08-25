import json
import logging
import re
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

NOTES_FILE = Path("notes.json")

def load_notes()-> list:
    if not NOTES_FILE.exists():
        logging.warning(f"Notes file {NOTES_FILE} not found")
        return []
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        logging.info(f"Notes file {NOTES_FILE} loaded")
        return json.load(f)

def save_notes(text: str)-> None:
    notes = load_notes()
    note = {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "text": text}
    notes.append(note)

    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=4)
    logging.info(f"Note saved to {NOTES_FILE}")


def search_notes(keyword: str)-> list:
    notes = load_notes()

    # matches = []
    # for note in notes:

    #     text = note["text"]

    #     match = re.search(keyword, text, re.IGNORECASE)
    #     matches.append(match)

    return [ note for note in notes if re.search(keyword, note["text"], re.IGNORECASE)]

if __name__ == "__main__":
    save_notes("This is my daily routing notebook")
    save_notes("My mobine number is 9876543210")
    save_notes("This is my personal notebook so if you opeded then please close it.")

    search_results = search_notes("9876543210")
    print(search_results)



