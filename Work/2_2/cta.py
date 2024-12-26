# cta.py

# exercise 2.2

import readrides
from collections import Counter


def total_rides(rides):
    """
    Calculate the total number of rides
    """
    tot_rides = {ride["route"] for ride in rides}
    return len(tot_rides)


def people_on_date_and_route(date, route):
    """
    Calculate the total number of people on a given date
    """
    tot_rides = 0
    for ride in rides:
        if ride["date"] == date and ride["route"] == route:
            tot_rides += ride["rides"]
    return tot_rides


def total_number_of_rides(rides):
    """
    Calculate the total number of rides
    """
    total = Counter()
    for ride in rides:
        total[ride["route"]] += ride["rides"]

    top_three = total.most_common(3)
    return top_three


def ride_increase(rides):
    """
    Calculate the ride increase
    """
    counter_2001 = Counter()
    counter_2011 = Counter()
    for i in range(2001, 2012):
        if i == 2001 or i == 2011:
            for ride in rides:
                if str(i) in ride["date"]:
                    if i == 2001:
                        counter_2001[ride["route"]] += ride["rides"]
                    else:
                        counter_2011[ride["route"]] += ride["rides"]

            ride_increase = counter_2011 - counter_2001
            top_five = ride_increase.most_common(5)
        else:
            continue
    return top_five


if __name__ == "__main__":
    rides = readrides.read_rides_as_dicts("../Data/ctabus.csv")
    print("Nº of bus routes in Chicago:", total_rides(rides))
    print(
        "Nº of people on 02/02/2011 on route 22:",
        people_on_date_and_route("11/25/2003", "22"),
    )
    print("Top 3 bus routes with most rides:", total_number_of_rides(rides))
    print("Top 5 bus routes with most rides increase:", ride_increase(rides))
