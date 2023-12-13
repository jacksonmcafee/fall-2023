"""
Name: Jackson McAfee
Date: 11/19/2023
Assignment: Assignment 12: Using Threads with Locks
Due Date: 11/19/2023
About this project: This script is an example of using threads and locks.
                    It creates "player" and "accountant" threads to watch
                    how players win and lose money. Locks are used to make
                    sure writes / reads aren't happening at the same time. 
Assumptions: None
All work below was performed by Jackson McAfee
"""

# import random for random generation
from random import randrange
from threading import Thread, Lock

# declare global sum variable
totalSum = 0

# declare filename 
money_file = "money.txt"

# declare Lock for synchronization
lock = Lock()
apt_lock = Lock()

activePlayerThreads = 10

# function to clear a file
def clearFile(filename):
    try:
        # open file in write mode and truncate contents
        with open(filename, 'w') as file:
             file.truncate(0)

    # catch any exceptions
    except Exception as e:
        print(f"Error: {e}")

# function to append a number to a file
def appendNumToFile(filename, number):
    try:
        with open(filename, 'a') as file:
            file.write(str(number) + "\n")
            file.flush()

        # print(f"Player won ${number}")
    
    except Exception as e: 
        print(f"Error: {e}")

# function to allow "player" to "play" craps
def crapsPlayer():
    global activePlayerThreads
    playerMoney = 500

    while playerMoney > 0:
        try:
            lock.acquire()
            if playerMoney == 1:
                playerBet = 1
            elif playerMoney <= 0:
                break
            else:
                playerBet = randrange(1, playerMoney)
            
            # generate diceSum
            diceSum = randrange(1,6) + randrange(1,6)

            if diceSum in {2, 3, 4}:
                appendNumToFile(money_file, playerBet * 1)
            elif diceSum in {10, 11}:
                appendNumToFile(money_file, playerBet * 2)
            elif diceSum == 12:
                appendNumToFile(money_file, playerBet * 5)
            else:
                # print(f"A player lost ${playerBet}.")
                playerMoney -= playerBet        

        finally:
            lock.release()

        if playerMoney <= 0:
            with apt_lock:
                # print(f"Player has lost.")
                activePlayerThreads -= 1
                break

def crapsAccountant():
    global totalSum
    global activePlayerThreads

    while activePlayerThreads > 0: 
        try:
            lock.acquire()
            with open(money_file, 'r') as file:
                content = file.readlines()

                for value in content:
                    try:
                        num_value = int(value.strip("\n"))
                        totalSum += num_value
                    except ValueError:
                        print(f"Invalid value detected, skipping: {num_value}")

            clearFile(money_file)  

        except FileNotFoundError:
            print(f"Invalid filename: {money_file}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            lock.release()

def main():
    global totalSum
    global activePlayerThreads

    accountant_thread = Thread(target=crapsAccountant)
    accountant_thread.start()

    player_threads = []
    for _ in range(10):
        player_thread = Thread(target=crapsPlayer)
        player_threads.append(player_thread)
        player_thread.start()

    # Wait for all player threads to finish
    for player_thread in player_threads:
        player_thread.join()

    # End the accountant thread once all players have no more money
    accountant_thread.join()

    print(f"Total sum paid out: ${totalSum}")

if __name__ == "__main__":
    clearFile(money_file)
    main()
