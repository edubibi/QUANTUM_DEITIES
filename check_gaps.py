
import os
import re

collection_path = r"C:\Users\Usuario\.gemini\antigravity\scratch\QUANTUM_DEITIES\COLLECTION_151"
files = os.listdir(collection_path)
numbers = []
for f in files:
    match = re.search(r'_(\d+)\.png$', f)
    if match:
        numbers.append(int(match.group(1)))

if not numbers:
    print("No numbered files found.")
else:
    numbers.sort()
    all_nums = set(range(1, max(numbers) + 1))
    missing = all_nums - set(numbers)
    print(f"Max number: {max(numbers)}")
    print(f"Total count (set): {len(set(numbers))}")
    if missing:
        print(f"Missing numbers: {sorted(list(missing))[:20]}")
    else:
        print("No gaps in sequence.")
