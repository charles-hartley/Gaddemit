import random  # Simulating distance updates

def calculate_distance():
    """
    Simulate calculating or receiving new distance data from motion sensors.
    Returns a new distance (in AU) for the spacecraft.
    """
    # Replace this with real sensor data retrieval or calculations
    return round(random.uniform(0.01, 5.0), 2)  # Simulating random distance values between 0.01 and 5.0 AU

def main():
    spacecraft = {"name": "James Webb Space telescope"}
    spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    
    # Simulate receiving updated distance
    new_distance = calculate_distance()
    spacecraft["distance"] = new_distance  # Update the dictionary with the new distance
    
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ===== REPORT =====

    Name: {spacecraft.get("name", "unknown")}
    Distance: {spacecraft.get("distance", "unknown")} AU
    Orbit: {spacecraft.get("orbit", "unknown")}

    ==========
    """

main()
