speed = float(input("Give the current speed in km/h"))
limit = float(input("What is the allowed speed on the road"))
points = (speed-limit)/5
if speed < 60:
    print("OK")
else:
    print(points)
    if points > 60:
        print("You are over the limit")
