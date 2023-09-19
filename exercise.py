import re

name_pattern = r'([A-Z][a-z]+)\s+([A-Z][a-z]+)'

with open('names.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    match = re.search(name_pattern, line)
    if match:
        first_name = match.group(1)
        last_name = match.group(2)
        print(f"{first_name} {last_name}")
    else:
        print(None)