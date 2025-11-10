'''
Real-world scenario: Factorial calculation. Ditributing it over multiple CPU cores for improving perfomance
'''

import multiprocessing
import math
import sys
import time

# increas the max number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## funtion to compute factorial of a given number

def compute_factorial(num):
    print(f"Computing factorial of {num}")
    result = math.factorial(num)
    print(f"factorial is: {result}")
    return result

if __name__ == "__main__":
    numbers = [5000, 6000, 7000, 8000]
    start_time = time.time()

    ## create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    end_time = time.time()
    print(f"Results: {results}")
    print(f"time taken: {end_time - start_time}")