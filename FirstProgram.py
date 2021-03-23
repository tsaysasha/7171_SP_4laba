import multiprocessing
from random import randint
import time


def decrease_fighters():
    i = randint(1, 100)
    while i > 0:
        print(f'first team: {i}')
        time.sleep(2)
        i = i - randint(1, 10)
        if i < 0:
            print("All first team fighters were killed")


def increase_fighters():
    i = randint(1, 100)
    while i < 200:
        print(f'second team: {i}')
        time.sleep(2)
        i = i + randint(1, 10)
        if i > 200:
            print("The number of fighters has reached the maximum")


if __name__ == '__main__':
    firstProcess = multiprocessing.Process(target=decrease_fighters)
    secondProcess = multiprocessing.Process(target=increase_fighters)

    firstProcess.start()
    secondProcess.start()

    firstProcess.join()
    secondProcess.join()