rover_status = {
    "Battery" : 85,
    "Heater" : "On",
    "Camera" : "Standby",
    "Speed" : 5
}
print(rover_status["Battery"])
print(rover_status)

mission_log = [{"Site": "Crater A", "Radiation": "Low", "Water": False},{"Site": "Dune B", "Radiation": "High", "Water": True}]
for i in range(len(mission_log)):
    sites = mission_log[i]["Site"]
    rads = mission_log[i]["Radiation"]
    print(f"Site {sites} has {rads.lower()} radiation")
    i += 1