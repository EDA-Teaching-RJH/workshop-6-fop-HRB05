try:
    x = input("Enter Motor Speed: ")
    print(f"Speed set to {int(x)}")
except:
    print("Error: Corrupted Signal. Maintaining current speed.")