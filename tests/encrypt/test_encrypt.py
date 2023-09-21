import pytest

from challenges.challenge_encrypt_message import encrypt_message

# from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError) as type_error_key:
        encrypt_message("test", "re")

    assert str(type_error_key.value) == "tipo inválido para key"

    with pytest.raises(TypeError) as type_error_message:
        encrypt_message(123234, 3)

    assert str(type_error_message.value) == "tipo inválido para message"

    assert encrypt_message("teste", 5) == "etset"
    assert encrypt_message("teste", 2) == "ets_et"
    assert encrypt_message("teste", 3) == "set_et"
    assert encrypt_message("hello", 8) == "olleh"
