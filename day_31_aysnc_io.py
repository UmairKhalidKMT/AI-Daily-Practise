"""

CONCEPT DEFINITIONS:
1. Asynchronous Programming: A programming paradigm that allows multiple tasks to run 
   concurrently without waiting for one task to finish before starting another (non-blocking).
2. Coroutine: A special function defined with `async def` that can be paused and resumed, 
   allowing other tasks to run in the meantime using the `await` keyword.
3. asyncio: Python's built-in standard library module for writing concurrent code using 
   the async/await syntax.

"""

import asyncio
import time

# ==============================================================================
# SECTION 1: CREATING AND RUNNING ASYNC COROUTINES
# ==============================================================================

async def fetch_data(task_id: int, delay: int):
    """An asynchronous coroutine simulating a network request or I/O operation."""
    print(f"Task {task_id}: Started...")
    # asyncio.sleep() is non-blocking (unlike time.sleep())
    await asyncio.sleep(delay)
    print(f"Task {task_id}: Completed after {delay} seconds!")
    return f"Data from Task {task_id}"


async def main():
    """Main coroutine to coordinate execution."""
    print("--- Testing AsyncIO in VS Code ---")
    start_time = time.time()

    # ==========================================================================
    # SECTION 2: RUNNING TASKS CONCURRENTLY WITH asyncio.gather()
    # ==========================================================================
    # asyncio.gather() runs multiple coroutines concurrently and waits for all of them to finish
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 3),
        fetch_data(3, 1)
    )

    print(f"\nAll tasks finished! Results: {results}")
    print(f"Total execution time: {time.time() - start_time:.2f} seconds")


# ==============================================================================
# EXECUTION ENTRY POINT
# ==============================================================================

if __name__ == "__main__":
    # asyncio.run() manages the event loop, runs the coroutine, and closes the loop
    asyncio.run(main())