travel_log = [
    {
        "contry": "USA",
        "Visited places": ["New York", "Boston", "Ohio"],
        "Visit time": 5
    },
     {
        "country": "India",
        "Visited places": ["Agartala", "Tripura", "Mizoram"],
        "Visit time": 9
    },
]


def add_new_country(contry_name, places, visit_frequency):
    new_country ={}
    new_country["contry"] = contry_name
    new_country["Visited places"] = places
    new_country["Visit time"] = visit_frequency
    travel_log.append(new_country)
add_new_country("Russia", ["Leningrad", "Moscow", "khorus"], 7)

print(travel_log)