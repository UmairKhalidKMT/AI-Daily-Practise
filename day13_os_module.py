"""

CONCEPT DEFINITIONS:
- os Module: A built-in Python standard library module that provides functions 
             for interacting with the host operating system.
- Cross-Platform File Handling: Using 'os.path' guarantees code works seamlessly 
             across Windows (uses '\') and Linux/Mac (uses '/').

"""

import os


# DIRECTORY OPERATIONS

# os.getcwd(): Returns the Current Working Directory as a string
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# os.mkdir("folder_name"): Creates a single new directory
if not os.path.exists("test_folder"):
    os.mkdir("test_folder")  # Creates 'test_folder'

# os.makedirs("path/to/folder"): Creates nested directories recursively
if not os.path.exists("parent_folder/child_folder"):
    os.makedirs("parent_folder/child_folder")  # Creates both parent and child

# os.listdir(path): Returns a list of all files/folders in the specified directory
files_and_folders = os.listdir(".")
print(f"Directory Contents: {files_and_folders}")

# os.chdir(path): Changes the current working directory
# os.chdir("test_folder")

# os.rmdir("folder_name"): Removes an empty directory
# os.rmdir("test_folder")


# FILE MANAGEMENT OPERATIONS

# Creating a dummy file for demonstration
with open("sample.txt", "w") as f:
    f.write("Hello World!")

# os.rename(old_name, new_name): Renames a file or directory
if os.path.exists("sample.txt"):
    os.rename("sample.txt", "renamed_sample.txt")

# os.remove(file_path): Deletes a file (cannot delete non-empty folders)
if os.path.exists("renamed_sample.txt"):
    os.remove("renamed_sample.txt")



#PATH OPERATIONS (os.path module)

# os.path.join(): Safely joins path components using the correct system separator
full_path = os.path.join("parent_folder", "child_folder", "file.txt")
print(f"OS-Safe Path: {full_path}")

# os.path.exists(path): Checks if a file or directory exists (Returns True/False)
path_check = os.path.exists("parent_folder")
print(f"Does path exist? {path_check}")

# os.path.isfile(path) & os.path.isdir(path): Check specific path type
print(f"Is directory? {os.path.isdir('parent_folder')}")

# os.path.abspath(path): Returns the absolute/full path
abs_path = os.path.abspath("parent_folder")
print(f"Absolute Path: {abs_path}")

# os.path.split(path): Splits a path into a tuple (head/folder, tail/filename)
folder_part, file_part = os.path.split(full_path)
print(f"Folder: {folder_part}, File: {file_part}")


#SYSTEM & ENVIRONMENT VARIABLES

# os.environ: A dictionary-like object representing system environment variables
user_home = os.environ.get("HOME") or os.environ.get("USERPROFILE")
print(f"User Home Directory: {user_home}")

# os.name: Returns the OS dependent module name ('posix' for Linux/Mac, 'nt' for Windows)
print(f"Operating System Type: {os.name}")

# os.system(command): Executes system terminal commands (e.g., 'dir' or 'ls')
# Note: For production code, the 'subprocess' module is preferred.
# os.system("echo Hello from OS Terminal")


# Clean up demo folders created above
if os.path.exists("parent_folder/child_folder"):
    os.rmdir("parent_folder/child_folder")
if os.path.exists("parent_folder"):
    os.rmdir("parent_folder")
if os.path.exists("test_folder"):
    os.rmdir("test_folder")