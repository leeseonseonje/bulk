from enum import Enum

from src.app.util.random.column_generator import *


class DataType(Enum):
    INTEGER = ('int', 'bigint',)
    REAL_NUMBER = ('decimal', 'float', 'double')
    STRING = ('char', 'varchar', 'text', 'longtext', 'name')
    DATE = ('date', 'datetime', 'timestamp')
    TIME = 'time'
    BOOLEAN = ('tinyint', 'boolean', 'bit')

    @staticmethod
    def type_checking_and_value_generate(data_type, is_random):
        if get_data_type(data_type) in DataType.INTEGER.value:
            return get_integer(is_random)
        elif get_data_type(data_type) in DataType.REAL_NUMBER.value:
            return get_real_number(data_type, is_random)
        elif get_data_type(data_type) in DataType.STRING.value:
            length = get_length(data_type)
            return get_string(length, is_random)
        elif get_data_type(data_type) in DataType.DATE.value:
            return get_date(is_random)
        elif get_data_type(data_type) in DataType.TIME.value:
            return get_time(is_random)
        elif get_data_type(data_type) in DataType.BOOLEAN.value:
            return get_boolean()


def get_data_type(data_type):
    return str(data_type).split('(')[0]


def get_length(data_type):
    split = str(data_type).split('(')
    length = split[1].split(')')
    return int(length[0])
