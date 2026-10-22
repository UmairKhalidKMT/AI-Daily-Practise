"""
================================================================================
CONCEPT DEFINITIONS:
1. Regular Expression (RegEx): A sequence of characters that forms a search pattern, 
   used for string matching, searching, and data extraction.
2. `re` Module: Python's built-in module providing regular expression matching operations 
   similar to those found in Perl.
3. Meta-characters: Special characters (`^`, `$`, `*`, `+`, `?`, `[]`, `{}`, `|`, `()`) 
   that give special meaning to RegEx patterns.
================================================================================
"""

import re

# Sample text for searching and matching
sample_text = """
Contact us at support@codewithharry.com or admin@python-tutorial.org.
You can also reach out via mobile at +91-9876543210 or 987-654-3210.
Order IDs are #1023, #4589, and #9981.
"""

# ==============================================================================
# SECTION 1: CORE `re` MODULE FUNCTIONS
# ==============================================================================

print("--- 1. re.search() [Finding the First Match] ---")
# Searches for the first occurrence of a pattern in the string and returns a match object
pattern = r"support@codewithharry\.com"
match = re.search(pattern, sample_text)

if match:
    print(f"Found match: {match.group()}")
    print(f"Match span (start, end): {match.span()}")
else:
    print("No match found.")


print("\n--- 2. re.findall() [Finding All Matches] ---")
# Finds all occurrences of a pattern and returns them as a list of strings
email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
emails = re.findall(email_pattern, sample_text)
print(f"Extracted Emails: {emails}")


print("\n--- 3. re.finditer() [Iterating Over All Matches with Details] ---")
# Returns an iterator yielding match objects for all matches, providing span and group info
order_pattern = r"#\d{4}"
print("Searching for Order IDs:")
for match in re.finditer(order_pattern, sample_text):
    print(f"Found '{match.group()}' at position {match.span()}")


print("\n--- 4. re.sub() [Search and Replace] ---")
# Replaces occurrences of the pattern with a replacement string
phone_pattern = r"\+?91[-]?\d{10}|\d{3}-\d{3}-\d{4}"
masked_text = re.sub(phone_pattern, "[PHONE_MASKED]", sample_text)
print(f"\nMasked Text Output:\n{masked_text.strip()}")


# ==============================================================================
# SECTION 2: OTHER IMPORTANT FUNCTIONS & PATTERNS TO REMEMBER
# ==============================================================================

print("\n--- 5. re.match() [Checking Match at the Beginning] ---")
# Checks for a match ONLY at the beginning of the string
start_match = re.match(r"\nContact", sample_text)
if start_match:
    print("Matched at the start of the string!")
else:
    print("Did not match at the very beginning of the string.")


print("\n--- 6. re.split() [Splitting Strings by Pattern] ---")
# Splits a string by the occurrences of the pattern
split_pattern = r"[,.]\s+"
sentences = re.split(split_pattern, sample_text.strip())
print(f"First 2 split segments: {sentences[:2]}")