import datetime
import random

string_set = set()
integer_set = set()


def random_integer(n):
    while True:
        random_int = get_random_integer()
        integer_set.add(random_int)
        if n > len(integer_set):
            random_int = get_random_integer()
            integer_set.add(random_int)
        if n == len(integer_set):
            break
    return random_int


def get_random_integer():
    return random.randrange(0, 2140000000)


def random_real_number(data_type: str):
    try:
        return decimal_type(data_type)
    except:
        return random.uniform(0, 999)


def decimal_type(data_type):
    length = len(data_type)
    split = data_type[length - 4:length - 1].split(',')
    precision = int(split[0])
    scale = int(split[1])
    max_range = 1
    for i in range(precision - 1):
        max_range = max_range * 10
    real_number = random.uniform(0, max_range)
    return round(real_number, scale)


def random_string(length, n):
    while True:
        random_str = get_random_string(length)
        string_set.add(random_str)
        if n > len(string_set):
            random_str = get_random_string(length)
            string_set.add(random_str)
        if n == len(string_set):
            break
    return random_str


def get_random_string(length):
    random_str = []
    if length > 5:
        length = 5
    base_string = '1234567890qwertyuiopasdfghjklzxcvbnm'
    for i in range(0, length):
        choice = random.choice(base_string)
        random_str.append(choice)

    result = ''.join(random_str)
    return result


def random_date():
    return datetime.datetime(year=random.randrange(1, 10000),
                             month=random.randrange(1, 13),
                             day=random.randrange(1, 29),
                             hour=random.randrange(0, 23),
                             minute=random.randrange(0, 60),
                             second=random.randrange(0, 60))


def random_boolean():
    return random.randrange(0, 1)


# n = 1000000
# s = set()
# for i in range(0, n):
#     s.add(random_string(256, i + 1))
    # s.add(random_integer(i + 1))
#
# print(len(integer_set))
# print(len(s))
