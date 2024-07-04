from src.decorators import my_function
# import os


def test_log_decorator_success(capsys):
    result = my_function(1, 2)
    assert result == 3
    captured = capsys.readouterr()
    assert "my_function ok" in captured.err
#

# def test_log_decorator_file_output():
#     my_function(1, 2)
#     assert os.path.exists("mylog.txt")
#     with open("mylog.txt", "r") as file:
#          lines = file.readlines()
#          assert "my_function ok" in lines[-1]
#     os.remove("mylog.txt")
