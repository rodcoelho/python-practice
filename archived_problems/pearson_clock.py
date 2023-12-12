

def clock(hours, minutes):

    hours_in_day = 12
    minutes_in_hour = 60
    
    minutes_angle = minutes/minutes_in_hour * 360

    hour_shift = 1/12 * minutes_angle
    hour_angle = hours/hours_in_day * 360 + hour_shift

    print("hour_angle", hour_angle)
    print("minutes_angle", minutes_angle)

    if hour_angle - minutes_angle > 180:
        return 360-hour_angle - minutes_angle
    return hour_angle - minutes_angle


print("acute angle", clock(9, 0))