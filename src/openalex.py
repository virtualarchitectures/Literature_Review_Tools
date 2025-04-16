import json
from pyalex import (
    Works,
    Authors,
    Sources,
    Institutions,
    Topics,
    Publishers,
    Funders,
    config,
)
from time import sleep
from rich import print
import os

# Ensure the 'data/' directory exists
os.makedirs("data", exist_ok=True)

config.max_retries = 0
config.retry_backoff_factor = 0.1
config.retry_http_codes = [429, 500, 503]

pager = Works().search_filter(title="airbnb").paginate(method="page", per_page=200)

all_pages = []

file_count = 0  # Initialize a file counter

for page in pager:
    for work in page:
        file_count += 1
        print(f"Work {file_count}: {work['title']}")  # Add prefix with file counter

    # Add current page
    all_pages.append(page)
    sleep(1)

# Save the collected data to a JSON file
with open("data/works.json", "w") as f:
    json.dump(all_pages, f, indent=2)

# Print the total number of files processed
print(f"Total number of works: {file_count}")
