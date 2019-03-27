import datetime


def most_frequent_days(year):

    day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    first_day = datetime.date(year, 1, 1)
    last_day = datetime.date(year, 12, 31)

    counter = [0]*7

    for i in range(first_day.weekday(), 7):
        counter[i] += 1

    for i in range(0, last_day.weekday() + 1):
        counter[i] += 1

    max_count = max(counter)

    max_count_days = []

    for i, count in enumerate(counter):
        if count == max_count:
            max_count_days.append(day_of_week[i])

    return max_count_days

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent_days(2399) == ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"

