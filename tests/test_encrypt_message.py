import pytest

from challenges.challenge_encrypt_message import encrypt_message


@pytest.mark.xfail(reason="expected fail when string is passed as key")
def test_type_error_with_string_key():
    message = "test"
    numbers = "re"

    with pytest.raises(TypeError) as type_error:
        encrypt_message(message, numbers)

    assert str(type_error.value) == "tipo inválido para key"


@pytest.mark.xfail(reason="expected fail when number is passed as message")
def test_type_error_with_int_message():
    message = 123234
    numbers = 3

    with pytest.raises(TypeError) as type_error:
        encrypt_message(message, numbers)

    assert str(type_error.value) == "tipo inválido para message"


def test_return_reverse_message():
    message = "teste"
    numbers = 5

    assert encrypt_message(message, numbers) == "etset"


def test_with_odd_number():
    message = "teste"
    numbers = 3

    assert encrypt_message(message, numbers) == "set_et"


def test_with_even_number():
    message = "teste"
    numbers = 2

    assert encrypt_message(message, numbers) == "ets_et"


def test_positive_valid_index():
    message = "hello"
    numbers = 8

    assert encrypt_message(message, numbers) == "olleh"
