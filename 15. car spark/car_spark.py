from __future__ import print_function
from pprint import pprint

# number_of_test_cases
T = int(raw_input())

for _ in range(T):
    # number_of_bookings
    N = int(raw_input())

    bookings = []

    for _ in range(N):
        line = raw_input()

        B_s, B_e, A_i = line.split()
        # booking start time
        B_s = int(B_s)
        # booking end time
        B_e = int(B_e)
        # amount the customer is willing to spend
        A_i = int(A_i)

        bookings.append( (B_s, B_e, A_i) )

    print("bookings:")
    print(bookings)

    bookings.sort(key=lambda x: x[2], reverse=True)
    print(bookings)

    break_flag = False
    booked = []
    total_amount = 0
    for booking in bookings:
        for hour in range(booking[0], booking[1]):
            if hour in booked:
                break_flag = True
                break

        if break_flag:
            break

        for hour in range(booking[0], booking[1]):
            booked.append(hour)

        total_amount += booking[2]

    print("booked:")
    print(booked)

    print("total_amount:")
    print(total_amount)
