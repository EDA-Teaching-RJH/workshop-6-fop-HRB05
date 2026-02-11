
def get_coordinate():
    while True:
        try:
            x = input("What is the X coordinate: ")
            print(f"Coordinate set to {int(x)}")
            break
        except:
            print("Invalid coordinate")
            continue

get_coordinate()