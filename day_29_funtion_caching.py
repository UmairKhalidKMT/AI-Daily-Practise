"""

CONCEPT DEFINITIONS:
1. Function Caching: A technique that stores the results of expensive function calls 
   and returns the cached result when the same inputs occur again.
2. Memoization: An optimization technique used primarily to speed up computer programs 
   by storing the results of heavy function calls and returning the cached result 
   when the same inputs are requested.
3. @lru_cache (Least Recently Used Cache): A built-in decorator from the `functools` 
   module that automatically caches function return values up to a specified maximum size.
"""

import time
from functools import lru_cache


# SECTION 1: USING @lru_cache FOR PERFORMANCE OPTIMIZATION

# maxsize specifies how many recent return values should be stored (None = unlimited)
@lru_cache(maxsize=32)
def expensive_computation(n: int):
    """Simulates a time-consuming computation (e.g., database query or heavy math)."""
    print(f"Computing result for {n} (This takes 3 seconds)...")
    time.sleep(3)  # Simulate delay
    return n * 10


print("--- Testing Function Caching in VS Code ---")

# 1. First call with argument 5 (Takes ~3 seconds)
start = time.time()
print(f"Result for 5: {expensive_computation(5)}")
print(f"Time taken: {time.time() - start:.2f} seconds\n")

# 2. Second call with argument 5 (Instantly retrieved from cache!)
start = time.time()
print(f"Result for 5 (Cached): {expensive_computation(5)}")
print(f"Time taken: {time.time() - start:.2f} seconds\n")

# 3. Call with a new argument 10 (Takes ~3 seconds because it's not cached yet)
start = time.time()
print(f"Result for 10: {expensive_computation(10)}")
print(f"Time taken: {time.time() - start:.2f} seconds\n")

# 4. Inspecting cache statistics
print(f"Cache Info: {expensive_computation.cache_info()}")

# To clear the cache manually if needed:
# expensive_computation.cache_clear()