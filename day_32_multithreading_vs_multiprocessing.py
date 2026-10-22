"""

CONCEPT DEFINITIONS & KEY DIFFERENCES:
1. Multithreading: 
   - Multiple threads share the same memory space.
   - Ideal for **I/O-bound tasks** (e.g., downloading files, web scraping, API calls).
   - Limited in Python for CPU-bound tasks due to the Global Interpreter Lock (GIL).
2. Multiprocessing: 
   - Spawns separate independent processes, each with its own Python interpreter and memory space.
   - Ideal for **CPU-bound tasks** (e.g., heavy mathematical computations, image processing, data science).
   - Bypasses the GIL entirely, utilizing multiple CPU cores simultaneously.
3. `multiprocessing` Module: Python's built-in module for creating and managing separate processes.
"""

import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor

# SECTION 1: USING THE `multiprocessing` MODULE

def cpu_heavy_task(number: int):
    """Simulates a heavy CPU-bound computation."""
    print(f"Process starting for number: {number}")
    # Simulating heavy calculation
    total = sum(i * i for i in range(10_000_000))
    print(f"Process finished for number: {number} | Result: {total}")
    return total


if __name__ == "__main__":
    print("--- Testing Basic Multiprocessing ---")
    start_time = time.time()

    processes = []
    numbers_to_process = [1, 2, 3, 4]

    # Spawning individual processes
    for num in numbers_to_process:
        p = multiprocessing.Process(target=cpu_heavy_task, args=(num,))
        processes.append(p)
        p.start()

    # Joining processes to ensure the main program waits for all of them to finish
    for p in processes:
        p.join()

    print(f"All basic processes completed in {time.time() - start_time:.2f} seconds\n")


    # SECTION 2: USING `concurrent.futures.ProcessPoolExecutor`

    print("--- Testing ProcessPoolExecutor & .map() ---")
    exec_start = time.time()

    # ProcessPoolExecutor manages a pool of worker processes automatically
    # Useful for running CPU-bound tasks in parallel across multiple CPU cores
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(cpu_heavy_task, numbers_to_process)
        
        print("Computed Results from Executor:")
        for res in results:
            print(f"Task Result: {res}")

    print(f"ProcessPoolExecutor finished in {time.time() - exec_start:.2f} seconds")