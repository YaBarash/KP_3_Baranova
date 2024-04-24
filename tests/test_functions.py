import os.path

import pytest
from src.functions import (get_all_operation, get_executed_operations, get_sort_operation, get_update_operations_list,
                           get_date,
                           change_date_format, masking)


def test_get_all_operation():
    DATA_FOR_TEST_PATH = os.path.join(os.path.dirname(__file__), 'data_for_test.json')
    assert get_all_operation(DATA_FOR_TEST_PATH) == [
        {
            "1": "1",
            "2": "2",
            "3": "3"
        }
    ]


def test_get_executed_operations():
    data_test_executed = [
        {"id": 518707726, "state": "EXECUTED"},
        {"id": 594226727, "state": "CANCELED"},
        {"id": 147815167, "state": "EXECUTED"}
    ]
    expected_test_executed = [
        {"id": 518707726, "state": "EXECUTED"},
        {"id": 147815167, "state": "EXECUTED"}
    ]
    assert get_executed_operations(data_test_executed) == expected_test_executed


def test_get_date():
    assert get_date(
        {
            "id": 154927927,
            "state": "EXECUTED",
            "date": "2019-11-19T09:22:25.899614",
        }
    ) == "2019-11-19T09:22:25.899614"


def test_get_sort_operation():
    data_sort_operation = [
        {"id": 104807525, "state": "EXECUTED", "date": "2019-06-01T06:46:16.803326"},
        {"id": 550607912, "state": "EXECUTED", "date": "2018-07-31T12:25:32.579413"},
        {"id": 122284694, "state": "EXECUTED", "date": "2019-08-08T21:58:06.688541"},
        {"id": 260972664, "state": "EXECUTED", "date": "2018-01-23T01:48:30.477053"},
        {"id": 317987878, "state": "EXECUTED", "date": "2018-01-13T13:00:58.458625"},
        {"id": 721227091, "state": "EXECUTED", "date": "2018-12-18T17:07:09.800800"}
    ]
    expected_sort_operation = [
        {"id": 122284694, "state": "EXECUTED", "date": "2019-08-08T21:58:06.688541"},
        {"id": 104807525, "state": "EXECUTED", "date": "2019-06-01T06:46:16.803326"},
        {"id": 721227091, "state": "EXECUTED", "date": "2018-12-18T17:07:09.800800"},
        {"id": 550607912, "state": "EXECUTED", "date": "2018-07-31T12:25:32.579413"},
        {"id": 260972664, "state": "EXECUTED", "date": "2018-01-23T01:48:30.477053"}
    ]
    assert get_sort_operation(data_sort_operation, 5) == expected_sort_operation


@pytest.mark.parametrize('data_date_format, expected_date_format',
                         [("2019-06-01T06:46:16.803326", "01.06.2019"), ("2018-07-31T12:25:32.579413", "31.07.2018")])
def test_change_date_format(data_date_format, expected_date_format):
    assert change_date_format(data_date_format) == expected_date_format


def test_get_update_operations_list():
    data_operations_list = [
        {"date": "2019-06-01T06:46:16.803326", "to": "Счет 15351391408911677994"},
        {"date": "2018-12-18T17:07:09.800800", "from": "Счет 38427597486442637521",
         "to": "MasterCard 9175985085449563"},
        {"date": "2018-02-06T06:42:02.219233", "from": "Visa Classic 4040551273087672",
         "to": "Счет 90817634362091276762"}
    ]
    expected_operations_list = [
        {"date": "01.06.2019", "to": "Счет **7994", "from": "Данные не найдены"},
        {"date": "18.12.2018", "from": "Счет **7521",
         "to": "MasterCard 9175 98** **** 9563"},
        {"date": "06.02.2018", "from": "Visa Classic 4040 55** **** 7672",
         "to": "Счет **6762"}
    ]
    get_update_operations_list(data_operations_list)
    assert data_operations_list == expected_operations_list

@pytest.mark.parametrize("account_test, account_expected", [
    ("Счет 24763316288121894080", 'Счет **4080'),
    ("Visa Gold 9447344650495960", 'Visa Gold 9447 34** **** 5960'),
    ("MasterCard 3152479541115065", 'MasterCard 3152 47** **** 5065'),
    ("Visa Platinum 5355133159258236", "Visa Platinum 5355 13** **** 8236"),
    ("", "Данные не найдены"),
    (None, "Данные не найдены")
])
def test_masking(account_test, account_expected):
    assert masking(account_test) == account_expected
