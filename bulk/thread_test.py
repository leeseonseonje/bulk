from concurrent.futures import ThreadPoolExecutor


def task(m):
    print(m)


# if __name__ == '_main_':
executor = ThreadPoolExecutor(4)
executor.map(task, 5)
