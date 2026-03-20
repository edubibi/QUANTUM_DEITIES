
import os
import re

collection_path = r"C:\Users\Usuario\.gemini\antigravity\scratch\QUANTUM_DEITIES\COLLECTION_151"
files = os.listdir(collection_path)
numbers = set()
for f in files:
    match = re.search(r'_(\d+)\.png$', f)
    if match:
        numbers.add(int(match.group(1)))

batch_4 = set(range(162, 182))
missing_batch_4 = batch_4 - numbers
found_batch_4 = batch_4 & numbers

print(f"Batch 4 (162-181):")
print(f" - Found: {len(found_batch_4)}")
print(f" - Missing: {len(missing_batch_4)}")
if missing_batch_4:
    print(f" - Missing numbers: {sorted(list(missing_batch_4))}")

others = numbers - batch_4
print(f"\nOther images found: {len(others)}")
print(f"Total unique numbered images: {len(numbers)}")
