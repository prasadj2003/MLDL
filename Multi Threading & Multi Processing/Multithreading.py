## Multithreading

## when to use -> I/O bound tasks and concurrent execution

# import threading
# import time

# def print_num():
#     for i in range(5):
#         time.sleep(2)
#         print(f"number: {i}")


# def print_letter():
#     for letter in "abcde":
#         time.sleep(2)
#         print(f"letter: {letter}")

# t=time.time()
# print_num()
# print_letter()
# finish = time.time()
# print(f"time taken: {finish-t}")

## What is happening is while my print num fiunction is waiting, print letter function is also waiting, I can make the print letter function run while print num is waiting


import threading
import time

def print_num():
    for i in range(5):
        time.sleep(2)
        print(f"number: {i}")


def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter: {letter}")

## Creating 2 threads

t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_letter)


t=time.time()
## star the thread
t1.start()
t2.start()

## Wait for the threads to complete
## join will join the threads to the main thread
t1.join()
t2.join()
finish = time.time()
print(f"time taken: {finish-t}")

