
def get_coordinate():
    while True:
        try:
            x = input("What is the X coordinate: ")
            print(f"Coordinate set to {int(x)}")
        except:
            print("Invalid coordinate")
            continue
        if -100 < x < 100:
            print(f"Coordinate set to {int(x)}")
            break
        else:
            print("Coordinate out of range")
            continue

get_coordinate()