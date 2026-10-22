"""

CONCEPT DEFINITIONS:
1. Requests Module: An elegant and simple HTTP library for Python, built for human use. 
   It allows you to send HTTP/1.1 requests (GET, POST, PUT, DELETE) effortlessly without 
   having to manually add query strings or form-encode data.

"""

import requests
import json

# SECTION 1: CORE `requests` FUNCTIONS

print("--- 1. requests.get() [Fetching Web Pages / APIs] ---")
# Sending a GET request to a public API endpoint
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

# Check if the request was successful (Status Code 200)
if response.status_code == 200:
    print(f"Status Code: {response.status_code}")
    # Parse JSON response directly into a Python dictionary
    data = response.json()
    print(f"Fetched Data: {data}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")


print("\n--- 2. requests.post() [Sending Data to an API] ---")
# Sending a POST request with payload data and headers
post_url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Python Requests Tutorial",
    "body": "Learning how to send POST requests in Python.",
    "userId": 1
}
headers = {
    "Content-type": "application/json; charset=UTF-8"
}

post_response = requests.post(post_url, json=payload, headers=headers)
print(f"POST Status Code: {post_response.status_code}")
print(f"POST Response JSON: {post_response.json()}")



# SECTION 2: OTHER IMPORTANT FUNCTIONS TO REMEMBER

print("\n--- 3. Handling Query Parameters with `params` ---")
# Passing query parameters cleanly using a dictionary
search_url = "https://jsonplaceholder.typicode.com/posts"
query_params = {"userId": 1}

param_response = requests.get(search_url, params=query_params)
print(f"Filtered Posts Count: {len(param_response.json())}")


print("\n--- 4. Handling Request Timeouts (`timeout`) ---")
# Always use timeouts in production code to prevent scripts from hanging indefinitely
try:
    timeout_response = requests.get("https://api.github.com", timeout=3)
    print(f"GitHub API Reachable! Status: {timeout_response.status_code}")
except requests.exceptions.Timeout:
    print("The request timed out.")


print("\n--- 5. Checking Response Content Types & Text ---")
# Inspecting raw text or binary content (e.g., for downloading images)
google_res = requests.get("https://www.google.com")
print(f"Response Encoding: {google_res.encoding}")
print(f"HTML snippet (first 100 chars): {google_res.text[:100]}...")