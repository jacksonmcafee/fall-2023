"""
Name: Jackson McAfee
Date: 11/12/2023
Assignment: Assignment 11: Using Threads with Events
Due Date: 11/12/2023
About this project: This project will demonstrate the use of threads with events to 
                    calculate the future value of an investment.
Assumptions: N/A
All work below was performed by Jackson McAfee
"""

import random, time, concurrent.futures

# global list to hold results
results = []

def calculate_future_value(pv, i, n, t):
    # calculate future value
    fv = pv * (1 + (i / n))**(n * t)
    
    # add result to global list
    results.append((t,fv))

def wait_for_futures(futures):
    # wait for all threads to complete
    for future in concurrent.futures.as_completed(futures):
        future.result()

    # display results
    print("Results:")
    for result in results:
        print("Future value for {} years is ${}".format(
            result[0], result[1]))
        
    # sort by future value and display best investment
    results.sort(key=lambda x: x[1], reverse=True)
    print("Best investment is {} years for ${}".format(
        results[0][0], results[0][1]))

def main():
    # seed random
    random.seed(time.time())

    # set PV and compounding periods per year
    pv = 1000
    n = 12

    # generate random interest rate values
    r1 = random.uniform(0.5, 0.1)
    r2 = random.uniform(0.5, 0.1)
    r3 = random.uniform(0.5, 0.1)

    # create three threads to calculate future value
    # using the same PV and n values
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(calculate_future_value, pv, r1, n, 1),
            executor.submit(calculate_future_value, pv, r2, n, 2),
            executor.submit(calculate_future_value, pv, r3, n, 3)
        ]

        # create a thread that uses events to wait for all threads to complete
        waiting_thread = executor.submit(wait_for_futures, futures)

        # display results
        waiting_thread.result()

if __name__ == "__main__":
    main()
