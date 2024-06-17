import pytest
from src.processing import filter_by_state, sort_by_date



@pytest.fixture
def data_input():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
@pytest.mark.parametrize('state, expected', [('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                              {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                                             ('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                              {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])])
def test_filter_by_state(data_input, state, expected):
     assert filter_by_state(data_input, state) == expected



#
# @pytest.fixture
# def sample_data():
#     return [
#         {"state": "EXECUTED", "date": "2022-01-15"},
#         {"state": "PENDING", "date": "2022-01-10"},
#         {"state": "EXECUTED", "date": "2022-01-20"},
#         {"state": "FAILED", "date": "2022-01-05"}
#     ]
#
# @pytest.mark.parametrize("state, expected_result", [
#     ("EXECUTED", [{"state": "EXECUTED", "date": "2022-01-15"}, {"state": "EXECUTED", "date": "2022-01-20"}]),
#     ("PENDING", [{"state": "PENDING", "date": "2022-01-10"}]),
#     ("FAILED", [{"state": "FAILED", "date": "2022-01-05"}]),
# ])
# def test_filter_by_state(sample_data, state, expected_result):
#     assert filter_by_state(sample_data, state) == expected_result
#
# @pytest.mark.parametrize("ascending, expected_result", [
#     (True, list(reversed([
#         {"state": "FAILED", "date": "2022-01-05"},
#         {"state": "PENDING", "date": "2022-01-10"},
#         {"state": "EXECUTED", "date": "2022-01-15"},
#         {"state": "EXECUTED", "date": "2022-01-20"}
#     ]))),
#     (False, list(reversed([
#         {"state": "EXECUTED", "date": "2022-01-20"},
#         {"state": "EXECUTED", "date": "2022-01-15"},
#         {"state": "PENDING", "date": "2022-01-10"},
#         {"state": "FAILED", "date": "2022-01-05"}
#     ]))),
# ])
#
# def test_sort_by_date(sample_data, ascending, expected_result):
#     assert sort_by_date(sample_data, ascending) == expected_result