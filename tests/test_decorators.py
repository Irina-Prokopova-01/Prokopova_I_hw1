import pytest
from src.decorators import log, my_function

# def test_log(capsys):
#     with pytest.raises(Exception):
#         captured = capsys.readouterr()
#         assert captured.out == f"my_function error: {e}. Inputs:{args}, {kwargs}\n"

def test_log():
    with pytest.raises(Exception, match='my_function error: {e}. Inputs:{args}, {kwargs}'):
        my_function()


def test_my_function():
    @my_function
    def add_numbers(x, y):
        return x + y

    result = add_numbers(3, 5)
    assert result == 8