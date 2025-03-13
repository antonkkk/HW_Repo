# 7. Json
import json

with open('clubs.json', 'r', encoding='utf-8') as file:
    clubs = json.load(file)

selected_countries = ["Франция", "Германия", "Италия"]
filtered_clubs = [club for club in clubs if club['страна'] in selected_countries]

max_wins_club = max(filtered_clubs, key=lambda club: club['победы'])

print("Клуб с наибольшим количеством побед:")
print(f"Название: {max_wins_club['название']}")
print(f"Страна: {max_wins_club['страна']}")
print(f"Количество побед: {max_wins_club['победы']}")
