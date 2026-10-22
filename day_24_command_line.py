"""

CONCEPT DEFINITIONS:
1. Command Line Utility: A program designed to be run from the terminal or command 
   prompt, taking arguments/flags to perform specific tasks.
2. argparse: Python's built-in standard library module used for parsing command-line 
   options, arguments, and sub-commands, automatically generating help messages.

"""

import argparse
import sys


# SECTION 1: CREATING A BASIC COMMAND LINE PARSER

def setup_argparse():
    """Sets up an argument parser to handle terminal inputs."""
    parser = argparse.ArgumentParser(description="A simple command-line utility in Python.")

    # Adding positional arguments
    parser.add_argument("url", type=str, help="The target URL or file path to process.")

    # Adding optional flags (e.g., -o or --output)
    parser.add_argument("-o", "--output", type=str, default="output.txt", 
                        help="The output filename for saving results.")

    # Parse arguments from the command line
    args = parser.parse_args()
    return args



# DEMONSTRATION IN VS CODE (Simulating Execution)


if __name__ == "__main__":
    # Note: To test this in your terminal, run your script like this:
    # python script.py https://example.com -o custom_file.txt

    print("--- Command Line Utility Simulation ---")
    
    # Simulating command-line arguments for demonstration purposes inside VS Code
    # (Comment out this block if you are running it directly from the actual terminal)
    if len(sys.argv) == 1:
        print("Tip: Run this script from your terminal with arguments!")
        print("Example command: python script.py https://example.com -o results.txt\n")
    
    # If running normally via terminal:
    # args = setup_argparse()
    # print(f"Processing URL: {args.url}")
    # print(f"Saving to output file: {args.output}")