import datetime
from concurrent.futures import ThreadPoolExecutor
import time


def task(m, n):
    print(f'm = ${m}m')
    print(f'n = ${n}m')


# executor = ThreadPoolExecutor(4)
# args = ((1, 2), (3, 4))
# executor.map(task, [1], [3])

now = time.time()
time.sleep(1)
end = time.time() - now
format = datetime.timedelta(seconds=end)
print(format)
# print(end)
