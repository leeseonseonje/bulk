from concurrent.futures import ThreadPoolExecutor


def task(m, n):
    print(f'm = ${m}m')
    print(f'n = ${n}m')


executor = ThreadPoolExecutor(4)
args = ((1, 2), (3, 4))
executor.map(task, [1], [3])
