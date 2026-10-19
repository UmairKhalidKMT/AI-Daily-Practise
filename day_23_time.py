"""
CONCEPT DEFINITIONS:
1. Time Module: A built-in Python standard library module used to handle time-related 
   tasks such as measuring execution time, pausing execution, and formatting dates.
2. Epoch Time: The point where time starts—specifically January 1, 1970, 00:00:00 UTC, 
   represented as the number of elapsed seconds.
"""

import time

# SECTION 1 CORE TIME MODULE FUNCTIONS

print("--- 1. time.time() [Epoch Time] ---")
# Returns the current time in seconds since the Epoch (January 1, 1970) as a float.
start_epoch = time.time()
print(f"Current Epoch Seconds: {start_epoch}")


print("\n--- 2. Measuring Execution Time ---")
# Using time.time() to measure how long a code block takes to run
start_time = time.time()

# Simulating a task (e.g., counting up to 100,000)
total = 0
for i in range(100000):
    total += i

end_time = time.time()
execution_duration = end_time - start_time
print(f"Task completed in: {execution_duration:.6f} seconds")


print("\n--- 3. time.sleep() [Delay Execution] ---")
# Pauses program execution for a specified number of seconds
print("Waiting for 2 seconds...")
time.sleep(2)
print("Resumed execution after delay!")


print("\n--- 4. time.localtime() & time.strftime() [Formatting Time] ---")
# time.localtime(): Converts epoch seconds into a structured time object
local_time_struct = time.localtime()
print(f"Structured Local Time: {local_time_struct}")

# time.strftime(): Formats the structured time into a readable string
# %Y: Year, %m: Month, %d: Day, %H: Hour, %M: Minute, %S: Second, %p: AM/PM
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S %p", local_time_struct)
print(f"Formatted Readable Time: {formatted_time}")


# SECTION  ADDITIONAL IMPORTANT FUNCTIONS TO REMEMBER

print("\n--- 5. time.perf_counter() [High-Precision Performance Timing] ---")
# Returns a high-precision timer (measured in fractional seconds) ideal for benchmarking code.
perf_start = time.perf_counter()

# Short code snippet to benchmark
sum([x for x in range(10000)])

perf_end = time.perf_counter()
print(f"High-precision execution time: {perf_end - perf_start:.8f} seconds")


print("\n--- 6. time.asctime() & time.ctime() [Quick Human-Readable Strings] ---")
# ctime(): Converts a time expressed in seconds since the epoch to a string string
current_ctime = time.ctime()
print(f"ctime() string output: {current_ctime}")

# asctime(): Converts a time tuple/struct_time to a 24-character string
current_asctime = time.asctime(local_time_struct)
print(f"asctime() string output: {current_asctime}")