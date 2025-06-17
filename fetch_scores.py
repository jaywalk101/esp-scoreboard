import requests
import json
import datetime
import os

# TheSportsDB free API key (you can register for your own later)
API_KEY = "1"
SPORT = "Baseball"

# Create output directory
os.makedirs("public", exist_ok=True)

# Get today's date in YYYY-MM-DD
today = datetime.datetime.now().strftime("%Y-%m-%d")

# Fetch games for today
url = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/eventsday.php?d={today}&s={SPORT}"
resp = requests.get(url)
data = resp.json()

output = []
for event in data.get("events", []):
    home = event["strHomeTeam"]
    away = event["strAwayTeam"]
    home_score = event.get("intHomeScore", "?")
    away_score = event.get("intAwayScore", "?")
    status = event.get("strStatus", "Scheduled")

    # Create a simple scroll line
    line = f"{away} {away_score} vs {home} {home_score} - {status}"
    output.append({
        "line": line,
        "abbr1": away,
        "abbr2": home,
        "score1": away_score,
        "score2": home_score,
        "status": status
    })

# Save to public/mlb_scroll.json
with open("public/mlb_scroll.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ MLB scores saved to public/mlb_scroll.json")
