## A `ThreadPoolExecutor` is a class in Python’s concurrent.futures module that manages a pool of worker threads.
## It allows you to run multiple functions concurrently (at the same time) without manually creating and managing threads.


from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"number: {number}"

numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)

for result in results:
    print(result)
