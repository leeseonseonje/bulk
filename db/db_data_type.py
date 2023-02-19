from enum import Enum

from src.main.app.util.random.random_generator import *


class DataType(Enum):
    INTEGER = ('int', 'bigint',)
    REAL_NUMBER = ('decimal', 'float', 'double')
    STRING = ('char', 'varchar', 'text', 'longtext', 'name')
    DATE = ('date', 'datetime', 'timestamp')
    TIME = 'time'
    BOOLEAN = ('tinyint', 'boolean', 'bit')

    @staticmethod
    def from_str(value):
        if value in DataType.INTEGER.value:
            return DataType.INTEGER
        elif value in DataType.REAL_NUMBER.value:
            return DataType.REAL_NUMBER
        elif value in DataType.STRING.value:
            return DataType.STRING
        elif value in DataType.DATE.value:
            return DataType.DATE
        elif value in DataType.TIME.value:
            return DataType.TIME
        elif value in DataType.BOOLEAN.value:
            return DataType.BOOLEAN


def type_checking_and_value_generate(data, data_type, n):
    if column_data_type(data_type) == DataType.INTEGER:
        data.append(str(random_integer(n)))

    elif column_data_type(data_type) == DataType.STRING:
        length = get_length(data_type)
        data.append(f"'{str(random_string(length, n))}'")

    elif column_data_type(data_type) == DataType.DATE:
        data.append(f"'{str(random_date())}'")

    elif column_data_type(data_type) == DataType.REAL_NUMBER:
        data.append(str(random_real_number(data_type)))

    elif column_data_type(data_type) == DataType.BOOLEAN:
        data.append(f"'{str(random_boolean())}'")

    elif column_data_type(data_type) == DataType.TIME:
        data.append(f"'{str(random_time())}'")


def column_data_type(data_type):
    return DataType.from_str(str(data_type).split('(')[0])


def get_length(data_type):
    split = str(data_type).split('(')
    length = split[1].split(')')
    return int(length[0])
