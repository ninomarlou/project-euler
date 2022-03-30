def main():
    x = counting_sundays()
    print(x)


def counting_sundays():

    year = 1900
    month = 1
    day = 1
    weekday = 1
    result = 0

    forward = 1

    while forward:

        # day rules
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
                # not leap year
                if day == 28:
                    day = 0
                    month += 1
            else:
                # leap year
                if year % 100 == 0 and year % 400 == 0:
                    if day == 29:
                        # print(day,month,year,weekday,result)
                        day = 0
                        month += 1
                elif year % 100 == 0 and year % 400 != 0:
                    if day == 28:
                        day = 0
                        month += 1
                else:
                    if day == 29:
                        # print(day,month,year,weekday,result)
                        day = 0
                        month += 1

        day += 1

        if weekday == 7:
            weekday = 1
        else:
            weekday += 1

        if weekday == 7 and day == 1 and year > 1900:
            result += 1

        if year == 2001:
            forward = 0

    return result


if __name__ == "__main__":
    main()
