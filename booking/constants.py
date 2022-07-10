base_url = "https://www.booking.com"

def month_to_int(mois):
    switch = {
        "janvier" : 1,
        "février" : 2,
        "mars" : 3,
        "avril" : 4,
        "mai": 5,
        "juin": 6,
        "juillet": 7,
        "août": 8,
        "septembre": 9,
        "octobre": 10,
        "novembre": 11,
        "décembre": 12,
    }
    return switch.get(mois)