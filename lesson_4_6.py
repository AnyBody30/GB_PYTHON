from itertools import count
from itertools import cycle
from datetime import datetime

for x in count(3):
    if x > 10:
        break
    else:
        print(x)


start_time = datetime.timestamp(datetime.now())
for x in cycle([1, 2, 3]):
    print(x)
    if datetime.timestamp(datetime.now()) - start_time > 0.0001:
        break
