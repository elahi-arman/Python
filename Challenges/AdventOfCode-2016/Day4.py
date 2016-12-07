import re
from collections import defaultdict

with open('Day4.in', 'r') as f:
    validRooms = 0
    for line in f:
        match = re.match(r'([a-z\-]*)([0-9]*)(\[[a-z]*\])',line)
        encrypted = match.group(1).replace("-", "")
        sectorID = match.group(2)
        checksum = match.group(3)[1:-1]

        frequencies = defaultdict(int)
        for char in encrypted:
            frequencies[char] += 1

        # http://stackoverflow.com/a/9919379 -- WTF PYTHON
        actualChecksum = ''.join([v[0] for v in sorted(frequencies.items(), key=lambda kv: (-kv[1], kv[0]))])
        actualChecksum = actualChecksum[0:5] # only want the first 5 letters

        if actualChecksum == checksum:
            validRooms += int(sectorID)

    print(validRooms)
