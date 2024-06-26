from src.decorators import my_function


def test_log_decorator_success(capsys):
    result = my_function(1, 2)
    assert result == 3
    captured = capsys.readouterr()
    assert "my_function ok" in captured.err
