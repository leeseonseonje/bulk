import datetime

from src.app.bulk.db_data_type import DataType


def test_integer_type_checking_and_value_generate():
    result = DataType.type_checking_and_value_generate('int', False)
    assert result == 1
    assert type(result) == int


def test_real_number_type_checking_and_value_generate():
    result = DataType.type_checking_and_value_generate('decimal', False)
    assert result == 0.1
    assert type(result) == float


def test_string_type_checking_and_value_generate():
    result = DataType.type_checking_and_value_generate('varchar(256)', False)
    assert result == 'a'
    assert type(result) == str


def test_date_type_checking_and_value_generate():
    result = DataType.type_checking_and_value_generate('date', False)
    assert type(result) == datetime.datetime


def test_time_type_checking_and_value_generate():
    result = DataType.type_checking_and_value_generate('time', False)
    assert result == datetime.time(12, 10, 10)
    assert type(result) == datetime.time


def test_boolean_type_checking_and_value_generate():
    result = DataType.type_checking_and_value_generate('tinyint', False)
    assert result == 0 or 1
    assert type(result) == int
