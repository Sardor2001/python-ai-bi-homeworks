import requests
import json
from bs4 import BeautifulSoup

BASE_URL = "https://www.demoblaze.com/"
CATEGORIES_URL = "https://api.demoblaze.com/bycat"
NEXT_PAGE_URL = "https://api.demoblaze.com/pagination"  # Not an actual endpoint, used for pagination simulation

HEADERS = {"Content-Type": "application/json"}


def get_laptops():
    """Scrape laptop data from Demoblaze and store it in JSON format."""
    laptops = []
    payload = {"cat": "notebook"}  # Request payload to get laptops

    response = requests.post(CATEGORIES_URL, headers=HEADERS, json=payload)
    if response.status_code != 200:
        print("Failed to fetch data")
        return

    data = response.json()

    for item in data.get("Items", []):
        laptop = {
            "name": item.get("title", "Unknown"),
            "price": f"${item.get('price', 'N/A')}",
            "description": item.get("desc", "No description available"),
        }
        laptops.append(laptop)

    # Save data to JSON file
    with open("laptops.json", "w", encoding="utf-8") as f:
        json.dump(laptops, f, indent=4, ensure_ascii=False)

    print("Laptop data has been saved to laptops.json")


if __name__ == "__main__":
    get_laptops()
