a=10
print (a)

def local():
    b=5
    a=5
    print(a,b)
local()
"""

CONCEPT DEFINITIONS:
1. File I/O (Input/Output): The process of transferring data to/from files stored on disk.
2. File Handles/Pointers: An internal cursor maintained by the OS to track where 
   the next read or write operation will take place inside a file.
3. Resource Management: Closing files frees OS resource locks. Python's 'with' 
   context manager automates cleanup reliably even if errors occur.

"""

import os

# Create sample setup data
demo_filename = "demo_file.txt"

with open(demo_filename, "w") as file:
    file.write("Line 1: Python File Handling\nLine 2: CodeWithHarry Tutorial\nLine 3: File I/O Methods\nLine 4: Deep Dive")



# SECTION 1: BASIC FILE OPENING MODES & READ/WRITE OPERATIONS

"""
OPEN MODES DEFINITION:
- 'r'  : Read mode (default). Raises FileNotFoundError if file does not exist.
- 'w'  : Write mode. Overwrites existing content or creates a new file.
- 'a'  : Append mode. Appends content to the end without deleting old data.
- 'x'  : Exclusive creation. Fails if the file already exists.
- 't'  : Text mode (default). Reads/writes string data.
- 'b'  : Binary mode. Used for images, PDFs, EXEs (e.g., 'rb', 'wb').
"""

# Standard File Opening (Requires Manual Closing)
file_handle = open(demo_filename, "r")
content = file_handle.read() # Reads the entire file content into a string
file_handle.close()          # Always close file handles manually if not using 'with'


# Recommended Method: Context Manager ('with' statement)
# The 'with' block automatically closes the file when the block finishes.
with open(demo_filename, "a") as file:
    file.write("\nLine 5: Appended via Context Manager")



# SECTION 2: READING LINES INDIVIDUALLY AND IN BATCHES

with open(demo_filename, "r") as file:
    # readline(): Reads one line at a time from the current cursor position
    first_line = file.readline()
    second_line = file.readline()
    print(f"First Line: {first_line.strip()}")
    print(f"Second Line: {second_line.strip()}")

with open(demo_filename, "r") as file:
    # readlines(): Reads ALL remaining lines and returns them as a Python List
    all_lines = file.readlines()
    print(f"\nTotal lines returned as list: {len(all_lines)}")


# SECTION 3: WRITING LISTS OF LINES (writelines)

"""
writelines() DEFINITION:
Writes a list of string items directly to the file. 
Note: It does NOT automatically append newlines ('\n')—you must include them manually.
"""

new_filename = "written_lines.txt"
lines_to_write = ["First Line\n", "Second Line\n", "Third Line\n"]

with open(new_filename, "w") as file:
    file.writelines(lines_to_write)


# SECTION 4: ADVANCED FILE POINTER MANIPULATION (seek & tell)

"""
seek(offset) DEFINITION:
Moves the file read/write cursor to a specific byte position.

tell() DEFINITION:
Returns the current byte position of the file cursor.
"""

with open(demo_filename, "r") as file:
    # Read first 10 bytes
    initial_data = file.read(10)
    
    # Check current pointer position
    current_position = file.tell()
    print(f"\nCurrent Pointer Location: Byte {current_position}")
    
    # Reset pointer to the start of the file (Byte 0)
    file.seek(0)
    reset_data = file.read(10)
    print(f"Data read after seek(0): '{reset_data}'")


# SECTION 5: TRUNCATING FILES

"""
truncate(size) DEFINITION:
Resizes the file to the specified byte size. Any data beyond that length is deleted.
Requires write ('w') or append ('a') permission.
"""

trunc_filename = "truncate_demo.txt"

with open(trunc_filename, "w") as file:
    file.write("1234567890 - This extra text will be truncated")

# Truncate the file to keep only the first 10 bytes
with open(trunc_filename, "a") as file:
    file.truncate(10)

with open(trunc_filename, "r") as file:
    print(f"Content after truncate(10): '{file.read()}'")



# CLEANUP DEMO FILES
for temp_file in [demo_filename, new_filename, trunc_filename]:
    if os.path.exists(temp_file):
        os.remove(temp_file)
