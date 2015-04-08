import pytest
import break_me


def test_name_error():
    with pytest.raises(NameError):
        break_me.name_error(name)
