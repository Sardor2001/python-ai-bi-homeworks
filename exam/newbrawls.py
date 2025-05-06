import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Step 1: User Input
player_id = input("Enter the Player ID (e.g., P9QRLG9RU): ").strip()

# Step 2: Setup Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4472.124 Safari/537.36"
)
driver = webdriver.Chrome(options=options)

# Step 3: Open URL
url = f"https://brawlstats.com/profile/{player_id}"
driver.get(url)

# Step 4: Wait for Page Content to Load Fully
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/profile')]"))
    )
except Exception as e:
    print(f"Error: {e}. The page took too long to load or no data is present.")
    driver.quit()
    exit()

# Step 5: Fetch the Full Rendered HTML
html = driver.page_source
driver.quit()

# Step 6: Parse the HTML Using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
data = []

# Locate all brawler card containers
brawler_cards = soup.find_all("a", href=lambda href: href and href.startswith("/profile"))

# Step 7: Extract Brawler Data
for card in brawler_cards:
    try:
        # Extract Brawler Name
        name_div = card.find("div", style=lambda value: value and "font-size:23px;" in value)
        brawler_name = name_div.get_text(strip=True) if name_div else "Unknown"
        print(f"Extracted Brawler Name: {brawler_name}")

        # Rank - Find the first numeric value in sibling/child elements
        numeric_divs = card.find_all("div")
        rank = 0
        for div in numeric_divs:
            if div.get_text(strip=True).isdigit():
                rank = int(div.get_text(strip=True))
                print(f"Rank Value: {rank}")
                break

        # Level - Find Level label and fetch adjacent text
        level = 0
        level_label = card.find(string=re.compile(r'Level', re.IGNORECASE))
        if level_label:
            next_text = level_label.find_next(string=True)
            if next_text:
                numbers = re.findall(r'\d+', next_text)
                if numbers:
                    level = int(numbers[0])
        print(f"Level for {brawler_name}: {level}")

        # Current Trophies - Find Current label and fetch adjacent text
        current_trophies = 0
        current_label = card.find(string=re.compile(r'Current', re.IGNORECASE))
        if current_label:
            next_text = current_label.find_next(string=True)
            if next_text:
                numbers = re.findall(r'\d+', next_text)
                if numbers:
                    current_trophies = int(numbers[0])
        print(f"Current Trophies for {brawler_name}: {current_trophies}")

        # Max Trophies - Find Highest label and fetch adjacent text
        max_trophies = 0
        highest_label = card.find(string=re.compile(r'Highest', re.IGNORECASE))
        if highest_label:
            next_text = highest_label.find_next(string=True)
            if next_text and next_text.strip().isdigit():
                max_trophies = int(next_text.strip())
        print(f"Max Trophies for {brawler_name}: {max_trophies}")

        # Store data for this brawler
        data.append({
            "Brawler": brawler_name,
            "Level": level,
            "Rank": rank,
            "Current Trophies": current_trophies,
            "Max Trophies": max_trophies
        })

        # Debugging
        print(f"Extracted Data: Brawler: {brawler_name}, Level: {level}, Rank: {rank},"
              f" Current Trophies: {current_trophies}, Max Trophies: {max_trophies}")

    except Exception as e:
        print(f"Error processing brawler card: {e}")
        continue

# Step 8: Store Data into a Pandas DataFrame
df = pd.DataFrame(data, columns=["Brawler", "Level", "Rank", "Current Trophies", "Max Trophies"])

# Replace NaN or Null Values with 0
df.fillna(0, inplace=True)

# Step 9: Sort the DataFrame
df.sort_values(by=["Max Trophies", "Current Trophies", "Brawler"], ascending=[False, False, True], inplace=True)

# Step 10: Create a Second DataFrame for Brawlers with Level >= 9
df2 = df[df["Level"] >= 9]

# Step 11: Export to Excel - Two Sheets
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_filename = f"{player_id}_{timestamp}.xlsx"

with pd.ExcelWriter(output_filename, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Brawlers for Regular Games", index=False)
    df2.to_excel(writer, sheet_name="Brawlers for Ranked Games", index=False)

print(f"Data successfully saved to {output_filename}")