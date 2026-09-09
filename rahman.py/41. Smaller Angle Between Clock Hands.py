hour = int(input("Enter hour (1-12): "))
minute = int(input("Enter minutes: "))

hour_angle = (hour % 12) * 30 + minute * 0.5
minute_angle = minute * 6

angle = abs(hour_angle - minute_angle)

if angle > 180:
    angle = 360 - angle

print("Smaller angle =", angle, "degrees")
