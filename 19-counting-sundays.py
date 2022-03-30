def main():
    start_year = 1901
    end_year = 2000
    x = counting_sundays(start_year, end_year)
    print(x)


def counting_sundays(start_year, end_year):

    year = 1900
    month = 1
    day = 1
    weekday = 1
    result = 0

    forward = 1

    while forward:

        if month in [9, 4, 6, 11] and day == 30:
            day = 0
            month += 1

        if month in [1, 3, 5, 7, 8, 10, 12] and day == 31:
            if month != 12:
                day = 0
                month += 1
            else:
                month = 1
                day = 0
                year += 1

        if month == 2:
            if year % 4 != 0:
                if day == 28:
                    day = 0
                    month += 1
            else:
                if year % 100 == 0 and year % 400 == 0:
                    if day == 29:
                        day = 0
                        month += 1
                elif year % 100 == 0 and year % 400 != 0:
                    if day == 28:
                        day = 0
                        month += 1
                else:
                    if day == 29:
                        day = 0
                        month += 1

        day += 1

        if weekday == 7:
            weekday = 1
        else:
            weekday += 1

        if weekday == 7 and day == 1 and year >= start_year:
            result += 1

        if year == (end_year) + 1:
            forward = 0

    return result


if __name__ == "__main__":
    main()
