states = {"lubuskie", "pomorskie", "zachodniopomorskie", "kujawsko-pomorskie", "warminsko-mazurskie", "podlaskie", "lubelskie", "podkarpackie", "swietokrzyskie", "mazowieckie", "lodzkie", "wielkopolskie", "opolskie", "dolnoslaskie", "slaskie", "malopolskie"} # You can type your own states here.
all_radio_stations = {
    "pierwsze": {"lubuskie", "wielkopolskie", "zachodniopomorskie", "dolnoslaskie"},
    "drugie": {"zachodniopomorskie", "kujawsko-pomorskie", "pomorskie", "warminsko-mazurskie"},
    "trzecie": {"kujawsko-pomorskie", "wielkopolskie", "lodzkie"},
    "czwarte": {"wielkopolskie", "lodzkie", "opolskie"},
    "piate": {"dolnoslaskie", "opolskie", "slaskie"},
    "szoste": {"mazowieckie", "kujawsko-pomorskie", "lodzkie", "podlaskie"},
    "siodme": {"podlaskie", "lubelskie"},
    "osme": {"lubelskie", "swietokrzyskie", "mazowieckie", "podkarpackie", "malopolskie"},
    "dziewiate": {"lodzkie", "swietokrzyskie", "malopolskie", "opolskie"},
    "dziesiate": {"lubuskie", "dolnoslaskie", "opolskie"},
    "centrum": {"wielkopolskie", "kujawsko-pomorskie", "mazowieckie", "lodzkie"}
} # You can type your own radio stations and states here.
radio_stations = set()
while states:
    cost_effective_radio_station = None
    cover_states = set()
    for radio_station_name, radio_station_state in all_radio_stations.items():
        covered = states & radio_station_state # common part of the collections
        if len(covered) > len(cover_states):
            cost_effective_radio_station = radio_station_name
            cover_states = covered
    states -= cover_states
    radio_stations.add(cost_effective_radio_station)
print(radio_stations)