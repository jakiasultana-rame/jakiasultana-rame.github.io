import json
import datetime
import sys
import time
from scholarly import scholarly

SCHOLAR_ID = "KH8dL3sAAAAJ"
OUTPUT_PATH = "assets/data/scholar-stats.json"


def fetch():
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["basics"])
    return {
        "citations": author.get("citedby", 0),
        "hIndex": author.get("hindex", 0),
        "i10Index": author.get("i10index", 0),
        "updated": datetime.date.today().isoformat(),
    }


def main():
    data = None
    for attempt in range(3):
        try:
            data = fetch()
            break
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < 2:
                time.sleep(20 * (attempt + 1))

    if data is None:
        print("Could not fetch fresh stats after 3 attempts. Leaving existing file unchanged.")
        sys.exit(0)

    with open(OUTPUT_PATH, "w") as f:
        json.dump(data, f, indent=2)
    print("Saved:", data)


if __name__ == "__main__":
    main()
