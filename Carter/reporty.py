def main():
    spacecraft = {"name": "James Webb Space telescope"}
    spacecraft.update({"distance": 0.01, "orbirt": "Sun"})

    #simulate receiving new distance data
    new_distance = 0.0015 #example data from motion sensors
    update_distance(spacecraft, new_distance)

    print(create_report(spacecraft))

def update_distance(spacecraft, distance):
    """
    Updates the spacecraft dictionary with a new distance value.
    """
    spacecraft["distance"] = distance

def create_report(spacecraft):
    return f"""
    ===== REPORT =====

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "unknown")} AU
    Orbit: {spacecraft.get("orbit", "unknown")}

    ========
    """

main()