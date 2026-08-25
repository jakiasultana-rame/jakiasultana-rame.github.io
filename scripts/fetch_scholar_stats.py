import json
import datetime
import sys
from scholarly import scholarly, ProxyGenerator

SCHOLAR_ID = "KH8dL3sAAAAJ"
OUTPUT_PATH = "assets/data/scholar-stats.json"


def setup_proxy():
    pg = ProxyGenerator()
    ok = pg.FreeProxies()
    if ok:
        scholarly.use_proxy(pg)
    return ok


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
    setup_proxy()  # fine if this returns False, we still try direct after
    try:
        data = fetch()
    except Exception as e:
        print(f"Could not fetch fresh stats ({e}). Leaving existing file unchanged.")
        sys.exit(0)  # don't fail the workflow just because Scholar blocked us today

    with open(OUTPUT_PATH, "w") as f:
        json.dump(data, f, indent=2)
    print("Saved:", data)


if __name__ == "__main__":
    main()
