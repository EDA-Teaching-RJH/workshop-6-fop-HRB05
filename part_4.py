travel_log = []
while True:
    try:
        x = input("Sensor Reading (Slope Angle): ")
        int(x)
        if x > 45:
            print("CRITICAL TILT! HALTING.")
            break
        else:
            travel_log.append(x)
            print("Path Stable. Moving forward.")
    except:
        print("Sensor Glitch")
        continue

