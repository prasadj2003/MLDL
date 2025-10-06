from concurrent.futures import ProcessPoolExecutor
import time

def square_numbers(n):
    
    time.sleep(1)
    print(f"square: {n*n}")
    return n*n

numbers = [1,2,3,4,5]

if __name__ == "__main__":
    
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_numbers, numbers)

    for result in results:
        print(result)