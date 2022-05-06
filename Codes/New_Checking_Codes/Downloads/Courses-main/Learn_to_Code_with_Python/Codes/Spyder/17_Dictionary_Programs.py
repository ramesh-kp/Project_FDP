# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 22:58:22 2021
@author: ramesh.kp
"""

print()
print("#" * 30)
ice_cream_preferences = {
    "Benjamin": "Chocolate",
    "Sandy": "Vanilla",
    "Marv": "Cookies and Creme",
    "Julia": "Chocolate"
    }
print(len(ice_cream_preferences))
print(ice_cream_preferences)
print("#" * 30)

# Get Function
flight_prices = {
    "Chicago": 199,
    "San Francisco": 499,
    "Denver": 295
    }
print(flight_prices["Chicago"])
print(flight_prices["Denver"])
gym_membership_packages = {
    29: ["Machines"],
    49: ["Machines", "Vitamin Supplements"],
    79: ["Machines", "Vitamin Supplements", "Sauna"]
    }
print(gym_membership_packages[49])
print(gym_membership_packages[79])
print(gym_membership_packages.get(29, ["Basic Dumbbells"]))
print(gym_membership_packages.get(100, ["Basic Dumbbelles"]))
print(gym_membership_packages.get(100))
print("#" * 30)

pokemon = {
    "Fire": ["Charmander", "Charmeleon", "Charizard"],
    "Water": ["Squirtle", "Warturtle", "Blastoise"],
    "Grass": ["Bulbasaur", "Venusaur", "Ivysaur"]
    }
print("Fire" in pokemon)
print("Grass" in pokemon)
print("Water" not in pokemon)
print("#" * 30)

sports_team_rosters = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
    "New York Giants": ["Eli Manning", "Odell Beckham"]
    }
sports_team_rosters["Pittsburgh Steelers"] = ["Ben Roethlisberger", "Antonio Brown"]
print(sports_team_rosters["Pittsburgh Steelers"])
print(sports_team_rosters)
vedio_game_options = {}
vedio_game_options["Subtitles"] = True
vedio_game_options["Difficulty"] = "Medium"
vedio_game_options["Volume"] = 7
print(vedio_game_options)
vedio_game_options["Difficulty"] = "Hard"
vedio_game_options["Subtitles"] = False
vedio_game_options["volume"] = 10
print(vedio_game_options)
words = ["Danger", "Beware", "Danger", "Beware", "Beware"]
def count_words(words):
    counts = {}
    for i in words:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
print(count_words(words))
print("#" * 30)

# Setdefault Function
film_directors = {
    "The Godfather": "Francis Ford Coppola",
    "The Rock": "Michael Bay",
    "Goodfellas": "Martin Scorsese"
    }
print(film_directors)
print(film_directors.get("Goodfellas"))
print(film_directors.get("Bad Boys", "Michael Bay"))
print(film_directors)
film_directors.setdefault("Bad Boys", "A good director")
print(film_directors)
print(film_directors.get("Bad Boys", "Michael Bay"))
print("#" * 30)

# Pop and Del Function
release_dates = {
    "Python": 1991,
    "Ruby": 1995,
    "Java": 1995,
    "Go": 2007
    }
print(release_dates)
release_dates.pop("Java")
print(release_dates)
new_year_first = release_dates.pop("C++", 2000)
new_year_second = release_dates.pop("Ruby", 2000)
print(new_year_first)
print(new_year_second)
del release_dates["Go"]
print(release_dates)
print("#" * 30)

# Clear Function
websites = {
    "Wikipedia": "http://www.wikipedia.org",
    "Google": "http://wwww.google.com",
    "Netflix": "http://www.netflix.com"
    }
print(websites)
websites.clear()
print(websites)
print("#" * 30)

# Update Function
employee_salary = {
    "Guido": 100000,
    "James": 500000,
    "Brandon": 900000
    }
print(employee_salary)
extra_employee_salary = {
    "Yukihiro": 1000000,
    "Guido": 333333
    }
employee_salary.update(extra_employee_salary)
print(employee_salary)
print("#" * 30)

# Dict Function
employee_titles = [
    ["Mary", "Senior Manager"],
    ["Brian", "Vice President"],
    ["Julie", "Assistant Vice President"]
    ]
print(employee_titles)
print(dict(employee_titles))
print("#" * 30)

# Nested Dictionaries
tv_shows = {
    "The X-Files": {
        "Season 1": {
            "Episodes": ["Scary Monster", "Scary Alien"],
            "Genre": "Science Fiction",
            "Year": 1993
            },
        "Season 2": {
            "Episodes": "Scary Conspiracy",
            "Genre": "Horror",
            "Year": 1994
            }
        },
    "Lost": {
        "Season 1": {
            "Episodes": "What the hack is happeneing on this island?",
            "Genre": "Science Fiction",
            "Year": 2004
            }
        }
    }
print(tv_shows)
print(tv_shows["The X-Files"]["Season 1"]["Episodes"][1])
print(tv_shows["The X-Files"]["Season 2"]["Year"])
print(tv_shows["Lost"]["Season 1"]["Genre"])

print("#" * 30)
print()
