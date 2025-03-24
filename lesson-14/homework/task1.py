from bs4 import BeautifulSoup

# Load the HTML file
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract table rows
rows = soup.find("table").find("tbody").find_all("tr")

# Store weather data
weather_data = []

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text
    temperature = int(cols[1].text.replace("°C", ""))  # Convert temperature to integer
    condition = cols[2].text
    weather_data.append((day, temperature, condition))

# Display Weather Data
print("5-Day Weather Forecast:")
for day, temp, condition in weather_data:
    print(f"{day}: {temp}°C, {condition}")

# Find the day with the highest temperature
max_temp_day = max(weather_data, key=lambda x: x[1])

# Find all days with "Sunny" conditions
sunny_days = [day for day, temp, cond in weather_data if "Sunny" in cond]

# Calculate average temperature
avg_temp = sum(temp for _, temp, _ in weather_data) / len(weather_data)

# Print Results
print("\nDay with the highest temperature:")
print(f"{max_temp_day[0]}: {max_temp_day[1]}°C")

print("\nDays with 'Sunny' weather:")
print(", ".join(sunny_days))

print(f"\nAverage Temperature for the week: {avg_temp:.2f}°C")
