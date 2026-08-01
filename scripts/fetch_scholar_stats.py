import json
import datetime
from scholarly import scholarly

SCHOLAR_ID = "KH8dL3sAAAAJ"
OUTPUT_PATH = "assets/data/scholar-stats.json"

author = scholarly.search_author_id(SCHOLAR_ID)
author = scholarly.fill(author)

data = {
    "citations": author.get("citedby", 0),
    "hIndex": author.get("hindex", 0),
    "i10Index": author.get("i10index", 0),
    "updated": datetime.date.today().isoformat()
}

with open(OUTPUT_PATH, "w") as f:
    json.dump(data, f, indent=2)

print("Saved:", data)
