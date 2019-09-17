
from collections import defaultdict
d = defaultdict(int)
for i in [1, 1, 2, 3, 3, 3, 4, 5]:
 d[i] += 1

for item, count in d.items():
    print('Mode: {} Count: {}'.format(item, count))
