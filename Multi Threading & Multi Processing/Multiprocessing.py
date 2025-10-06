## processes that run in parallel
## CPU bound tasks that are heavy. eg: mathematical computation, data processing
## parallel execution - multiple cores of CPU

import multiprocessing
import time
from datetime import datetime

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube: {i*i*i}")

if __name__ == "__main__":
    # Create 2 processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    start_time = datetime.now()

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    finish_time = datetime.now()
    print(f"Finished in: {finish_time - start_time}")
