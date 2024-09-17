travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "total_visits": visits, "cities_visited": cities})
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
