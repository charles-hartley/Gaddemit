distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for index, (name, distance) in enumerate (distances.items()):
        print(f"{name} is {distances[name]} AU or {convert(distances[name])} Metres from Earth")

def convert(au):
    return au * 149597870700
main()