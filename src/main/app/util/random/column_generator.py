import datetime
import random
import uuid

set = set()

def get_pk():
    return uuid.uuid4()

def get_integer(is_random):
    if is_random:
        return get_random_integer()
    else:
        return 1


def get_random_integer():
    return random.randrange(0, 2140000000)


def get_real_number(data_type, is_random):
    if is_random:
        try:
            return decimal_type(data_type)
        except:
            return random.uniform(0, 999)
    else:
        return 0.1


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


def get_string(length, is_random):
    if is_random:
        return get_random_string(length)
    else:
        return 'a'


def get_random_string(length):
    random_str = []
    if length > 20:
        length = 20
    base_string = '1234567890qwertyuiopasdfghjklzxcvbnm'
    for i in range(0, length):
        choice = random.choice(base_string)
        random_str.append(choice)

    result = ''.join(random_str)
    return result


def get_date(is_random):
    # if is_random:
    return datetime.datetime(year=random.randrange(1970, 2030),
                             month=random.randrange(1, 13),
                             day=random.randrange(1, 29),
                             hour=random.randrange(0, 23),
                             minute=random.randrange(0, 60),
                             second=random.randrange(0, 60))


# else:
#     return datetime.datetime(year=9999, month=12, day=1, hour=12, minute=10, second=10)


def get_time(is_random):
    if is_random:
        return datetime.time(hour=random.randrange(0, 23),
                             minute=random.randrange(0, 60),
                             second=random.randrange(0, 60))
    else:
        return datetime.time(hour=12, minute=10, second=10)


def get_boolean():
    return random.randrange(0, 2)
