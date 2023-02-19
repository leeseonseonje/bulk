import datetime
import random


def random_integer():
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


def random_date():
    return datetime.datetime(year=random.randrange(1, 10000),
                      month=random.randrange(1, 13),
                      day=random.randrange(1, 29),
                      hour=random.randrange(1, 25),
                      minute=random.randrange(0, 60),
                      second=random.randrange(0, 60))


def random_boolean():
    return random.randrange(0, 1)


print(random_real_number('decimal(5,3)'))
print(random.randrange(1, 13))
print(random_date())
