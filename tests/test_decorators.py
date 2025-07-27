from time import sleep

import pytest

from src.decorators import my_function


def test_log() -> None:
    with pytest.raises(Exception, match="Ошибка ввода данных"):
        my_function()


def test_function_sleep() -> None:
    sleep(1)
    assert my_function(1, 2)


def test_function() -> None:
    assert my_function(1, 2)


def test_log_out(capsys) -> None:
    test_function()
    captured = capsys.readouterr()
    assert captured.out == ("my_function ok.Time in work: 0.000004\n")


def test_log_capsys(capsys) -> None:
    test_function()
    captured = capsys.readouterr()
    assert captured
