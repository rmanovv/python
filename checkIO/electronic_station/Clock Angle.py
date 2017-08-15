# You are given a time in 24-hour format and you should calculate a lesser angle between the hour and minute hands in degrees.
#  Don't forget that clock has numbers from 1 to 12, so 23 == 11. The time is given as a string with the follow format "HH:MM",
#  where HH is hours and MM is minutes. Hours and minutes are given in two digits format, so "1" will be writen as "01". The result
#  should be given in degrees with precision ±0.1.


def clock_angle(time):

    hour, minute = time.split(':')
    hour = int(hour) % 12
    minute = int(minute)

    hour_angle = (hour + minute/60.0) * 30.0
    minute_angle = 6.0 * minute
    angle = (minute_angle - hour_angle) % 360

    if angle > 180:
        angle = 360 - angle

    return angle

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")

