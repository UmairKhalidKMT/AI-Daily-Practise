"""

CONCEPT DEFINITIONS:
1. Shutil Module: Python's standard library module for high-level file operations 
   (e.g., copying files, moving files, renaming, archiving, and tree deletion).
2. High-Level Operations: Unlike the basic `os` module (which handles individual 
   file creation and path checks), `shutil` handles bulk file manipulation and directory trees.
"""

import shutil
import os

# Create sample files and folders for demonstration
demo_dir = "sample_directory"
sub_dir = os.path.join(demo_dir, "sub_folder")
os.makedirs(sub_dir, exist_ok=True)

source_file = os.path.join(demo_dir, "notes.txt")
with open(source_file, "w") as f:
    f.write("Important Python Notes: Shutil and File Operations.")


#  
# SECTION 1: CORE `shutil` FUNCTIONS
#  

print("--- 1. shutil.copy() [Copying Files] ---")
# Copies file content and permissions to a destination file or directory
backup_file = "notes_backup.txt"
shutil.copy(source_file, backup_file)
print(f"Copied '{source_file}' to '{backup_file}'")


print("\n--- 2. shutil.copytree() [Copying Entire Directory Trees] ---")
# Recursively copies an entire directory tree including all files and subfolders
destination_dir = "backup_directory"
if os.path.exists(destination_dir):
    shutil.rmtree(destination_dir) # Clean up if it already exists

shutil.copytree(demo_dir, destination_dir)
print(f"Recursively copied directory '{demo_dir}' to '{destination_dir}'")


print("\n--- 3. shutil.move() [Moving / Renaming Files or Folders] ---")
# Moves a file or directory to a new location (can also be used for renaming)
moved_file_path = "moved_notes.txt"
shutil.move(backup_file, moved_file_path)
print(f"Moved/Renamed '{backup_file}' to '{moved_file_path}'")


print("\n--- 4. shutil.rmtree() [Deleting Directory Trees] ---")
# Recursively deletes an entire directory tree (useful for cleaning up test folders)
shutil.rmtree(destination_dir)
print(f"Deleted directory tree '{destination_dir}'")


#  
# SECTION 2: OTHER IMPORTANT FUNCTIONS TO REMEMBER
#  

print("\n--- 5. shutil.make_archive() & unpack_archive() [Archiving Files] ---")
# Creates an archive file (e.g., ZIP or TAR) of a directory
archive_name = "my_archive"
archive_format = "zip" # Options: 'zip', 'tar', 'gztar', etc.

# Creating a zip archive of demo_dir
created_archive = shutil.make_archive(archive_name, archive_format, demo_dir)
print(f"Created archive: {created_archive}")

# Unpacking/extracting the archive
extract_dir = "extracted_folder"
shutil.unpack_archive(created_archive, extract_dir)
print(f"Extracted archive into: {extract_dir}")


print("\n--- 6. shutil.disk_usage() [Checking Disk Space] ---")
# Returns disk usage statistics about the given path as a named tuple (total, used, free)
disk_stats = shutil.disk_usage(".")
print(f"Total Disk Space: {disk_stats.total / (1024**3):.2f} GB")
print(f"Used Disk Space:  {disk_stats.used / (1024**3):.2f} GB")
print(f"Free Disk Space:  {disk_stats.free / (1024**3):.2f} GB")


#  
# CLEANUP DEMO FILES & FOLDERS
#  
for temp_item in [demo_dir, moved_file_path, f"{archive_name}.{archive_format}", extract_dir]:
    if os.path.isfile(temp_item):
        os.remove(temp_item)
    elif os.path.isdir(temp_item):
        shutil.rmtree(temp_item)

print("\nCleanup completed successfully!")