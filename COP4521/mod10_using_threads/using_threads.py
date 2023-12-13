'''
Name: Jackson McAfee
Date: 11/5/2023
Assignment: Module 10: Using Threads
Due Date: 11/5/2023
About this project: This script uses threads to calculate the probability of rolling 2 6-sided dice that sum to 7 or 11.
Assumptions: N/A
All work below was performed by Jackson McAfee
'''

import random
from concurrent.futures import ThreadPoolExecutor

def roll_dice(val):
    # generate dice rolls and sum 
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2

    # check if win condition met
    if total in (7, 11):
        return 1
    else:
        return 0

if __name__ == "__main__":
    max_workers = 3
    with ThreadPoolExecutor(max_workers = max_workers) as executor:
        # run 100K times 
        num_trials = 100000
        list_trials = range(num_trials)
        results = executor.map(roll_dice, list_trials)

    # calculate win percentage
    win_count = sum(results)
    win_ratio = win_count / num_trials

    # print results
    print(f"Ratio: {win_ratio:.3f}")
